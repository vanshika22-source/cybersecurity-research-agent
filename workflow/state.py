from typing import TypedDict, Optional


class CybersecurityState(TypedDict):

    user_query: str
    cve_id: Optional[str]

    research_data: Optional[dict]
    threat_data: Optional[dict]

    analysis_data: Optional[dict]
    verification_data: Optional[dict]

    final_report: Optional[str]

    errors: list