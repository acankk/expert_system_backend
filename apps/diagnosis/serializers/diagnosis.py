from rest_framework import serializers

from ..models.diagnosis import Diagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    disease = serializers.CharField(
        source="result_disease.name",
        read_only=True,
    )

    confidence = serializers.CharField(
        source="recommendation.confidence",
        read_only=True,
    )

    recommendation = serializers.CharField(
        source="recommendation.recommendation",
        read_only=True,
    )

    class Meta:
        model = Diagnosis
        fields = [
            "id",
            "user",
            "disease",
            "cf_result",
            "confidence",
            "recommendation",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]