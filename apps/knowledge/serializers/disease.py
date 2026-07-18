from rest_framework import serializers

from ..models.disease import Disease


class DiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disease
        fields = "__all__"
        read_only_fields = (
            "code",
            "created_at",
            "updated_at",
        )