"""
======================================================================
PROJECT TITLE
======================================================================

Agentic AI-Based Project Health and Risk Monitoring System
for Automated Project Governance

Author:
Noel Jacob Biju

======================================================================
PROJECT EVOLUTION AND IMPLEMENTATION JUSTIFICATION
======================================================================

Initial Approach:
-----------------
The project was initially designed using Microsoft Copilot Studio,
Power Automate, Microsoft Planner/Excel, Microsoft Teams,
and Microsoft Outlook.

The objective was to develop an AI-powered Project Health Agent
capable of:

1. Monitoring project activities
2. Assessing project health
3. Identifying project risks
4. Generating recommendations
5. Automating stakeholder communication

Challenges Encountered:
-----------------------
During implementation, the Copilot Studio Agent was successfully
configured with project governance rules, risk assessment logic,
and stakeholder communication workflows.

However, the final deployment relied on the "Execute Agent and Wait"
action in Power Automate, which required strict JSON-based
responses from the agent.

An environment-level publishing/licensing constraint prevented
the updated agent configuration from being published and deployed.
As a result, the latest agent version could not be fully validated
through the end-to-end workflow.

Enhanced Solution:
------------------
To ensure successful project completion and demonstrate the
intended functionality, the architecture was redesigned using
Python, Streamlit, and AI-powered agents.

The new implementation provides:

• Project Health Assessment Agent
• Risk Analysis Agent
• Recommendation Generation Agent
• Executive Reporting Agent
• Project Governance Agent
• Automated Email Notification Module

Benefits of the New Approach:
-----------------------------
1. Independent of platform publishing restrictions
2. Fully customizable and extensible
3. Easier testing and validation
4. Supports future integration with:
   - Azure OpenAI
   - Jira
   - Azure DevOps
   - Power BI
5. Enables complete demonstration of project functionality

Conclusion:
-----------
The transition from Copilot Studio to Python-based Agentic AI
was a strategic engineering decision made to overcome deployment
constraints while preserving the project's objectives,
functionality, and innovation.

======================================================================
"""

# ==============================================================
# IMPORT LIBRARIES
# ==============================================================

import streamlit as st
import pandas as pd

from agents import (
    project_health_agent,
    risk_analysis_agent,
    recommendation_agent,
    reporting_agent,
    governance_agent
)

import smtplib

from pathlib import Path

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

# ==============================================================
# EMAIL FUNCTION
# Sends generated reports through Gmail SMTP.
# ==============================================================

def send_email(
        sender_email,
        app_password,
        receiver_email,
        report_content):

    try:

        message = MIMEMultipart()

        message["From"] = sender_email

        message["To"] = receiver_email

        message["Subject"] = (
            "Project Health Monitoring Report"
        )

        message.attach(
            MIMEText(
                report_content,
                "plain"
            )
        )

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            sender_email,
            app_password
        )

        result = server.send_message(
    message
)

        print("SMTP Result:", result)
        server.quit()

        return True

    except Exception as e:

        return str(e)
    
# ==============================================================
# PAGE CONFIGURATION
# ==============================================================

st.set_page_config(
    page_title="Agentic AI Project Governance",
    page_icon="📊",
    layout="wide"
)

# ==============================================================
# HEADER SECTION
# ==============================================================

st.title(
    "📊 Agentic AI-Based Project Health and Risk Monitoring System"
)

st.markdown("""
### Automated Project Governance Dashboard

This system automates:

✅ Project Monitoring

✅ Project Health Assessment

✅ Risk Identification

✅ Recommendation Generation

✅ Executive Reporting

✅ Governance Assessment

✅ Automated Email Distribution

✅ Decision Support
""")

# ==============================================================
# SIDEBAR
# ==============================================================

st.sidebar.header("Project Data Upload")

uploaded_file = st.sidebar.file_uploader(
    "Upload Project Tracker",
    type=["xlsx"]
)

# ======================================================
# EMAIL CONFIGURATION
# Allows generated reports to be sent
# to project stakeholders via Gmail.
# ======================================================

st.sidebar.header("📧 Email Configuration")

sender_email = st.sidebar.text_input(
    "Sender Gmail"
)

gmail_app_password = st.sidebar.text_input(
    "Gmail App Password",
    type="password"
)

receiver_email = st.sidebar.text_input(
    "Recipient Email"
)

# ======================================================
# ADD NEW PROJECT TASK
# Allows users to insert new project records
# directly from the dashboard.
# ======================================================

st.sidebar.header("➕ Add New Task")

project_name = st.sidebar.text_input(
    "Project Name",
    placeholder="Customer Portal"
)

task_name = st.sidebar.text_input(
    "Task Name",
    placeholder="Deployment"
)

owner = st.sidebar.text_input(
    "Owner",
    placeholder="John"
)

status = st.sidebar.selectbox(
    "Status",
    [
        "Not Started",
        "In Progress",
        "Completed",
        "Delayed",
        "Blocked"
    ]
)

priority = st.sidebar.selectbox(
    "Priority",
    [
        "High",
        "Medium",
        "Low"
    ]
)

due_date = st.sidebar.date_input(
    "Due Date"
)

# ======================================================
# ADD RECORD TO EXCEL
# ==============================================================

if st.sidebar.button("Add Record"):

    if (
        project_name.strip() == ""
        or task_name.strip() == ""
        or owner.strip() == ""
    ):

        st.sidebar.warning(
            "Please fill all mandatory fields."
        )

    else:

        try:

            file_path = "project_data.xlsx"

            if Path(file_path).exists():

                existing_df = pd.read_excel(
                file_path
            )

            else:

                existing_df = pd.DataFrame(
                    columns=[
                    "ProjectName",
                    "TaskName",
                    "Owner",
                    "Status",
                    "Priority",
                    "DueDate"
                    ]
                )

                new_record = {
                    "ProjectName": project_name,
                    "TaskName": task_name,
                    "Owner": owner,
                    "Status": status,
                    "Priority": priority,
                    "DueDate": due_date.strftime(
                        "%d-%b-%y"
                    )
                }

            updated_df = pd.concat(
                [
                    existing_df,
                    pd.DataFrame([new_record])
                ],
                ignore_index=True
            )

            updated_df.to_excel(
                file_path,
                index=False
            )

            st.sidebar.success(
                "✅ Record added successfully!"
            )

            st.rerun()

        except Exception as e:

            st.sidebar.error(
                f"Unable to add record: {e}"
            )

# ==============================================================
# MAIN APPLICATION
# ==============================================================

if uploaded_file:

    try:

        # ======================================================
        # LOAD DATA
        # ==============================================================

        df = pd.read_excel(uploaded_file)

        # ======================================================
        # COLUMN VALIDATION
        # ==============================================================

        required_columns = [
            "ProjectName",
            "TaskName",
            "Owner",
            "Status",
            "Priority",
            "DueDate"
        ]

        df.columns = df.columns.str.strip()

        missing_columns = [
            col
            for col in required_columns
            if col not in df.columns
        ]

        if missing_columns:

            st.error(
                f"Missing columns detected: {missing_columns}"
            )

            st.stop()

        st.header("📁 Project Dataset")

        st.dataframe(
            df,
            use_container_width=True
        )

        # ======================================================
        # DATA PREPARATION
        # Converts project information into a structured
        # format for Multi-Agent AI analysis.
        # ==============================================================

        completed_count = len(
            df[
                df["Status"]
                .astype(str)
                .str.lower()
                .str.contains("completed")
            ]
        )

        delayed_count = len(
            df[
                df["Status"]
                .astype(str)
                .str.lower()
                .str.contains("delayed")
            ]
        )

        blocked_count = len(
            df[
                df["Status"]
                .astype(str)
                .str.lower()
                .str.contains("blocked")
            ]
        )

        project_data = f"""

PROJECT HEALTH MONITORING DATASET

Project Information:

{df.to_string(index=False)}

Summary Metrics:

Total Tasks: {len(df)}

Completed Tasks: {completed_count}

Delayed Tasks: {delayed_count}

Blocked Tasks: {blocked_count}

Please analyze this project from a governance,
risk management, and project delivery perspective.

"""

        # ======================================================
        # PROJECT METRICS
        # ==============================================================

        st.header("📈 Project Metrics")

        total_tasks = len(df)

        # ======================================================
        # TASK STATUS ANALYSIS
        # ==============================================================

        completed_tasks = completed_count

        delayed_tasks = delayed_count

        blocked_tasks = blocked_count

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Tasks",
            total_tasks
        )

        col2.metric(
            "Completed Tasks",
            completed_tasks
        )

        col3.metric(
            "Delayed Tasks",
            delayed_tasks
        )

        col4.metric(
            "Blocked Tasks",
            blocked_tasks
        )

        # ======================================================
        # ANALYSIS BUTTON
        # ==============================================================

        st.header("🤖 Multi-Agent AI Analysis")

        analyze = st.button(
            "Analyze Project",
            type="primary"
        )

        if analyze:

            # ==================================================
            # PROJECT HEALTH AGENT
            # ==================================================

            with st.spinner(
                "Running Project Health Agent..."
            ):

                project_health = (
                    project_health_agent(
                        project_data
                    )
                )

            # ==================================================
            # RISK ANALYSIS AGENT
            # ==================================================

            with st.spinner(
                "Running Risk Analysis Agent..."
            ):

                risk_analysis = (
                    risk_analysis_agent(
                        project_data
                    )
                )

            # ==================================================
            # RECOMMENDATION AGENT
            # ==================================================

            with st.spinner(
                "Running Recommendation Agent..."
            ):

                recommendations = (
                    recommendation_agent(
                        project_data
                    )
                )

            # ==================================================
            # REPORTING AGENT
            # ==================================================

            with st.spinner(
                "Generating Executive Summary..."
            ):

                executive_summary = (
                    reporting_agent(
                        project_data
                    )
                )

            # ==================================================
            # GOVERNANCE AGENT
            # ==================================================

            with st.spinner(
                "Running Governance Assessment Agent..."
            ):

                governance_report = (
                    governance_agent(
                        project_data
                    )
                )

            # ==================================================
            # RESULTS SECTION
            # ==============================================================

            st.divider()

            st.subheader(
                "🟢 Project Health Assessment"
            )

            st.write(project_health)

            st.subheader(
                "⚠️ Risk Analysis"
            )

            st.write(risk_analysis)

            st.subheader(
                "✅ Recommendations"
            )

            st.write(recommendations)

            st.subheader(
                "📄 Executive Summary"
            )

            st.write(executive_summary)

            st.subheader(
                "🏛️ Project Governance Assessment"
            )

            st.write(governance_report)

            # ==================================================
            # DOWNLOADABLE REPORT & EMAIL DISTRIBUTION
            # Generates reports and supports automated
            # stakeholder communication.
            # ==================================================

            report = f"""
====================================================
PROJECT HEALTH REPORT
====================================================

PROJECT HEALTH ASSESSMENT

{project_health}

----------------------------------------------------

RISK ANALYSIS

{risk_analysis}

----------------------------------------------------

RECOMMENDATIONS

{recommendations}

----------------------------------------------------

EXECUTIVE SUMMARY

{executive_summary}

----------------------------------------------------

PROJECT GOVERNANCE ASSESSMENT

{governance_report}

====================================================
END OF REPORT
====================================================
"""

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="Project_Health_Report.txt",
                mime="text/plain"
            )

            # ==================================================
            # EMAIL REPORT
            # Sends generated reports to stakeholders.
            # ==============================================================

            if st.button(
                "📧 Send Report"
            ):

                if (
                    sender_email.strip() == ""
                    or gmail_app_password.strip() == ""
                    or receiver_email.strip() == ""
                ):

                    st.warning(
                        "Please enter email details."
                    )

                else:

                    result = send_email(
                        sender_email,
                        gmail_app_password,
                        receiver_email,
                        report
                    )

                    if result is True:

                        st.success(
                            "✅ Report sent successfully!"
                        )

                    else:

                        st.error(
                            f"Email delivery failed: {result}"
                        )
                        

    except Exception as e:
                    st.error(
                        f"Error processing file: {e}"
                    )

# ==============================================================
# NO FILE UPLOADED
# ==============================================================

else:

    st.info(
        "Please upload a Project Tracker Excel file to begin analysis."
    )

# ==============================================================
# FOOTER
# ==============================================================

st.markdown("---")

st.markdown(
    "Developed as part of the project: "
    "**Agentic AI-Based Project Health and Risk Monitoring System "
    "for Automated Project Governance**"
)