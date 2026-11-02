from agents.research_agent import research_agent

result = research_agent("CVE-2021-44228")

print("\n========== RESEARCH RESULT ==========")

if result["success"]:
    print("CVE ID:", result["cve_id"])
    print("Description:", result["description"])
    print("CVSS Score:", result["cvss_score"])
    print("Severity:", result["severity"])
    print("Published:", result["published"])
    print("Last Modified:", result["last_modified"])
    print("Source:", result["source"])
else:
    print("Error:", result["error"])