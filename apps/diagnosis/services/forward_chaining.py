from apps.knowledge.models.disease import Disease
from apps.knowledge.models.rule import Rule


def forward_chaining(symptoms):
    candidates = []

    diseases = Disease.objects.all()

    for disease in diseases:

        rules = Rule.objects.filter(
            disease=disease,
        )

        matched_rules = []

        for rule in rules:

            for symptom in symptoms:

                if rule.symptom_id == symptom["symptom"]:

                    matched_rules.append(
                        {
                            "rule": rule,
                            "cf_user": symptom["cf_user"],
                        }
                    )

                    break

        if matched_rules:

            candidates.append(
                {
                    "disease": disease,
                    "rules": matched_rules,
                }
            )

    return candidates