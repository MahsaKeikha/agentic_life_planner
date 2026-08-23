from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("goals", "constraints", "priorities", "scenarios", "review"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_life_plan_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_plan_can_release():
    assert authorize("release_life_plan_package", approved_context())["allowed"] is True


def test_goal_conflict_blocks():
    assert authorize("release_life_plan_package", approved_context() | {"goal_value_conflict": True})["allowed"] is False


def test_capacity_gap_blocks():
    assert authorize("release_life_plan_package", approved_context() | {"constraint_capacity_gap": True})["allowed"] is False


def test_wellbeing_risk_blocks():
    assert authorize("release_life_plan_package", approved_context() | {"wellbeing_safety_risk": True})["allowed"] is False


def test_privacy_autonomy_risk_blocks():
    assert authorize("release_life_plan_package", approved_context() | {"privacy_autonomy_risk": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
