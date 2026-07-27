from rest_framework import serializers


class SymptomInputSerializer(serializers.Serializer):
    symptom = serializers.IntegerField()

    cf_user = serializers.DecimalField(
        max_digits=2,
        decimal_places=1,
    )


class DiagnosisRequestSerializer(serializers.Serializer):
    symptoms = SymptomInputSerializer(
        many=True,
    )


