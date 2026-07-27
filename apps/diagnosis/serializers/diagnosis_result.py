from rest_framework import serializers


class DiagnosisResponseSerializer(serializers.Serializer):
    disease_id = serializers.IntegerField()

    disease_code = serializers.CharField()

    disease_name = serializers.CharField()

    cf_result = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    confidence = serializers.CharField()

    recommendation = serializers.CharField()
    