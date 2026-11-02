from agents.planner import planner_agent
from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.verification_agent import verification_agent
from tools.cisa_tool import check_exploitation

from agents.report_agent import report_agent
def planner_node(state):

    print("\n========== PLANNER NODE ==========")

    result = planner_agent(state["user_query"])

    if not result["success"]:
        return {
            "errors": [result["error"]]
        }

    return {
        "cve_id": result["cve_id"]
    }


def research_node(state):

    print("\n========== RESEARCH NODE ==========")

    result = research_agent(state["cve_id"])

    if not result["success"]:
        return {
            "errors": [result["error"]]
        }

    return {
        "research_data": result
    }


def threat_intelligence_node(state):

    print("\n========== THREAT INTELLIGENCE NODE ==========")

    result = check_exploitation(state["cve_id"])

    if not result["success"]:
        return {
            "errors": [result["error"]]
        }

    return {
        "threat_data": result
    }


def analysis_node(state):

    print("\n========== ANALYSIS NODE ==========")

    result = analysis_agent(
        state["research_data"],
        state["threat_data"]
    )

    if not result["success"]:
        return {
            "errors": [result["error"]]
        }

    return {
        "analysis_data": result
    }


def verification_node(state):

    print("\n========== VERIFICATION NODE ==========")

    result = verification_agent(
        state["research_data"],
        state["threat_data"],
        state["analysis_data"]
    )

    if not result["success"]:
        return {
            "verification_data": result,
            "errors": result["issues"]
        }

    return {
        "verification_data": result
    }
def report_node(state):

    print("\n========== REPORT NODE ==========")

    result = report_agent(
        state["research_data"],
        state["threat_data"],
        state["analysis_data"],
        state["verification_data"]
    )

    if not result["success"]:
        return {
            "errors": [result["error"]]
        }

    return {
        "final_report": result["report"]
    }