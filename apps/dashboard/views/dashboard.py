from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.users.permissions import IsAdminGroup

from apps.knowledge.models.disease import Disease
from apps.knowledge.models.symptom import Symptom
from apps.knowledge.models.rule import Rule
from apps.knowledge.models.recommendation import Recommendation


class DashboardView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdminGroup,
    ]

    def get(self, request):

        data = {
            "total_diseases": Disease.objects.count(),
            "total_symptoms": Symptom.objects.count(),
            "total_rules": Rule.objects.count(),
            "total_recommendations": Recommendation.objects.count(),
        }

        return Response(data)