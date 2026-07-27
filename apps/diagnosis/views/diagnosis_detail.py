from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.diagnosis.models.diagnosis import Diagnosis
from apps.diagnosis.serializers.diagnosis import DiagnosisSerializer
from apps.diagnosis.serializers.diagnosis_detail import DiagnosisDetailSerializer


class DiagnosisDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        diagnosis = get_object_or_404(
            Diagnosis.objects.select_related(
                "result_disease",
                "recommendation",
            ).prefetch_related(
                "details__symptom",
            ),
            pk=pk,
            user=request.user,
        )

        diagnosis_serializer = DiagnosisSerializer(
            diagnosis,
        )

        detail_serializer = DiagnosisDetailSerializer(
            diagnosis.details.all(),
            many=True,
        )

        return Response(
            {
                "diagnosis": diagnosis_serializer.data,
                "details": detail_serializer.data,
            }
        )