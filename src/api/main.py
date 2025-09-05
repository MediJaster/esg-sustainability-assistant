from fastapi import FastAPI

from models.esg_info import ESGInfo

from esg_sustainability_assistant.main import ESGFlow


app = FastAPI()


@app.post("/esg")
def kickoff_crew(input: ESGInfo) -> str:
    esg_flow = ESGFlow(esg_info=input, verbose=False)

    result = esg_flow.kickoff()
    return result
