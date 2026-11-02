
import requests


NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def search_vulnerability(cve_id):

    print(f"\n[Research Tool] Searching for {cve_id}...")

    try:
        response = requests.get(
            NVD_API_URL,
            params={"cveId": cve_id},
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        vulnerabilities = data.get("vulnerabilities", [])

        if not vulnerabilities:
            return {
                "success": False,
                "error": f"No vulnerability found for {cve_id}"
            }

        cve = vulnerabilities[0]["cve"]

        description = next(
            (
                item["value"]
                for item in cve.get("descriptions", [])
                if item["lang"] == "en"
            ),
            "No description available"
        )

        metrics = cve.get("metrics", {})

        cvss_score = None
        severity = "Not available"

        for metric_type in ["cvssMetricV40", "cvssMetricV31",
                            "cvssMetricV30", "cvssMetricV2"]:

            metric_list = metrics.get(metric_type, [])

            if metric_list:
                cvss_data = metric_list[0].get("cvssData", {})
                cvss_score = cvss_data.get("baseScore")
                severity = cvss_data.get(
                    "baseSeverity",
                    "Not available"
                )
                break

        return {
            "success": True,
            "cve_id": cve.get("id"),
            "description": description,
            "cvss_score": cvss_score,
            "severity": severity,
            "published": cve.get("published"),
            "last_modified": cve.get("lastModified"),
            "source": "NIST National Vulnerability Database"
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "NVD API request timed out."
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": f"API request failed: {error}"
        }

    except (KeyError, IndexError, ValueError) as error:
        return {
            "success": False,
            "error": f"Could not process NVD response: {error}"
        }
