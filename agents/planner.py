
import re


def planner_agent(user_query):

    print("\n[Planner Agent] Understanding research request...")

    # Identify a CVE ID from the user's query
    cve_match = re.search(
        r"CVE-\d{4}-\d{4,}",
        user_query,
        re.IGNORECASE
    )

    if not cve_match:
        return {
            "success": False,
            "error": "No valid CVE ID found in the query."
        }

    cve_id = cve_match.group().upper()

    print(f"[Planner Agent] Identified vulnerability: {cve_id}")

    # Break the research query into smaller tasks
    tasks = [
        {
            "agent": "Research Agent",
            "task": "Retrieve vulnerability description and CVSS severity",
            "tool": "NVD"
        },
        {
            "agent": "Threat Intelligence Agent",
            "task": "Check whether the vulnerability is known to be exploited",
            "tool": "CISA KEV"
        },
        {
            "agent": "Analysis Agent",
            "task": "Analyse severity and exploitation evidence",
            "tool": "Python Analysis"
        },
        {
            "agent": "Verification Agent",
            "task": "Verify completeness and consistency of findings",
            "tool": "Validation"
        },
        {
            "agent": "Report Agent",
            "task": "Generate the final cybersecurity research report",
            "tool": "Report Generator"
        }
    ]

    print("\n[Planner Agent] Research plan created.")

    return {
        "success": True,
        "original_query": user_query,
        "cve_id": cve_id,
        "tasks": tasks
    }
