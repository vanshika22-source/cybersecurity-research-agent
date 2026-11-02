
import requests

CISA_API_URL = (
    "https://www.cisa.gov/sites/default/files/feeds/"
    "known_exploited_vulnerabilities.json"
)


def check_exploitation(cve_id):

    print(f"\n[Threat Intelligence Agent] Checking {cve_id}...")

    try:
        response = requests.get(CISA_API_URL, timeout=30)
        response.raise_for_status()

        data = response.json()

        vulnerabilities = data.get("vulnerabilities", [])

        for vulnerability in vulnerabilities:

            if vulnerability.get("cveID") == cve_id:

                return {
                    "success": True,
                    "cve_id": cve_id,
                    "known_exploited": True,
                    "vendor": vulnerability.get("vendorProject"),
                    "product": vulnerability.get("product"),
                    "date_added": vulnerability.get("dateAdded"),
                    "required_action": vulnerability.get("requiredAction"),
                    "due_date": vulnerability.get("dueDate"),
                    "source": "CISA Known Exploited Vulnerabilities Catalog"
                }

        return {
            "success": True,
            "cve_id": cve_id,
            "known_exploited": False,
            "message": "Not found in CISA KEV catalog."
        }

    except requests.exceptions.RequestException as error:

        return {
            "success": False,
            "error": str(error)
        }

    except ValueError as error:

        return {
            "success": False,
            "error": f"Invalid API response: {error}"
        }
