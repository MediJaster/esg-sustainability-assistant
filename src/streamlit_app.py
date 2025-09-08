import os
import requests

import streamlit as st

from models.company_info import CompanyInfo
from models.feedback import FeedbackData
from models.inference import ESGResponse

STREAMLIT_API_URL = os.getenv("STREAMLIT_API_URL", "http://localhost:8080")

st.title("🌿 ESG Sustainability Assistant")


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

                st.success("✅ ESG Report Generated!")
                st.markdown(esg_report.final_report)

                # Star Rating Feedback
                st.divider()
                st.subheader("📊 Rate this ESG Report")

                # Create star rating using radio buttons
                rating = st.radio(
                    "How would you rate the quality and usefulness of this ESG report?",
                    options=[1, 2, 3, 4, 5],
                    format_func=lambda x: "⭐" * x + "☆" * (5 - x),
                    horizontal=True,
                    key="esg_report_rating",
                )

                # Optional feedback text
                feedback_text = st.text_area(
                    "Additional feedback (optional):",
                    placeholder="Share your thoughts about the report...",
                    key="esg_report_feedback",
                )

                # Submit feedback button
                if st.button("Submit Feedback", key="submit_feedback"):
                    # Store feedback in session state
                    st.session_state.feedback_data = FeedbackData(
                        trace_id=esg_report.trace_id,
                        rating=rating,
                        feedback_text=feedback_text if feedback_text.strip() else None,
                    )

                    st.success(
                        f"✅ Thank you for your feedback! You rated this report {rating}/5 stars."
                    )

                    # Optional: Send feedback to API
                    try:
                        feedback_response = requests.post(
                            f"{STREAMLIT_API_URL}/feedback",
                            json=st.session_state.feedback_data,
                        )
                        if feedback_response.status_code == 200:
                            st.info("📤 Feedback sent to improve our service!")
                    except Exception as feedback_error:
                        # Silently handle feedback API errors to not disrupt user experience
                        pass
            except Exception as e:
                st.error(f"❌ An error occurred with the API call:\n{e}")
