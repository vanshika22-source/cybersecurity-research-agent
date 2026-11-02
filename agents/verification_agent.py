def verification_agent(research_data, threat_data, analysis_data):

    print("\n[Verification Agent] Verifying research findings...")

    issues = []

    # Check research data
    if not research_data.get("success"):
        issues.append("Research data retrieval failed.")

    # Check threat intelligence data
    if not threat_data.get("success"):
        issues.append("Threat intelligence retrieval failed.")

    # Check analysis data
    if not analysis_data.get("success"):
        issues.append("Risk analysis failed.")

    # Check CVE consistency
    if research_data.get("cve_id") != analysis_data.get("cve_id"):
        issues.append("CVE ID mismatch between research and analysis.")

    # Check CVSS score consistency
    if research_data.get("cvss_score") != analysis_data.get("cvss_score"):
        issues.append("CVSS score mismatch.")

    if issues:
        print("[Verification Agent] Verification failed.")

        return {
            "success": False,
            "verified": False,
            "issues": issues
        }

    print("[Verification Agent] All checks passed.")

    return {
        "success": True,
        "verified": True,
        "issues": [],
        "message": "Research findings passed verification."
    }