from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.verification_agent import verification_agent
from tools.cisa_tool import check_exploitation

cve_id = "CVE-2021-44228"

# Step 1: Research
research_data = research_agent(cve_id)

print("\nResearch Success:", research_data.get("success"))
if not research_data.get("success"):
    print("Research Error:", research_data.get("error"))

# Step 2: Threat intelligence
threat_data = check_exploitation(cve_id)

print("\nThreat Intelligence Success:", threat_data.get("success"))
if not threat_data.get("success"):
    print("Threat Intelligence Error:", threat_data.get("error"))

# Step 3: Analysis
analysis_data = analysis_agent(research_data, threat_data)

print("\nAnalysis Success:", analysis_data.get("success"))
if not analysis_data.get("success"):
    print("Analysis Error:", analysis_data.get("error"))

# Step 4: Verification
verification_data = verification_agent(
    research_data,
    threat_data,
    analysis_data
)

print("\n========== VERIFICATION RESULT ==========")
print("Verification Successful:", verification_data["success"])
print("Verified:", verification_data["verified"])
print("Issues:", verification_data["issues"])