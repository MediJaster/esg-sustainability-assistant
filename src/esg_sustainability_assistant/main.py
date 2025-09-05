from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from .crews.data_analysis.data_analysis import ESGAnalysisCrew


class EsgState(BaseModel):
    pass


class EsgFlow(Flow[EsgState]):

    @start()
    def generate_sentence_count(self):
        company_name = input("company_name > ")
        industry_sector = input("industry_sector > ")
        data_analysis_crew = ESGAnalysisCrew()
        res = data_analysis_crew.crew().kickoff(
            inputs={
                "company_name": company_name,
                "industry_sector": industry_sector
            }
        )

def kickoff():
    esg_flow = EsgFlow()
    esg_flow.kickoff()

def plot():
    esg_flow = EsgFlow()
    esg_flow.plot()


if __name__ == "__main__":
    kickoff()
