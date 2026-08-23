"""Fail-closed governance for F161 Agentic Life Planner."""

PROTECTED_ACTIONS = {
    "make_irreversible_life_decision",
    "spend_or_transfer_money",
    "enter_or_terminate_legal_commitment",
    "make_medical_or_mental_health_decision",
    "impersonate_user_or_contact_third_party",
    "override_user_values_consent_or_autonomy",
}

REQUIRED_REVIEWS = (
    "goals_values_reviewed",
    "constraints_commitments_reviewed",
    "priorities_tradeoffs_reviewed",
    "scenario_uncertainty_reviewed",
    "wellbeing_safety_reviewed",
    "financial_legal_boundary_reviewed",
    "privacy_autonomy_reviewed",
    "user_approval_reviewed",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "irreversible decision, money movement, legal commitment, medical decision, third-party impersonation, or autonomy override is outside planner authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required life-planning review", "missing": missing}
    checks = {
        "goal_value_conflict": "material conflict among stated goals, values, identity commitments, or desired outcomes remains unresolved",
        "constraint_capacity_gap": "material time, energy, caregiving, work, family, accessibility, resource, dependency, or existing-commitment constraint remains unresolved",
        "priority_tradeoff_gap": "material priority, opportunity-cost, sequencing, dependency, or sacrifice is hidden or unresolved",
        "scenario_uncertainty_gap": "material uncertainty, assumption, downside, reversibility, contingency, or scenario risk remains unresolved",
        "wellbeing_safety_risk": "material wellbeing, coercion, exploitation, burnout, self-neglect, unsafe behavior, or crisis concern remains unresolved",
        "financial_legal_boundary_risk": "material financial, tax, legal, contractual, immigration, employment, insurance, or regulated-advice issue requires qualified review",
        "privacy_autonomy_risk": "material privacy, sensitive-data, consent, manipulation, dependency, autonomy, or third-party-boundary concern remains unresolved",
        "provenance_review_gap": "material goal, constraint, assumption, recommendation, source, decision, revision, or user-approval provenance is incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "life-planning governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "life-plan package approved for user-controlled consideration"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
