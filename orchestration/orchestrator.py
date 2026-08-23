from AGENTS import constraint_agent, goal_agent, priority_agent, review_agent, scenario_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "goals": goal_agent.run(case),
        "constraints": constraint_agent.run(case),
        "priorities": priority_agent.run(case),
        "scenarios": scenario_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_life_plan_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
