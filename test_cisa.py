
from tools.cisa_tool import check_exploitation

result = check_exploitation("CVE-2021-44228")

print("\n========== THREAT INTELLIGENCE RESULT ==========")

if result["success"]:

    print("CVE ID:", result["cve_id"])
    print("Known Exploited:", result["known_exploited"])

    if result["known_exploited"]:
        print("Vendor:", result["vendor"])
        print("Product:", result["product"])
        print("Date Added:", result["date_added"])
        print("Required Action:", result["required_action"])
        print("Due Date:", result["due_date"])

    else:
        print(result["message"])

else:
    print("Error:", result["error"])
