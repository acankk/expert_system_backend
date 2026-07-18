from rest_framework import serializers

from ..models.symptom import Symptom


class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = "__all__"

        read_only_fields = (
            "code",
            "created_at",
            "updated_at",
        )


