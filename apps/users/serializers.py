from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User
from rest_framework.permissions import BasePermission
from django.db import transaction

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "first_name",
            "username",
            "email",
            "password",
            "birth_date",
            "profile_picture",
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        group, created = Group.objects.get_or_create(name="User")
        user.groups.add(group)

        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True, trim_whitespace=False)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "first_name",
            "username",
            "email",
            "birth_date",
            "profile_picture",
        )





class IsAdminGroup(BasePermission):
    message = "Hanya Admin yang dapat mengakses endpoint ini."

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Admin").exists()