from rest_framework import serializers
from ..models.rule import Rule



class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rule
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")