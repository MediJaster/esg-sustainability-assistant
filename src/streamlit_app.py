import os
import requests

import streamlit as st

from models.company_info import CompanyInfo

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

                st.success("✅ ESG Report Generated!")
                st.markdown(result["final_report"])
            except Exception as e:
                st.error(f"❌ An error occurred with the API call:\n{e}")
