"""Held-out governance scenarios for F161."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"goal_value_conflict": True}, False),
    (base() | {"constraint_capacity_gap": True}, False),
    (base() | {"priority_tradeoff_gap": True}, False),
    (base() | {"scenario_uncertainty_gap": True}, False),
    (base() | {"wellbeing_safety_risk": True}, False),
    (base() | {"financial_legal_boundary_risk": True}, False),
    (base() | {"privacy_autonomy_risk": True}, False),
    (base() | {"provenance_review_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_life_plan_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F161 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
