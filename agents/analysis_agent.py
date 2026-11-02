def analysis_agent(research_data, threat_data):

    print("\n[Analysis Agent] Analysing vulnerability...")

    if not research_data["success"]:
        return {
            "success": False,
            "error": "Research data is unavailable."
        }

    if not threat_data["success"]:
        return {
            "success": False,
            "error": "Threat intelligence data is unavailable."
        }

    cvss_score = research_data["cvss_score"]
    severity = research_data["severity"]

    known_exploited = threat_data["known_exploited"]

    if known_exploited:
        exploitation_status = "Known to be exploited (listed in CISA KEV)"
    else:
        exploitation_status = "Not listed in CISA KEV"

    if cvss_score is not None and cvss_score >= 9:
        risk_level = "CRITICAL"
    elif cvss_score is not None and cvss_score >= 7:
        risk_level = "HIGH"
    elif cvss_score is not None and cvss_score >= 4:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW or UNAVAILABLE"

    if known_exploited:
        recommendation = (
            "Prioritise remediation. Apply available security updates "
            "and investigate potentially affected systems."
        )
    else:
        recommendation = (
            "Review the affected software and apply available security updates."
        )

    print("[Analysis Agent] Analysis completed.")

    return {
        "success": True,
        "cve_id": research_data["cve_id"],
        "cvss_score": cvss_score,
        "severity": severity,
        "risk_level": risk_level,
        "exploitation_status": exploitation_status,
        "recommendation": recommendation
    }