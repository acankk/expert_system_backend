from decimal import Decimal


def certainty_factor(candidates):
    results = []

    for candidate in candidates:

        disease = candidate["disease"]
        matched_rules = candidate["rules"]

        cf_combine = None

        details = []

        for matched_rule in matched_rules:

            rule = matched_rule["rule"]

            cf_user = Decimal(str(matched_rule["cf_user"]))
            cf_expert = Decimal(str(rule.cf_expert))

            cf = cf_user * cf_expert

            details.append(
                {
                    "rule": rule,
                    "cf_user": cf_user,
                    "cf_expert": cf_expert,
                    "cf_result": cf,
                }
            )

            if cf_combine is None:
                cf_combine = cf

            else:
                cf_combine = cf_combine + (
                    cf * (Decimal("1") - cf_combine)
                )

        results.append(
            {
                "disease": disease,
                "cf_result": cf_combine,
                "details": details,
            }
        )

    if not results:
        return None

    results.sort(
        key=lambda item: item["cf_result"],
        reverse=True,
    )

    return results[0]