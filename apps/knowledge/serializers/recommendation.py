from rest_framework import serializers

from ..models.recommendation import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = [
            "id",
            "disease",
            "min_cf",
            "max_cf",
            "confidence",
            "recommendation",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        disease = attrs.get("disease", getattr(self.instance, "disease", None))
        min_cf = attrs.get("min_cf", getattr(self.instance, "min_cf", None))
        max_cf = attrs.get("max_cf", getattr(self.instance, "max_cf", None))

        if min_cf < 0 or max_cf > 1:
            raise serializers.ValidationError(
                "Nilai CF harus berada pada rentang 0 sampai 1."
            )

        if min_cf >= max_cf:
            raise serializers.ValidationError(
                "Nilai min_cf harus lebih kecil dari max_cf."
            )

        overlap = Recommendation.objects.filter(
            disease=disease,
            min_cf__lt=max_cf,
            max_cf__gt=min_cf,
        )

        if self.instance:
            overlap = overlap.exclude(pk=self.instance.pk)

        if overlap.exists():
            raise serializers.ValidationError(
                "Rentang CF bertabrakan dengan rekomendasi lain untuk penyakit ini."
            )

        return attrs