from rest_framework import serializers

from ..models.diagnosis_detail import DiagnosisDetail


class DiagnosisDetailSerializer(serializers.ModelSerializer):
    symptom = serializers.CharField(
        source="symptom.name",
    )

    class Meta:
        model = DiagnosisDetail
        fields = [
            "symptom",
            "cf_user",
            "cf_expert",
            "cf_result",
        ]