from fastapi import FastAPI

from models.company_info import CompanyInfo

from esg_sustainability_assistant.main import ESGSustainabilityFlow


app = FastAPI()


@app.post("/esg")
def kickoff_crew(input: CompanyInfo) -> dict[str, str]:
    esg_flow = ESGSustainabilityFlow(company_info=input, verbose=False)

    result = esg_flow.kickoff()
    return result
