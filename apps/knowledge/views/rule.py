from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ...users.permissions import IsAdminGroup
from ..models.rule import Rule
from ..serializers.rule import RuleSerializer


class RuleListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminGroup()]
        
        return [IsAuthenticated()]
    

    def get(self, request):

        rules = Rule.objects.all()

        serializer = RuleSerializer(rules, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK,)
    
    def post(self, request):
        serializer = RuleSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Rule berhasil ditambahkan.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
    

class RuleDetailView(APIView):

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAdminGroup()]
        
        return [IsAuthenticated()]
    
    def get_object(self, id):
        return get_object_or_404(Rule, id=id)


    def get(self, request, id):
        rule = self.get_object(id)
        serializer = RuleSerializer(rule)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def put(self, request, id):
        rule = self.get_object(id)

        serializer = RuleSerializer(
            rule,
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Rule berhasil diperbarui.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    

    def delete(self, request, id):
        rule = self.get_object(id)

        rule.delete()

        return Response(
            {
                "message": "Rule berhasil dihapus.",
            },
            status=status.HTTP_200_OK,
        )