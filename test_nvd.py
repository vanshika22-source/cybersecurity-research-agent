
from tools.nvd_tool import search_vulnerability

result = search_vulnerability("CVE-2021-44228")

print("\n========== RESEARCH RESULT ==========")

if result["success"]:
    print("CVE ID:", result["cve_id"])
    print("Description:", result["description"])
    print("CVSS Score:", result["cvss_score"])
    print("Severity:", result["severity"])
    print("Published:", result["published"])
else:
    print("Error:", result["error"])
