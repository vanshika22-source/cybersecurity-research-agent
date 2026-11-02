from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.verification_agent import verification_agent
from agents.report_agent import report_agent
from tools.cisa_tool import check_exploitation

cve_id = "CVE-2021-44228"

research_data = research_agent(cve_id)

threat_data = check_exploitation(cve_id)

analysis_data = analysis_agent(
    research_data,
    threat_data
)

verification_data = verification_agent(
    research_data,
    threat_data,
    analysis_data
)

result = report_agent(
    research_data,
    threat_data,
    analysis_data,
    verification_data
)

print("\n========== FINAL REPORT ==========")

if result["success"]:
    print(result["report"])
else:
    print("Error:", result["error"])