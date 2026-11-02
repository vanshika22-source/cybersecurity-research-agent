
import streamlit as st
from workflow.graph import build_workflow
from contextlib import redirect_stdout
from io import StringIO

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Cybersecurity Research Agent",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CUSTOM STYLING ----------------

st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #00c8ff;
    }
    .subtitle {
        color: #aab7c4;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🛡️ Cybersecurity Research Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Multi-Agent Vulnerability Research and Risk Analysis System</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown("### 🔍 Vulnerability Research")

# ---------------- USER INPUT ----------------

with st.form("research_form"):

    user_query = st.text_area(
        "Enter your cybersecurity research query:",
        value=(
            "Research CVE-2021-44228 (Log4Shell). "
            "Retrieve its vulnerability details, check CISA KEV, "
            "analyze its risk, verify findings, and generate a report."
        ),
        height=120
    )

    submit = st.form_submit_button(
        "🚀 Run Research",
        use_container_width=True
    )

# ---------------- WORKFLOW EXECUTION ----------------

if submit:

    if not user_query.strip():
        st.warning("Please enter a research query.")

    else:

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

        execution_log = StringIO()

        try:
            with st.spinner("Executing multi-agent research workflow..."):

                workflow = build_workflow()

                with redirect_stdout(execution_log):
                    result = workflow.invoke(initial_state)

            st.success("Workflow execution completed!")

            # ---------------- EXECUTION TRACE ----------------

            st.markdown("### ⚙️ Agent Execution Trace")

            with st.expander("View agent execution logs", expanded=True):
                st.code(execution_log.getvalue(), language="text")

            # ---------------- ERROR HANDLING ----------------

            if result.get("errors"):

                st.error("Research could not be completed.")

                for error in result["errors"]:
                    st.write(f"- {error}")

            else:

                analysis = result.get("analysis_data", {})
                threat = result.get("threat_data", {})
                verification = result.get("verification_data", {})

                # ---------------- RESULTS ----------------

                st.divider()
                st.markdown("### 📊 Vulnerability Analysis")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "CVE ID",
                    result.get("cve_id", "N/A")
                )

                col2.metric(
                    "CVSS Score",
                    analysis.get("cvss_score", "N/A")
                )

                col3.metric(
                    "Risk Level",
                    analysis.get("risk_level", "N/A")
                )

                st.markdown("### 🚨 Threat Intelligence")

                if threat.get("known_exploited"):
                    st.error("Known Exploitation: Listed in CISA KEV")
                else:
                    st.info("Known Exploitation: Not listed in CISA KEV")

                st.markdown("### ✅ Verification")

                if verification.get("verified"):
                    st.success(verification.get("message", "Verification passed."))
                else:
                    st.warning("Verification did not pass.")

                st.markdown("### 💡 Recommendation")

                st.write(
                    analysis.get(
                        "recommendation",
                        "No recommendation available."
                    )
                )

                # ---------------- FINAL REPORT ----------------

                report = result.get("final_report")

                if report:

                    st.divider()
                    st.markdown("### 📄 Final Cybersecurity Report")

                    st.text(report)

                    st.download_button(
                        label="⬇️ Download Research Report",
                        data=report,
                        file_name=f"{result.get('cve_id', 'cybersecurity_report')}_report.txt",
                        mime="text/plain"
                    )

                else:
                    st.warning("No final report was generated.")

        except Exception as e:

            st.error(f"An unexpected error occurred: {e}")

            with st.expander("Execution logs"):
                st.code(execution_log.getvalue())
