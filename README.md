# Cybersecurity Research Agent

A Python-based multi-agent system for cybersecurity vulnerability research, threat intelligence analysis, risk assessment, and report generation.

# About the Project

Understanding a cybersecurity vulnerability requires collecting information from different sources, checking its severity, and assessing whether it is known to be exploited.

The Cybersecurity Research Agent automates these research steps through multiple specialised agents coordinated using LangGraph.

The system takes a CVE ID as input, retrieves vulnerability information, checks exploitation status, analyses risk, verifies selected findings, and generates a final research report.

# Project Workflow

User Query  
↓  
Planner Agent  
↓  
Research Agent → NVD API  
↓  
Threat Intelligence Agent → CISA KEV  
↓  
Analysis Agent  
↓  
Verification Agent  
↓  
Report Agent  
↓  
Final Cybersecurity Report

# Agents and Responsibilities

| Agent | Responsibility |
|---|---|
| Planner Agent | Extracts the CVE ID and identifies research tasks. |
| Research Agent | Retrieves vulnerability details from the NVD API. |
| Threat Intelligence Agent | Checks the CISA Known Exploited Vulnerabilities catalog. |
| Analysis Agent | Evaluates severity, risk level, and remediation recommendations. |
| Verification Agent | Checks consistency of selected research findings. |
| Report Agent | Generates the final cybersecurity research report. |

# Technologies Used

- Python 3.13
- LangGraph
- Streamlit (user interface)
- NVD API
- CISA Known Exploited Vulnerabilities (KEV) Catalog
- Requests
- TypedDict
# Example: Log4Shell

The project was tested using `CVE-2021-44228`, commonly known as Log4Shell.

Example results:

- CVE ID: CVE-2021-44228
- CVSS Score: 10.0
- Severity: CRITICAL
- CISA KEV Status: Listed as known exploited
- Verification: Passed
- Final Report: Generated successfully

#Error Handling

The system was also tested with an invalid CVE ID:

`CVE-9999-99999`

The NVD API did not return vulnerability details. The Research Agent reported the failure, and the workflow stopped safely instead of generating an incomplete report.

# Project Structure

```text
cybersecurity-research-agent/
│
├── agents/
│   ├── planner.py
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── verification_agent.py
│   └── report_agent.py
│
├── tools/
│   ├── nvd_tool.py
│   └── cisa_tool.py
│
├── workflow/
│   ├── state.py
│   ├── nodes.py
│   └── graph.py
│
├── app.py
├── run_workflow.py
├── requirements.txt
└── README.md
```

# Installation and Setup

# 1. Clone the repository

```bash
git clone https://github.com/vanshika22-source/cybersecurity-research-agent.git
```

# 2. Open the project directory

```bash
cd cybersecurity-research-agent
```

# 3. Create a virtual environment

```bash
python -m venv venv
```

# 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

# 5. Install dependencies

```bash
pip install -r requirements.txt
```

# 6. Run the application

To run the command-line workflow:

```bash
python run_workflow.py
```

To launch the Streamlit interface:

```bash
streamlit run app.py
```

# Current Limitations

- The Planner Agent currently uses rule-based CVE extraction.
- Agent operations use Python logic and external APIs rather than LLM-powered reasoning.
- Verification checks selected fields and is not a complete independent security audit.
- The workflow depends on external API availability.
- Not being listed in the CISA KEV catalog does not prove that a vulnerability has never been exploited.

# Future Improvements

- Integrate an LLM for more flexible query understanding and explanations.
- Add controlled retry and recovery mechanisms.
- Support multiple CVE investigations.
- Expand threat intelligence sources.
- Improve report generation and presentation.

# Information Sources

- [National Vulnerability Database (NVD)](https://nvd.nist.gov/)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview)

# Author

Vanshika Vaidya

Integrated M.Tech – Artificial Intelligence and Data Science  
Devi Ahilya Vishwavidyalaya (DAVV), Indore

GitHub: [vanshika22-source](https://github.com/vanshika22-source)
