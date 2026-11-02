
from agents.planner import planner_agent


query = "Research CVE-2021-44228 and explain its security impact."

result = planner_agent(query)


print("\n========== PLANNER RESULT ==========")

if result["success"]:

    print("Original Query:", result["original_query"])
    print("Identified CVE:", result["cve_id"])

    print("\nResearch Tasks:")

    for index, task in enumerate(result["tasks"], start=1):

        print(f"\nTask {index}")
        print("Agent:", task["agent"])
        print("Task:", task["task"])
        print("Tool:", task["tool"])

else:

    print("Error:", result["error"])
