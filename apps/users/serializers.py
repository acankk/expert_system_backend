from django.db import transaction
from django.contrib.auth.models import Group

from rest_framework import serializers
from rest_framework.permissions import BasePermission

from .models import User


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
            "password": {
                "write_only": True,
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        group, _ = Group.objects.get_or_create(
            name="User",
        )

        user.groups.add(group)

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )


class ProfileSerializer(serializers.ModelSerializer):

    groups = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "username",
            "email",
            "birth_date",
            "profile_picture",
            "groups",
        )

    def get_groups(self, obj):
        return list(
            obj.groups.values_list(
                "name",
                flat=True,
            )
        )


class IsAdminGroup(BasePermission):

    message = "Hanya Admin yang dapat mengakses endpoint ini."

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return request.user.groups.filter(
            name="Admin",
        ).exists()