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

        serializer = DiagnosisSerializer(
            diagnoses,
            many=True,
        )

        return Response(
            serializer.data,
        ) 