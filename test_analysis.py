from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from tools.cisa_tool import check_exploitation

# Step 1: Get vulnerability research
research_data = research_agent("CVE-2021-44228")

# Step 2: Get threat intelligence
threat_data = check_exploitation("CVE-2021-44228")

# Step 3: Analyse both results
result = analysis_agent(research_data, threat_data)

# Step 4: Display the analysis
print("\n========== ANALYSIS RESULT ==========")

if result["success"]:
    print("CVE ID:", result["cve_id"])
    print("CVSS Score:", result["cvss_score"])
    print("Severity:", result["severity"])
    print("Risk Level:", result["risk_level"])
    print("Exploitation Status:", result["exploitation_status"])
    print("Recommendation:", result["recommendation"])
else:
    print("Error:", result["error"])