"""FastAPI routes for ESG report generation and feedback endpoints."""

import mlflow
from fastapi import FastAPI, HTTPException

from models.company_info import CompanyInfo

from esg_sustainability_assistant.main import ESGSustainabilityFlow

from models.inference import ESGResponse
from models.feedback import FeedbackData


app = FastAPI(title="ESG Sustainability Assistant API")


@app.post("/esg", tags=["Inference"])
def generate_esg_report(input: CompanyInfo) -> ESGResponse | None:
    """
    Generate an ESG report for a given company.

    Parameters
    ----------
    input : CompanyInfo
        Company information for which to generate the ESG report.

    Returns
    -------
    ESGResponse or None
        ESG report response object, or None if generation fails.

    Raises
    ------
    HTTPException
        If an error occurs during report generation.

    Examples
    --------
    >>> from models.company_info import CompanyInfo
    >>> input = CompanyInfo(name="TestCo", industry_sector="Tech")
    >>> generate_esg_report(input)  # doctest: +SKIP
    ESGResponse(...)

    Notes
    -----
    Complexity: O(1) for orchestration; underlying flow logic may vary.
    """
    try:
        with mlflow.start_run(run_name="API_ESG_Analysis", nested=True):
            mlflow.log_param("company_name", input.name)
            mlflow.log_param("industry_sector", input.industry_sector)
            # Log other CompanyInfo fields if present
            for field, value in input.model_dump().items():
                if field not in ["name", "industry_sector"]:
                    mlflow.log_param(field, value)

            esg_flow = ESGSustainabilityFlow(company_info=input, verbose=False)
            result = esg_flow.kickoff()

            # Log result keys as params (truncate long values)
            if isinstance(result, dict):
                for k, v in result.items():
                    mlflow.log_param(
                        k, v if len(str(v)) < 500 else str(v)[:500] + "..."
                    )

            response = ESGResponse(
                final_report=result["final_report"],
                trace_id=result["trace_id"],
            )
            return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/feedback", tags=["Feedback"])
def submit_feedback(feedback: FeedbackData) -> None:
    """
    Submit feedback for a generated ESG report.

    Parameters
    ----------
    feedback : FeedbackData
        Feedback data including trace ID, rating (1-5), and optional text.

    Returns
    -------
    None

    Examples
    --------
    >>> from models.feedback import FeedbackData
    >>> fb = FeedbackData(trace_id="abc123", rating=5)
    >>> submit_feedback(fb)  # doctest: +SKIP

    Notes
    -----
    Complexity: O(1).
    """
    mlflow.log_feedback(
        trace_id=feedback.trace_id,
        value=feedback.rating,
        rationale=feedback.feedback_text,
    )
