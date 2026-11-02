
def report_agent(research_data, threat_data, analysis_data, verification_data):

    print("\n[Report Agent] Generating cybersecurity report...")

    # Check whether the research was verified
    if not verification_data or not verification_data.get("verified"):
        return {
            "success": False,
            "error": "Report cannot be generated because verification failed."
        }

    cve_id = research_data.get("cve_id", "N/A")
    description = research_data.get("description", "Not available")
    cvss = research_data.get("cvss_score", "N/A")
    severity = research_data.get("severity", "Unknown")
    risk = analysis_data.get("risk_level", "Unknown")
    known_exploited = threat_data.get("known_exploited", False)

    vendor = threat_data.get("vendor", "Not available")
    product = threat_data.get("product", "Not available")
    date_added = threat_data.get("date_added", "Not available")

    recommendation = analysis_data.get(
        "recommendation",
        "Review the vulnerability and apply appropriate security updates."
    )

    # Plain-language explanation for Log4Shell
    if cve_id == "CVE-2021-44228":
        simple_explanation = (
            "Log4Shell is a security weakness in Apache Log4j2, "
            "a logging library used by Java applications. Under "
            "affected conditions, an attacker could send specially "
            "crafted information to a vulnerable application and "
            "potentially cause it to execute malicious code on its server."
        )
        impact = (
            "An affected server could be compromised, potentially "
            "allowing attackers to access data or perform unauthorized actions."
        )
        affected = (
            "Organizations using vulnerable versions of the "
            "Apache Log4j2 log4j-core component."
        )
    else:
        simple_explanation = (
            "This vulnerability represents a security weakness in "
            "the affected software. Its exact impact depends on the "
            "vulnerability details and the affected system."
        )
        impact = (
            "The potential impact should be assessed using the "
            "technical description and severity information below."
        )
        affected = (
            "Check the affected products and versions in the NVD "
            "record before deciding whether your systems are affected."
        )

    if known_exploited:
        exploitation = (
            "YES. This vulnerability is listed in the CISA Known "
            "Exploited Vulnerabilities catalog."
        )
    else:
        exploitation = (
            "NOT LISTED in the CISA KEV catalog at the time of this check. "
            "This does not prove that exploitation has never occurred."
        )

    report = f"""
============================================================
              CYBERSECURITY RESEARCH REPORT
============================================================

VULNERABILITY: {cve_id}

1. WHAT DOES THIS MEAN? (SIMPLE EXPLANATION)

{simple_explanation}

2. WHY IS IT A SECURITY CONCERN?

{impact}

3. WHO COULD BE AFFECTED?

{affected}

4. HOW DANGEROUS IS IT?

CVSS Score: {cvss} / 10
Severity: {severity}
Risk Level: {risk}

5. HAS THIS VULNERABILITY BEEN EXPLOITED?

{exploitation}

Vendor: {vendor}
Product: {product}
Date added to CISA KEV: {date_added}

6. WHAT SHOULD ORGANIZATIONS DO?

{recommendation}

Additional recommended steps:
- Identify applications using the affected software.
- Check whether vulnerable versions are installed.
- Upgrade to an appropriate fixed version.
- Investigate systems for possible compromise.
- Monitor security logs for suspicious activity.

7. TECHNICAL DETAILS

Original NVD Description:
{description}

8. VERIFICATION RESULTS

Status: PASSED
Message: {verification_data.get("message", "Research findings verified.")}

9. INFORMATION SOURCES

NVD:
https://nvd.nist.gov/vuln/detail/{cve_id}

CISA KEV:
https://www.cisa.gov/known-exploited-vulnerabilities-catalog

============================================================
                 END OF REPORT
============================================================
"""

    print("[Report Agent] Report generated successfully.")

    return {
        "success": True,
        "cve_id": cve_id,
        "report": report
    }
