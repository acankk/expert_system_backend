from rest_framework import serializers

from apps.knowledge.models.disease import Disease


class DiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disease
        fields = [
            "id",
            "code",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "code",
            "created_at",
            "updated_at",
        ]