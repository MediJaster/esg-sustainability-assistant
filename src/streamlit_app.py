"""
Streamlit UI for the ESG Sustainability Assistant.

This module provides a simple interface to submit company information,
request an ESG report from the backend API, and optionally send user feedback.

Environment Variables
---------------------
STREAMLIT_API_URL : str, optional
    Base URL of the backend API. Defaults to ``"http://localhost:8080"``.

Notes
-----
This module is intended to be executed by Streamlit and does not expose
public functions. The code path runs at import time in the Streamlit app
runtime.
"""

import os
import requests

import streamlit as st
from streamlit_star_rating import st_star_rating

from models.company_info import CompanyInfo
from models.feedback import FeedbackData
from models.inference import ESGResponse

STREAMLIT_API_URL = os.getenv("STREAMLIT_API_URL", "http://localhost:8080")

st.session_state.final_report = (
    None if "final_report" not in st.session_state else st.session_state.final_report
)

st.title("🌿 ESG Sustainability Assistant")

if st.session_state.final_report is None:
    st.info("ℹ️ Please provide the company details below to generate an ESG report.")

    st.session_state.company_name = st.text_input("Company Name:")
    st.session_state.industry_sector = st.text_input("Industry Sector:")

    if st.button("Generate ESG Report"):
        if not st.session_state.company_name or not st.session_state.industry_sector:
            st.error("❌ Please provide both Company Name and Industry Sector.")
        else:
            with st.spinner("Generating ESG Report, this may take a while..."):
                company_info = CompanyInfo(
                    name=st.session_state.company_name,
                    industry_sector=st.session_state.industry_sector,
                )

                try:
                    result = requests.post(
                        f"{STREAMLIT_API_URL}/esg", json=company_info.model_dump()
                    ).json()

                    esg_report = ESGResponse.model_validate(result)

                    # esg_report = ESGResponse(
                    #     final_report="This is a placeholder ESG report.",
                    #     trace_id="12345",
                    # )

                    st.session_state.final_report = esg_report.final_report
                    st.session_state.trace_id = esg_report.trace_id

                    st.success("✅ ESG Report Generated!")
                except Exception as e:
                    st.error(f"❌ An error occurred with the API call:\n{e}")

if st.session_state.final_report is not None:
    st.divider()
    st.markdown(st.session_state.final_report)

    # Star Rating Feedback
    st.divider()
    st.subheader("📊 Rate this ESG Report")

    # Create star rating using st_star_rating
    st.session_state.rating_value = st_star_rating(
        label="How would you rate the quality and usefulness of this ESG report?",
        defaultValue=0,
        maxValue=5,
        key="esg_report_rating_value",
    )

    # Optional feedback text
    st.session_state.rating_feedback_text = st.text_area(
        "Additional feedback (optional):",
        placeholder="Share your thoughts about the report...",
        key="esg_report_feedback",
    )

    # Submit feedback button
    if st.button("Submit Feedback", key="submit_feedback"):
        # Store feedback in session state
        st.session_state.feedback_data = FeedbackData(
            trace_id=st.session_state.trace_id,
            rating=st.session_state.rating_value,
            feedback_text=st.session_state.rating_feedback_text
            if st.session_state.rating_feedback_text.strip()
            else None,
        )

        try:
            feedback_response = requests.post(
                f"{STREAMLIT_API_URL}/feedback",
                json=st.session_state.feedback_data.model_dump(),
            )
            if feedback_response.status_code == 200:
                st.success(
                    f"✅ Thank you for your feedback! You rated this report {st.session_state.rating_value}/5 stars."
                )
                st.info("📤 Feedback sent to improve our service!")
        except Exception as e:
            st.error(f"❌ An error occurred while sending feedback:\n{e}")
