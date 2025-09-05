from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from crewai_tools import SerperDevTool

# from mcp import StdioServerParameters
from typing import List
 
 
@CrewBase
class ESGAnalysisCrew:
    """ESG Analysis Crew"""
   
    agents: List[BaseAgent]
    tasks: List[Task]
 
    # mcp_server_params = [
    #     StdioServerParameters(
    #         command="docker",
    #         args=[
    #             "run",
    #             "-i",
    #             "--rm",
    #             "mcp/duckduckgo"
    #         ],
    #         # env={**os.environ}  # inherit your current environment
    #     )
    # ]

    @agent
    def esg_data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["esg_data_analyst"],  # type: ignore[index]
            tools=[SerperDevTool()],  # self.get_mcp_tools(),
            verbose=True
        )
   
 
    @task
    def analyze_esg_context(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_esg_context"],  # type: ignore[index]
            output_file="./out/report.md",
        )
   
    @crew
    def crew(self) -> Crew:
        """Creates the ESG Analysis Crew"""
 
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )