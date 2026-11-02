
from langgraph.graph import StateGraph, START, END

from workflow.state import CybersecurityState

from workflow.nodes import (
    planner_node,
    research_node,
    threat_intelligence_node,
    analysis_node,
    verification_node,
    report_node
)


# Check whether an agent encountered an error
def check_errors(state):

    if state.get("errors"):
        return "stop"

    return "continue"


# Build the complete cybersecurity research workflow
def build_workflow():

    workflow = StateGraph(CybersecurityState)

    # Register all agent nodes
    workflow.add_node("planner", planner_node)
    workflow.add_node("research", research_node)
    workflow.add_node("threat_intelligence", threat_intelligence_node)
    workflow.add_node("analysis", analysis_node)
    workflow.add_node("verification", verification_node)
    workflow.add_node("report", report_node)

    # Start with the Planner Agent
    workflow.add_edge(START, "planner")

    # Planner -> Research
    workflow.add_conditional_edges(
        "planner",
        check_errors,
        {
            "continue": "research",
            "stop": END
        }
    )

    # Research -> Threat Intelligence
    workflow.add_conditional_edges(
        "research",
        check_errors,
        {
            "continue": "threat_intelligence",
            "stop": END
        }
    )

    # Threat Intelligence -> Analysis
    workflow.add_conditional_edges(
        "threat_intelligence",
        check_errors,
        {
            "continue": "analysis",
            "stop": END
        }
    )

    # Analysis -> Verification
    workflow.add_conditional_edges(
        "analysis",
        check_errors,
        {
            "continue": "verification",
            "stop": END
        }
    )

    # Verification -> Report (only if verification succeeds)
    workflow.add_conditional_edges(
        "verification",
        check_errors,
        {
            "continue": "report",
            "stop": END
        }
    )

    # Report -> End
    workflow.add_edge("report", END)

    # Compile the workflow
    return workflow.compile()
