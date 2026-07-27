from rest_framework import serializers

from ..models.rule import Rule


class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rule
        fields = [
            "id",
            "disease",
            "symptom",
            "cf_expert",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]