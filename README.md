# F161 | Agentic Life Planner | L3 Gold Standard | v1.0

A governed five-agent reference architecture for personal planning across goals, values, constraints, priorities, tradeoffs, scenarios, reviews, adaptation, privacy, autonomy, and user-controlled decisions.

F161 is a planning and reflection system. It is not a therapist, physician, lawyer, financial adviser, immigration adviser, employer, guardian, fiduciary, or autonomous decision maker. It cannot make irreversible life decisions, move money, enter legal commitments, make medical decisions, impersonate the user, contact third parties as the user, or override the user's values, consent, or autonomy.

## Life-planning lifecycle

```text
Current Context and Values
        -> Goals and Desired Outcomes
        -> Constraints and Existing Commitments
        -> Priorities and Tradeoffs
        -> Scenarios, Uncertainty, and Contingencies
        -> User Review and Revision
        -> User-Controlled Action
```

The workflow fails closed when required reviews are missing or when material goal conflicts, capacity constraints, hidden tradeoffs, scenario uncertainty, wellbeing concerns, regulated-advice boundaries, privacy issues, autonomy concerns, or provenance gaps remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Goal Agent | Structures goals, values, desired outcomes, horizons, motivations, dependencies, and definitions of progress | What does the user actually want, and why does it matter to them? |
| Constraint Agent | Identifies time, energy, resources, obligations, dependencies, caregiving, work, family, accessibility, and hard boundaries | What realities constrain the plan? |
| Priority Agent | Compares importance, urgency, opportunity cost, sequencing, reversibility, and competing commitments | What deserves attention now, and what must wait or be declined? |
| Scenario Agent | Tests assumptions, uncertainty, downside, upside, contingencies, alternative paths, and reversibility | How does the plan behave when reality differs from expectations? |
| Review Agent | Synthesizes the plan, unresolved tensions, milestones, review cadence, user approvals, and adaptation rules | Is this a coherent plan the user understands and chooses? |

## Repository structure

```text
AGENTS/
├── goal_agent.py
├── constraint_agent.py
├── priority_agent.py
├── scenario_agent.py
└── review_agent.py

SKILLS/
├── goal_decomposition.py
├── prioritization.py
├── tradeoff_reasoning.py
├── scenario_planning.py
└── reflection.py

TOOLS/
├── goal_registry.py
├── constraint_ledger.py
├── priority_matrix.py
├── scenario_matrix.py
└── approval_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## User autonomy

The user remains the decision maker. F161 can organize possibilities, reveal conflicts, compare tradeoffs, and support reflection, but it should not pressure the user toward the system's preferred lifestyle, identity, relationship, career, location, financial choice, or definition of success.

## Goals and values

The executable policy requires `goals_values_reviewed`. `goal_value_conflict` blocks release when material conflicts among stated goals, values, identity commitments, or desired outcomes remain unresolved.

Goals should be written in the user's terms rather than converted automatically into conventional markers such as income, status, productivity, marriage, home ownership, or career advancement.

## Goal hierarchy

A planning system can distinguish life directions, multi-year outcomes, annual goals, projects, milestones, habits, and next actions. Lower-level actions should connect to higher-level intent where possible.

## Values

Values can guide choices when goals conflict. F161 should not infer values from demographic characteristics, profession, family role, culture, or prior behavior without user confirmation.

## Identity and self-concept

Identity can influence motivation, but the planner should avoid rigid labels. A plan should leave room for growth, experimentation, and changing preferences.

## Definitions of success

Success criteria should be explicit enough for the user to recognize progress while allowing qualitative outcomes that cannot be reduced to one metric.

## Multiple horizons

Planning can use near-term, quarterly, annual, multi-year, and open-ended horizons. Long-range plans should carry more uncertainty than immediate commitments.

## Goal decomposition

Large goals can be decomposed into outcomes, prerequisites, projects, milestones, experiments, and next actions.

Decomposition should not create false certainty about complex life paths.

## Constraints architecture

The executable policy requires `constraints_commitments_reviewed`. `constraint_capacity_gap` blocks release when material time, energy, caregiving, work, family, accessibility, resource, dependency, or existing-commitment constraints remain unresolved.

## Time

A calendar contains finite capacity. Plans should account for existing commitments, travel, transitions, recovery time, administrative work, and unplanned events rather than assuming every unscheduled hour is available.

## Energy

Tasks have different cognitive, emotional, physical, and social demands. F161 can help the user match demanding work to appropriate periods without making medical claims about energy or health.

## Attention

Attention is limited. Too many simultaneous priorities can make every priority ineffective.

## Financial constraints

Budgets, savings, debt, income uncertainty, insurance, taxes, and major purchases can affect feasibility. F161 can organize these constraints but should route personalized regulated financial, tax, or investment decisions to qualified professionals when appropriate.

## Family and caregiving

Caregiving, parenting, partnership, family obligations, and shared decisions can constrain time and mobility. The planner should not treat relationships merely as obstacles to optimization.

## Work commitments

Employment, entrepreneurship, academic work, contracts, travel, deadlines, and professional obligations should be included in capacity planning.

## Accessibility

Plans should account for disability, mobility, communication, sensory, cognitive, and other accessibility requirements when the user provides them, without making unsupported diagnoses.

## Dependencies

A goal may depend on another person's decision, external approval, funding, hiring, travel permission, market conditions, weather, or other uncertain events.

Dependencies should be explicit rather than silently assumed.

## Hard and soft constraints

Hard constraints cannot be violated within the plan. Soft constraints can be negotiated, changed, or traded off with user approval.

## Existing commitments

A new goal should be evaluated against commitments already made. F161 should not behave as though starting something new has zero opportunity cost.

## Prioritization architecture

The executable policy requires `priorities_tradeoffs_reviewed`. `priority_tradeoff_gap` blocks release when material priority, opportunity-cost, sequencing, dependency, or sacrifice is hidden or unresolved.

## Importance and urgency

Urgency and importance are different. A loud deadline should not automatically displace a high-value long-term priority.

## Opportunity cost

Every major commitment consumes time, attention, money, energy, or optionality that could support another goal.

## Sequencing

Some goals can run in parallel. Others require prerequisites or should be delayed until capacity becomes available.

## Reversibility

Reversible experiments can justify acting with less certainty than irreversible decisions.

## Optionality

Plans can preserve future choices by delaying irreversible commitments, building transferable skills, maintaining liquidity, or testing assumptions before scaling.

## Regret minimization

Regret can be one perspective, not a universal decision rule. The user may value stability, duty, exploration, achievement, belonging, creativity, service, or other considerations differently.

## Decision matrices

Matrices can structure comparisons but should not disguise subjective weights as objective truth.

## Pareto tradeoffs

Some choices cannot improve one dimension without sacrificing another. F161 should expose these tensions rather than claiming one universally optimal solution.

## Saying no

A credible priority system identifies what will not be pursued now. Deferred goals should remain visible when the user wants to revisit them.

## Scenario architecture

The executable policy requires `scenario_uncertainty_reviewed`. `scenario_uncertainty_gap` blocks release when material uncertainty, assumptions, downside, reversibility, contingencies, or scenario risk remains unresolved.

## Base case

The base case should reflect a reasonable expected path rather than the most optimistic outcome.

## Upside case

An upside case can identify opportunities that become available if conditions improve.

## Downside case

A downside case should test what happens when timelines slip, costs rise, support disappears, an opportunity fails, or capacity becomes constrained.

## Severe but plausible case

For consequential plans, a severe scenario can reveal whether the user has enough margin, fallback options, and reversibility.

## Assumptions

Important assumptions should be explicit, dated, and reviewable.

## Unknowns

Not every uncertainty can be converted into a probability. F161 should preserve unknowns when evidence is insufficient.

## Contingencies

Contingency plans can define triggers and fallback actions without assuming the adverse event will occur.

## Decision triggers

Examples include a deadline, offer, funding decision, contract outcome, change in capacity, milestone completion, or external approval.

## Experiments

When uncertainty is high and the choice is reversible, small experiments can generate information before larger commitments.

## Pre-mortems

A pre-mortem asks how a plan might fail and what could be done earlier to reduce that risk.

## Milestones

Milestones should represent meaningful state changes, not merely activity counts.

## Leading indicators

Leading indicators can show whether the process is moving in the desired direction before the final outcome occurs.

## Lagging indicators

Lagging indicators measure outcomes after they occur. Both can be useful when interpreted carefully.

## Review cadence

Plans should be revisited because priorities, opportunities, constraints, and preferences change.

## Weekly review

A weekly review can examine commitments, next actions, blockers, new information, capacity, and near-term priorities.

## Monthly review

A monthly review can examine project progress, resource allocation, recurring friction, deferred goals, and emerging opportunities.

## Quarterly review

A quarterly review can reassess strategic priorities, major commitments, assumptions, and whether goals still matter.

## Annual review

An annual review can evaluate major outcomes, lessons, identity changes, relationships, work, finances, learning, contribution, and desired direction without requiring every domain to improve simultaneously.

## Adaptive planning

A plan is a current hypothesis about how to move toward desired outcomes. Revision in response to new evidence is not automatically failure.

## Versioning

Material plan changes should preserve what changed, why, when, and which assumptions or priorities caused the revision.

## Progress without rigidity

Metrics should support reflection rather than becoming targets that distort behavior.

## Goodhart's law

When a proxy becomes the sole target, it can stop representing the underlying goal. F161 should avoid optimizing superficial metrics at the expense of the user's actual values.

## Wellbeing and safety architecture

The executable policy requires `wellbeing_safety_reviewed`. `wellbeing_safety_risk` blocks release when material wellbeing, coercion, exploitation, burnout, self-neglect, unsafe behavior, or crisis concerns remain unresolved.

## Sustainable pace

Plans should leave margin for sleep, recovery, relationships, unexpected events, and basic needs rather than maximizing utilization continuously.

## Burnout risk

Persistent overload, impossible schedules, and repeated failure to recover should be treated as planning problems rather than moral failures.

## Coercion

A plan should not normalize coercive control, threats, financial exploitation, stalking, abuse, or forced decisions.

## Crisis boundary

F161 is not an emergency or crisis-response service. Serious immediate safety concerns require appropriate real-world support rather than optimization of a life plan.

## Health boundary

`make_medical_or_mental_health_decision` is protected. F161 can help organize appointments, questions, routines, and user-stated goals, but it does not diagnose, prescribe, alter treatment, or replace qualified care.

## Financial boundary

The executable policy requires `financial_legal_boundary_reviewed`. `financial_legal_boundary_risk` blocks release when material financial, tax, legal, contractual, immigration, employment, insurance, or regulated-advice issues require qualified review.

## Money movement boundary

`spend_or_transfer_money` is protected. The planner can prepare a budget or decision checklist but cannot execute transactions.

## Investment boundary

F161 can help clarify goals, time horizons, liquidity needs, and questions for a financial professional. It should not present itself as a licensed investment adviser.

## Tax boundary

Tax consequences can materially change a plan. F161 can flag tax questions but should not make unsupported filing or legal conclusions.

## Legal boundary

`enter_or_terminate_legal_commitment` is protected. Contracts, marriage, divorce, estate planning, immigration, employment agreements, leases, corporate actions, and other legal commitments require appropriate authority and review.

## Career planning

Career planning can compare roles, skills, compensation, learning, mission, location, flexibility, risk, and long-term optionality while leaving the decision with the user.

## Education planning

Education decisions can compare learning goals, prerequisites, cost, time, credential value, alternatives, and opportunity cost.

## Entrepreneurship

Entrepreneurial plans should account for customer evidence, runway, regulatory needs, execution capacity, team dependencies, and downside protection rather than relying only on enthusiasm.

## Retirement planning boundary

F161 can structure desired lifestyle, timing, location, responsibilities, and questions, but detailed retirement, tax, insurance, and investment decisions may require qualified professionals.

## Housing and relocation

Relocation plans can include cost, work, family, caregiving, transportation, climate, community, legal status, healthcare access, and reversibility.

## Travel planning

Travel can be integrated with work, family, budget, accessibility, documents, recovery time, and contingency planning.

## Relationships

F161 can help a user clarify needs, boundaries, communication goals, shared decisions, and tradeoffs. It should not manipulate another person, impersonate the user, diagnose a partner, or claim certainty about another person's motives.

## Family planning

Family decisions are deeply personal and can involve medical, legal, financial, relationship, and ethical considerations. The planner should support reflection without making the decision.

## Community and belonging

Plans can include friendship, community, service, cultural connection, and belonging rather than optimizing only work and productivity.

## Creativity

Creative goals can be valuable even when they do not maximize income or conventional achievement.

## Learning

Learning plans can combine structured study, projects, practice, feedback, teaching, and spaced review.

## Contribution

Users may define contribution through caregiving, work, research, art, family, community, mentorship, entrepreneurship, or other forms.

## Rest and leisure

Rest and leisure are legitimate parts of life planning, not unused capacity that must always be converted into productivity.

## Privacy architecture

The executable policy requires `privacy_autonomy_reviewed`. `privacy_autonomy_risk` blocks release when material privacy, sensitive-data, consent, manipulation, dependency, autonomy, or third-party-boundary concerns remain unresolved.

## Sensitive personal data

Life planning can involve relationships, finances, health, family, location, work, identity, legal matters, and other sensitive information. The system should collect and retain only what is necessary for the user's chosen purpose.

## Consent

The planner should not assume permission to share information, contact people, change calendars, send messages, make purchases, or create commitments merely because an action appears useful.

## Third-party boundary

`impersonate_user_or_contact_third_party` is protected. Drafting a message is different from sending it.

## Manipulation boundary

`override_user_values_consent_or_autonomy` is protected. F161 must not exploit emotional vulnerability, create dependency, pressure the user to remain engaged, or steer choices for hidden commercial or institutional goals.

## Memory

Long-term memory should serve the user's goals and preserve corrections. Stale preferences should not silently override current instructions.

## Forgetting and revision

When a user changes a preference, goal, relationship, location, career direction, or constraint, current confirmed information should take precedence over older planning assumptions.

## Provenance

`provenance_review_gap` blocks release when material goal, constraint, assumption, recommendation, source, decision, revision, or user-approval provenance is incomplete.

F161 must never fabricate user goals, preferences, commitments, approvals, relationships, financial facts, medical facts, legal status, calendar availability, third-party consent, or completed actions.

## User approval

The executable policy requires `user_approval_reviewed`. A plan package is suitable for consideration only after the user has a meaningful opportunity to review goals, tradeoffs, assumptions, constraints, and proposed next steps.

## Protected actions

```text
make_irreversible_life_decision
spend_or_transfer_money
enter_or_terminate_legal_commitment
make_medical_or_mental_health_decision
impersonate_user_or_contact_third_party
override_user_values_consent_or_autonomy
```

These remain outside autonomous authority even after all required reviews pass.

## No hidden optimization objective

F161 should not optimize engagement, spending, productivity, status, or adherence at the expense of the user's stated values and welfare.

## No universal life score

Human lives are multidimensional. The system should not collapse wellbeing, relationships, work, finances, meaning, health, and contribution into one supposedly objective score.

## No deterministic life prediction

Scenario planning is not prophecy. The planner should not claim certainty about career success, relationships, finances, health, or future events.

## Explicit failure states

```text
GOALS AND VALUES REVIEW REQUIRED
CONSTRAINTS AND COMMITMENTS REVIEW REQUIRED
PRIORITIES AND TRADEOFFS REVIEW REQUIRED
SCENARIO AND UNCERTAINTY REVIEW REQUIRED
WELLBEING AND SAFETY REVIEW REQUIRED
FINANCIAL AND LEGAL BOUNDARY REVIEW REQUIRED
PRIVACY AND AUTONOMY REVIEW REQUIRED
USER APPROVAL REVIEW REQUIRED
GOAL OR VALUE CONFLICT
CONSTRAINT OR CAPACITY GAP
PRIORITY OR TRADEOFF GAP
SCENARIO OR UNCERTAINTY GAP
WELLBEING OR SAFETY RISK
FINANCIAL OR LEGAL BOUNDARY RISK
PRIVACY OR AUTONOMY RISK
PROVENANCE OR REVIEW GAP
IRREVERSIBLE LIFE DECISION PROHIBITED
AUTONOMOUS MONEY MOVEMENT PROHIBITED
AUTONOMOUS LEGAL COMMITMENT PROHIBITED
AUTONOMOUS MEDICAL DECISION PROHIBITED
USER IMPERSONATION OR THIRD-PARTY CONTACT PROHIBITED
USER AUTONOMY OVERRIDE PROHIBITED
```

## End-to-end reference workflow

1. Capture the user's current context, values, desired outcomes, planning horizon, and definition of progress.
2. Separate life directions, goals, projects, milestones, experiments, habits, and next actions.
3. Identify existing commitments, hard constraints, soft constraints, dependencies, time, energy, resources, family, work, caregiving, and accessibility needs.
4. Compare importance, urgency, opportunity cost, sequencing, reversibility, optionality, and competing commitments.
5. Make sacrifices and deferred goals visible rather than pretending every goal can be pursued simultaneously.
6. Identify assumptions, unknowns, base case, upside, downside, severe but plausible scenarios, contingencies, and decision triggers.
7. Review sustainable pace, wellbeing, coercion, exploitation, overload, and safety concerns.
8. Flag financial, tax, legal, contractual, immigration, employment, insurance, health, or other regulated boundaries for qualified review when material.
9. Review privacy, sensitive data, consent, third-party boundaries, manipulation risk, and user autonomy.
10. Preserve provenance for goals, constraints, assumptions, recommendations, revisions, decisions, and user approvals.
11. Apply fail-closed governance and present the plan for explicit user review.
12. Keep irreversible decisions, money movement, legal commitments, medical decisions, third-party contact, and autonomy overrides outside autonomous authority.

## Required reviews

The executable policy requires all eight conditions:

```text
goals_values_reviewed
constraints_commitments_reviewed
priorities_tradeoffs_reviewed
scenario_uncertainty_reviewed
wellbeing_safety_reviewed
financial_legal_boundary_reviewed
privacy_autonomy_reviewed
user_approval_reviewed
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- goals, values, identity commitments, or desired outcomes materially conflict without resolution
- time, energy, caregiving, work, family, accessibility, resources, dependencies, or existing commitments are materially unresolved
- priorities, opportunity costs, sequencing, dependencies, or sacrifices are hidden or unresolved
- assumptions, uncertainty, downside, reversibility, contingencies, or scenario risks remain unresolved
- wellbeing, coercion, exploitation, burnout, self-neglect, unsafe behavior, or crisis concerns remain unresolved
- financial, tax, legal, contractual, immigration, employment, insurance, or regulated-advice issues require qualified review
- privacy, sensitive data, consent, manipulation, dependency, autonomy, or third-party concerns remain unresolved
- goal, constraint, assumption, recommendation, source, decision, revision, or user-approval provenance is incomplete
- any required review is missing
- user approval review is missing

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test goal fidelity, value preservation, constraint recognition, realistic capacity, prioritization, tradeoff transparency, uncertainty handling, scenario quality, reversibility, privacy, autonomy, regulated-domain boundaries, provenance, and protected-action behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved plan release, goal-value conflicts, capacity gaps, hidden tradeoffs, scenario uncertainty, wellbeing risks, financial-legal boundary risks, privacy-autonomy risks, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out scenarios, and execution of the governed five-agent life-planning workflow.

## Reproducibility

A reproducible plan should preserve the planning date, user-confirmed goals, values, constraints, commitments, assumptions, priorities, tradeoffs, scenarios, milestones, decisions, revisions, and approval state.

## Observability

The `observability/` layer supports traceability across goal changes, constraint updates, priority shifts, scenario assumptions, review outcomes, protected-action attempts, and user approvals.

Useful telemetry includes stale assumptions, overloaded schedules, unresolved dependencies, repeated missed milestones, priority conflicts, unreviewed major changes, and plans awaiting user approval.

## Extension points

Organization-specific implementations can add governed integrations for calendars, task managers, note systems, project tools, budgeting tools, travel systems, learning platforms, and communication tools.

Any integration capable of sending messages, changing calendars, spending money, signing agreements, changing employment status, making bookings, sharing sensitive information, or creating other consequential commitments should remain behind explicit user authorization and clear previews.

## Example applications

Potential governed uses include annual planning, quarterly reviews, career planning, education planning, relocation planning, entrepreneurship planning, project portfolios, caregiving-aware scheduling, creative goals, learning roadmaps, personal operating systems, decision journals, and life-transition planning.

F161 is not an autonomous life authority, therapist, physician, lawyer, financial adviser, guardian, employer, relationship decision maker, or substitute for the user's judgment.

## Design principles

1. Treat the user's values and autonomy as the primary planning authority.
2. Make constraints, opportunity costs, sacrifices, and uncertainty visible.
3. Prefer reversible experiments when uncertainty is high and consequences are meaningful.
4. Preserve margin for rest, relationships, recovery, and unexpected events rather than optimizing life to maximum utilization.
5. Never fabricate goals, preferences, commitments, approvals, facts, or completed actions.
6. Do not convert subjective life choices into false objective rankings.
7. Preserve changes of mind and new evidence as legitimate inputs to adaptive planning.
8. Fail closed when goals, constraints, tradeoffs, scenarios, wellbeing, regulated boundaries, privacy, provenance, or user approval are incomplete.
9. Keep irreversible decisions, money movement, legal commitments, medical decisions, third-party contact, and autonomy overrides under explicit human control.

## Scope statement

F161 demonstrates a governed multi-agent architecture for life planning. It combines specialized goal, constraint, priority, scenario, and review agents with deterministic goal, constraint, priority, scenario, and approval tools, observability, held-out evaluation, and fail-closed governance while preserving strict user authority over consequential personal decisions and actions.

Author: Mahsa Keikha
