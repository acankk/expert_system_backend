from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ...users.permissions import IsAdminGroup
from ..models.recommendation import Recommendation
from ..serializers.recommendation import RecommendationSerializer


class RecommendationListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminGroup()]

        return [IsAuthenticated()]

    def get(self, request):
        recommendations = Recommendation.objects.all()

        serializer = RecommendationSerializer(
            recommendations,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = RecommendationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Recommendation berhasil ditambahkan.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class RecommendationDetailView(APIView):

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAdminGroup()]

        return [IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(
            Recommendation,
            pk=pk,
        )

    def get(self, request, pk):
        recommendation = self.get_object(pk)

        serializer = RecommendationSerializer(recommendation)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        recommendation = self.get_object(pk)

        serializer = RecommendationSerializer(
            recommendation,
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Recommendation berhasil diperbarui.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk):
        recommendation = self.get_object(pk)

        recommendation.delete()

        return Response(
            {
                "message": "Recommendation berhasil dihapus.",
            },
            status=status.HTTP_200_OK,
        )