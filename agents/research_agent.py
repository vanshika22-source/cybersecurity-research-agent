from tools.nvd_tool import search_vulnerability


def research_agent(cve_id):

    print("\n[Research Agent] Starting vulnerability research...")

    result = search_vulnerability(cve_id)

    if not result["success"]:
        print("[Research Agent] Research failed.")

        return {
            "success": False,
            "cve_id": cve_id,
            "error": result["error"]
        }

    print("[Research Agent] Vulnerability details retrieved.")

    return {
        "success": True,
        "cve_id": result["cve_id"],
        "description": result["description"],
        "cvss_score": result["cvss_score"],
        "severity": result["severity"],
        "published": result["published"],
        "last_modified": result["last_modified"],
        "source": result["source"]
    }