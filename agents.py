"""
======================================================================
FILE: agents.py

PROJECT:
Agentic AI-Based Project Health and Risk Monitoring System
for Automated Project Governance

DESCRIPTION:
This file contains all AI agents used within the system.

The system follows a Multi-Agent Architecture where each agent
performs a specific responsibility:

1. Project Health Agent
   - Evaluates overall project health
   - Determines Green / Amber / Red status

2. Risk Analysis Agent
   - Identifies project risks
   - Analyzes risk severity and impact

3. Recommendation Agent
   - Generates mitigation strategies
   - Suggests corrective actions

4. Reporting Agent
   - Creates management-level summaries
   - Supports governance reporting

This architecture improves modularity, maintainability,
and scalability.
======================================================================
"""

# ==============================================================
# IMPORT LIBRARIES
# ==============================================================

import ollama

# ==============================================================
# MODEL CONFIGURATION
# ==============================================================

MODEL = "llama3"

# ==============================================================
# GENERIC AGENT EXECUTION FUNCTION
# ==============================================================

def call_agent(
        system_role: str,
        project_data: str) -> str:
    """
    Executes an AI agent using the provided role and project data.

    Parameters
    ----------
    system_role : str
        Defines the behavior of the agent.

    project_data : str
        Project information extracted from Excel.

    Returns
    -------
    str
        Generated AI response.
    """

    try:

        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_role
                },
                {
                    "role": "user",
                    "content": project_data
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"""
ERROR:
Unable to process project information.

Reason:
{str(e)}

Possible Solutions:
- Verify Ollama is installed correctly.
- Verify Ollama service is running.
- Verify the Llama3 model has been downloaded.
- Run: ollama list
- Run: ollama pull llama3
- Restart Streamlit after installing the model.
"""


# ==============================================================
# PROJECT HEALTH AGENT
# ==============================================================

def project_health_agent(
        project_data: str) -> str:
    """
    Determines overall project health.

    Responsibilities:
    - Analyze project progress
    - Evaluate delayed activities
    - Assess milestone status
    - Classify project health

    Output:
    - Green
    - Amber
    - Red
    """

    system_role = """

You are a Project Health Assessment Agent.

Analyze the project data and determine project health.

Project Health Criteria:

Green:
- No delayed tasks
- Project progressing according to plan
- No critical risks

Amber:
- One to three delayed tasks
- Moderate project risk
- Corrective actions may be required

Red:
- More than three delayed tasks
- Critical project risks identified
- Major milestones may be impacted

Provide:

1. Project Health Status
2. Reasoning
3. Supporting Observations
4. Key Concerns
5. Confidence Level

Use professional project management terminology.

"""

    return call_agent(
        system_role,
        project_data
    )


# ==============================================================
# RISK ANALYSIS AGENT
# ==============================================================

def risk_analysis_agent(
        project_data: str) -> str:
    """
    Identifies and evaluates project risks.

    Risk Categories:
    - Schedule Risks
    - Resource Risks
    - Operational Risks
    - Dependency Risks
    """

    system_role = """

You are a Risk Analysis Agent.

Analyze the project data.

Identify:

1. Schedule Risks
2. Resource Risks
3. Operational Risks
4. Dependency Risks

For every risk provide:

- Risk Description
- Severity
- Potential Impact
- Likelihood
- Recommended Mitigation

Use the following severity scale:

Low
Medium
High

Structure the response professionally.

"""

    return call_agent(
        system_role,
        project_data
    )


# ==============================================================
# RECOMMENDATION AGENT
# ==============================================================

def recommendation_agent(
        project_data: str) -> str:
    """
    Generates actionable recommendations.

    Focus Areas:
    - Risk mitigation
    - Project recovery
    - Resource optimization
    - Governance improvements
    """

    system_role = """

You are a Project Recommendation Agent.

Analyze the project information and generate:

1. Corrective Actions
2. Risk Mitigation Strategies
3. Governance Improvements
4. Resource Recommendations
5. Escalation Recommendations

Recommendations should be:

- Practical
- Actionable
- Prioritized
- Cost-effective
- Easy to implement

If critical risks exist, recommend escalation actions.

Provide recommendations in priority order.

"""

    return call_agent(
        system_role,
        project_data
    )


# ==============================================================
# REPORTING AGENT
# ==============================================================

def reporting_agent(
        project_data: str) -> str:
    """
    Generates executive-level summaries.

    Intended Audience:
    - Project Managers
    - Team Leads
    - Stakeholders
    - Senior Management
    """

    system_role = """

You are an Executive Reporting Agent.

Create a concise executive summary.

Include:

1. Overall Project Status
2. Key Risks
3. Impact Analysis
4. Important Recommendations
5. Immediate Actions Required

The report should be suitable for:

- Project Managers
- Team Leads
- Stakeholders
- Senior Management

Keep the report:

- Professional
- Concise
- Governance-focused
- Action-oriented

Limit the executive summary to a management-friendly format.

"""

    return call_agent(
        system_role,
        project_data
    )


# ==============================================================
# PROJECT GOVERNANCE AGENT
# ==============================================================

def governance_agent(
        project_data: str) -> str:
    """
    Additional governance-focused agent.

    Purpose:
    - Evaluate governance compliance
    - Identify accountability gaps
    - Recommend governance improvements
    """

    system_role = """

You are a Project Governance Agent.

Analyze project governance maturity.

Evaluate:

1. Accountability
2. Communication Effectiveness
3. Monitoring Mechanisms
4. Escalation Readiness
5. Governance Compliance

Provide:

- Strengths
- Weaknesses
- Governance Risks
- Improvement Opportunities

"""

    return call_agent(
        system_role,
        project_data
    )


# ==============================================================
# FUTURE AGENTS
# ==============================================================

"""
Future Scope:

1. Portfolio Management Agent
   - Monitor multiple projects

2. Predictive Risk Agent
   - Forecast delays using AI

3. Resource Optimization Agent
   - Suggest resource allocation

4. Stakeholder Communication Agent
   - Generate automatic email reports

5. Power BI Insight Agent
   - Generate project analytics

6. Root Cause Analysis Agent
   - Identify causes of delays

7. Project Recovery Agent
   - Generate project recovery plans

These agents can be integrated seamlessly due to the
modular architecture used in this implementation.
"""