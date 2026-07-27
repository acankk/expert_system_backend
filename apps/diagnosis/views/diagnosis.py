from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.diagnosis.models.diagnosis import Diagnosis
from apps.diagnosis.models.diagnosis_detail import DiagnosisDetail
from apps.diagnosis.serializers.diagnosis_request import DiagnosisRequestSerializer
from apps.diagnosis.services.certainty_factor import certainty_factor
from apps.diagnosis.services.forward_chaining import forward_chaining
from apps.knowledge.models.recommendation import Recommendation


class DiagnosisView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):

        serializer = DiagnosisRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        symptoms = serializer.validated_data["symptoms"]

        candidates = forward_chaining(
            symptoms,
        )

        if not candidates:
            return Response(
                {
                    "message": "Tidak ditemukan penyakit yang sesuai dengan gejala.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = certainty_factor(
            candidates,
        )

        recommendation = get_object_or_404(
            Recommendation,
            disease=result["disease"],
            min_cf__lte=result["cf_result"],
            max_cf__gte=result["cf_result"],
        )

        diagnosis = Diagnosis.objects.create(
            user=request.user,
            result_disease=result["disease"],
            recommendation=recommendation,
            cf_result=result["cf_result"],
        )

        for detail in result["details"]:

            DiagnosisDetail.objects.create(
                diagnosis=diagnosis,
                symptom=detail["rule"].symptom,
                cf_user=detail["cf_user"],
                cf_expert=detail["cf_expert"],
                cf_result=detail["cf_result"],
            )

        return Response(
            {
                "message": "Diagnosis berhasil.",
                "data": {
                    "id": diagnosis.id,
                    "disease": diagnosis.result_disease.name,
                    "cf_result": diagnosis.cf_result,
                    "confidence": recommendation.confidence,
                    "recommendation": recommendation.recommendation,
                },
            },
            status=status.HTTP_201_CREATED,
        )