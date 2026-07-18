from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ...users.permissions import IsAdminGroup
from ..models.disease import Disease
from ..serializers.disease import DiseaseSerializer


class DiseaseListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminGroup()]

        return [IsAuthenticated()]

    def get(self, request):
        diseases = Disease.objects.all()

        serializer = DiseaseSerializer(
            diseases,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = DiseaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "message": "Disease berhasil ditambahkan.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class DiseaseDetailView(APIView):

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAdminGroup()]

        return [IsAuthenticated()]

    def get_object(self, id):
        return get_object_or_404(Disease, id=id)

    def get(self, request, id):
        disease = self.get_object(id)

        serializer = DiseaseSerializer(disease)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, id):
        disease = self.get_object(id)

        serializer = DiseaseSerializer(
            disease,
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Disease berhasil diperbarui.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, id):
        disease = self.get_object(id)

        disease.delete()

        return Response(
            {
                "message": "Disease berhasil dihapus.",
            },
            status=status.HTTP_200_OK,
        )