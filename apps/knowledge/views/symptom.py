from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ...users.permissions import IsAdminGroup
from ..models.symptom import Symptom
from ..serializers.symptom import SymptomSerializer


class SymptomListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminGroup()]

        return [IsAuthenticated()]

    def get(self, request):
        symptoms = Symptom.objects.all()

        serializer = SymptomSerializer(
            symptoms,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = SymptomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "message": "Symptom berhasil ditambahkan.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class SymptomDetailView(APIView):

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAdminGroup()]

        return [IsAuthenticated()]

    def get_object(self, id):
        return get_object_or_404(Symptom, id=id)

    def get(self, request, id):
        symptom = self.get_object(id)

        serializer = SymptomSerializer(symptom)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, id):
        symptom = self.get_object(id)

        serializer = SymptomSerializer(
            symptom,
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Symptom berhasil diperbarui.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, id):
        symptom = self.get_object(id)

        symptom.delete()

        return Response(
            {
                "message": "Symptom berhasil dihapus.",
            },
            status=status.HTTP_200_OK,
        )