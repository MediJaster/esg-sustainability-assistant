from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from models.esg_info import ESGInfo

from .crews.data_analysis.data_analysis import ESGAnalysisCrew


class ESGState(BaseModel):
    esg_info: ESGInfo = None

    preliminary_analysis: str = ""


class ESGFlow(Flow[ESGState]):
    @start()
    def generate_preliminary_analysis(self):
        data_analysis_crew = ESGAnalysisCrew()
        result = data_analysis_crew.crew().kickoff(
            inputs=self.state.esg_info.model_dump()
        )

        self.state.preliminary_analysis = result.raw

        return self.state.preliminary_analysis


def kickoff():
    esg_flow = ESGFlow()
    esg_flow.kickoff()


def plot():
    esg_flow = ESGFlow()
    esg_flow.plot()


if __name__ == "__main__":
    kickoff()
