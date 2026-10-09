# 🚀 Agentic AI-Based Project Health and Risk Monitoring System for Automated Project Governance

## 📌 Overview

The **Agentic AI-Based Project Health and Risk Monitoring System** is an intelligent project governance solution designed to automate project health assessment, risk identification, recommendation generation, governance evaluation, executive reporting, and stakeholder communication.

The system leverages a **Multi-Agent AI Architecture** powered by **Python, Streamlit, Ollama, and Llama 3** to analyze project data from Excel-based project trackers and generate actionable insights. Each AI agent performs a specialized task and collaboratively supports effective project governance and decision-making.

By integrating AI-driven analysis with automation, the system improves project visibility, reduces manual monitoring effort, and enables proactive project management.

---

## 🎯 Aim

To develop an Agentic AI-based multi-agent system that automates project health assessment, risk analysis, governance evaluation, report generation, and stakeholder communication for effective project governance.

---

## 🎯 Objectives

- Assess project health through intelligent data-driven analysis.
- Identify and evaluate potential project risks.
- Generate recommendations to support informed decision-making.
- Facilitate governance assessment and performance monitoring.
- Enable automated reporting and stakeholder communication.

---

## 🏗️ System Architecture

```text
📊 Excel Project Tracker
            │
            ▼
🖥️ Streamlit Dashboard
            │
            ▼
📈 Data Validation & Processing
            │
            ▼
🟢 Project Health Agent
            │
            ▼
⚠️ Risk Analysis Agent
            │
            ▼
💡 Recommendation Agent
            │
            ▼
📄 Reporting Agent
            │
            ▼
🏛️ Governance Agent
            │
            ▼
📋 Project Health Report
            │
      ┌─────┴─────┐
      ▼           ▼
📥 Download   📧 Email Report
```

---

## 🤖 Multi-Agent Architecture

### 🟢 Project Health Agent

- Evaluates project health and performance.
- Determines Green, Amber, or Red status.
- Identifies key project concerns.

### ⚠️ Risk Analysis Agent

- Identifies project risks.
- Assesses impact and severity.
- Highlights critical risk areas.

### 💡 Recommendation Agent

- Generates corrective actions.
- Suggests risk mitigation strategies.
- Recommends governance improvements.

### 📄 Reporting Agent

- Generates executive summaries.
- Creates management-friendly reports.
- Supports stakeholder decision-making.

### 🏛️ Governance Agent

- Evaluates governance effectiveness.
- Assesses accountability and monitoring.
- Identifies governance improvement opportunities.

---

## 🔄 Workflow

1. Upload project data through an Excel-based project tracker.
2. Validate and process project information.
3. Calculate project metrics and performance indicators.
4. Execute multi-agent AI analysis.
5. Assess project health and identify risks.
6. Generate recommendations and governance insights.
7. Create executive reports automatically.
8. Download reports or distribute them through email.

---

## 🧩 Project Modules

### 📂 Project Data Management Module

Collects, validates, and manages project data.

### 🟢 Project Health Assessment Module

Evaluates project health and overall progress.

### ⚠️ Risk Analysis Module

Identifies and evaluates project risks.

### 💡 Recommendation Generation Module

Provides mitigation strategies and corrective actions.

### 📄 Executive Reporting Module

Generates stakeholder-ready reports and summaries.

### 🏛️ Governance Assessment Module

Evaluates governance effectiveness and compliance.

### 📧 Automated Report Distribution Module

Distributes generated reports through email.

### 🖥️ Dashboard and Visualization Module

Displays project metrics and analysis results through an interactive dashboard.

---

## 📊 Project Health Rules

| Status | Criteria |
|----------|----------|
| 🟢 Green | No delayed tasks |
| 🟡 Amber | 1–3 delayed tasks |
| 🔴 Red | More than 3 delayed tasks |

---

## 🛠️ Technology Stack

### 🎨 Frontend

- Streamlit

### ⚙️ Backend

- Python

### 🧠 AI Framework

- Ollama

### 🤖 Large Language Model

- Llama 3

### 📊 Data Processing

- Pandas

### 📂 Data Storage

- Excel (.xlsx)

### 📧 Communication

- Gmail SMTP

---

## ⚙️ Approach

The solution adopts a **Multi-Agent AI Architecture** where specialized AI agents collaborate to analyze project data, assess project health, identify risks, generate recommendations, produce executive reports, and evaluate governance effectiveness. Project information is sourced from Excel-based trackers, processed using Python and Pandas, and analyzed using Llama 3 through Ollama. The generated reports can be downloaded or automatically distributed to stakeholders through email.

---

## 📈 Key Features

✅ Automated Project Health Assessment

✅ AI-Based Risk Analysis

✅ Intelligent Recommendation Generation

✅ Governance Evaluation

✅ Executive Reporting

✅ Interactive Dashboard

✅ Downloadable Reports

✅ Automated Email Distribution

✅ Multi-Agent AI Architecture

---

## 📂 Project Structure

```text
📦 Project Folder
│
├── 📄 app.py
├── 📄 agents.py
├── 📄 requirements.txt
├── 📄 README.md
├── 📊 project_data.xlsx
│
└── 📁 reports
```

---

## 📋 Required Excel Format

The uploaded Excel file should contain the following columns:

```text
ProjectName
TaskName
Owner
Status
Priority
DueDate
```

### Sample Data

```text
ProjectName       TaskName       Owner   Status        Priority   DueDate
----------------------------------------------------------------------------
Customer Portal   Design         John    Completed     High       05-Sep-26
Customer Portal   Development    Mike    In Progress   High       08-Sep-26
Customer Portal   Testing        Alex    Delayed       High       10-Sep-26
Customer Portal   Deployment     John    Blocked       High       15-Sep-26
```

---

## 🚀 Installation

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```text
streamlit
pandas
openpyxl
ollama
```

---

## 🦙 Ollama Setup

### Verify Installation

```bash
ollama --version
```

### Download Llama 3

```bash
ollama pull llama3
```

### Verify Installed Models

```bash
ollama list
```

Expected Output:

```text
NAME      ID      SIZE
llama3    xxxx    4.7 GB
```

---

## ▶️ Running the Application

Start the application using:

```bash
streamlit run app.py
```

The dashboard will open automatically in your default browser.

---

## 📧 Email Configuration

The system supports automated report distribution through Gmail SMTP.

### Prerequisites

✅ Enable Two-Factor Authentication (2FA)

✅ Generate a Gmail App Password

✅ Use the App Password instead of the Gmail account password

---

## 📊 Expected Outcomes

- Improved project visibility and monitoring.
- Early identification of project risks and issues.
- Enhanced decision-making through AI-driven insights.
- Reduced manual reporting effort.
- Automated governance assessment.
- Improved stakeholder communication.
- Increased project management efficiency.

---

## 🔮 Future Enhancements

- Azure DevOps Integration
- Jira Integration
- Power BI Dashboard Integration
- Predictive Risk Analytics
- Resource Optimization Agent
- Multi-Project Portfolio Monitoring
- Microsoft Teams Integration
- Azure OpenAI Integration

---

## ✅ Conclusion

The **Agentic AI-Based Project Health and Risk Monitoring System for Automated Project Governance** successfully demonstrates the use of a multi-agent AI architecture for automating project health assessment, risk analysis, recommendation generation, governance evaluation, executive reporting, and stakeholder communication. By combining AI-driven analysis with automation, the solution enhances project visibility, improves governance effectiveness, reduces manual effort, and supports informed decision-making.

---

## 👨‍💻 Developed Using

- Python
- Streamlit
- Ollama
- Llama 3
- Pandas
- OpenPyXL
- Gmail SMTP

---

## 👤 Author

**Noel Jacob Biju**

---

## 📜 License

This project is developed for academic and research purposes.

---

⭐ **Intelligent Project Governance through Agentic AI and Multi-Agent Automation**
