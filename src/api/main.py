import mlflow
from fastapi import FastAPI, HTTPException

from models.company_info import CompanyInfo

from esg_sustainability_assistant.main import ESGSustainabilityFlow

from models.inference import ESGResponse
from models.feedback import FeedbackData


app = FastAPI()


@app.post("/esg", tags=["Inference"])
def generate_esg_report(input: CompanyInfo) -> ESGResponse | None:
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
    mlflow.log_feedback(
        trace_id=feedback.trace_id,
        value=feedback.rating,
        rationale=feedback.feedback_text,
    )
