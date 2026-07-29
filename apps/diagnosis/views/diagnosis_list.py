from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.diagnosis.models.diagnosis import Diagnosis
from apps.diagnosis.serializers.diagnosis import DiagnosisSerializer


class DiagnosisListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        diagnoses = (
            Diagnosis.objects.filter(
                user=request.user,
            )
            .select_related(
                "result_disease",
                "recommendation",
            )
        )

        sort = request.query_params.get("sort")

        if sort == "newest":
            diagnoses = diagnoses.order_by("-created_at")

        elif sort == "oldest":
            diagnoses = diagnoses.order_by("created_at")

        disease = request.query_params.get("disease")

        if disease:
            diagnoses = diagnoses.filter(
                result_disease_id=disease,
            )

        serializer = DiagnosisSerializer(
            diagnoses,
            many=True,
        )

        return Response(
            serializer.data,
        )