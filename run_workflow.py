from workflow.graph import build_workflow


def main():

    print("\n====================================")
    print(" CYBERSECURITY RESEARCH AGENT")
    print("====================================")

    # Get user input
    user_query = input("\nEnter your cybersecurity research query: ")

    # Build LangGraph workflow
    app = build_workflow()

    # Initialize shared state
    initial_state = {
        "user_query": user_query,
        "cve_id": None,
        "research_data": None,
        "threat_data": None,
        "analysis_data": None,
        "verification_data": None,
        "final_report": None,
        "errors": []
    }

    print("\n[System] Starting multi-agent workflow...")

    # Execute workflow
    result = app.invoke(initial_state)

    print("\n====================================")
    print(" WORKFLOW EXECUTION COMPLETED")
    print("====================================")

    if result.get("errors"):
        print("\nWorkflow Errors:")
        for error in result["errors"]:
            print("-", error)

    else:
        print("\nCVE ID:", result["cve_id"])

        print("\nRisk Analysis:")
        print("CVSS Score:", result["analysis_data"]["cvss_score"])
        print("Severity:", result["analysis_data"]["severity"])
        print("Risk Level:", result["analysis_data"]["risk_level"])

        print("\nExploitation Status:")
        print(result["analysis_data"]["exploitation_status"])

        print("\nVerification:")
        print(result["verification_data"]["message"])

        print("\nRecommendation:")
        print(result["analysis_data"]["recommendation"])
        
        print("\n========== FINAL CYBERSECURITY REPORT ==========")

        print(result["final_report"])


if __name__ == "__main__":
    main()