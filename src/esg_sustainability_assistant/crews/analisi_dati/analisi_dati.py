import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool


from src.settings import llm_settings, embedder_settings


@CrewBase
class ESGDataAnalystCrew:
    """ESG Data Analyst specialized crew for sector analysis and benchmarking"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def esg_sector_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["esg_sector_researcher"],
            tools=[SerperDevTool()],
            verbose=True,
            max_iter=3,
            memory=True,
        )

    @agent
    def competitor_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitor_intelligence_analyst"],
            tools=[
                SerperDevTool(),
                # WebsiteSearchTool(
                #     config={
                #         "llm": llm_settings,
                #         "embedder": embedder_settings,
                #     }
                # ),
            ],
            verbose=True,
            max_iter=3,
            memory=True,
        )

    @agent
    def company_profile_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["company_profile_researcher"],
            tools=[
                SerperDevTool(),
                # WebsiteSearchTool(
                #     config={
                #         "llm": llm_settings,
                #         "embedder": embedder_settings,
                #     }
                # ),
            ],
            verbose=True,
            max_iter=4,  # Più iterazioni per ricerca approfondita dell'azienda
            memory=True,
        )

    @agent
    def market_trends_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["market_trends_analyst"],
            tools=[SerperDevTool()],
            verbose=True,
            max_iter=3,
            memory=True,
        )

    @agent
    def data_synthesis_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["data_synthesis_specialist"],
            verbose=True,
            max_iter=2,  # Non fa ricerca, solo sintesi
            memory=True,
        )

    @task
    def sector_challenges_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["sector_challenges_research_task"],
        )

    @task
    def competitor_best_practices_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitor_best_practices_task"],
        )

    @task
    def company_profile_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["company_profile_research_task"],
        )

    @task
    def market_trends_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_trends_analysis_task"],
        )

    @task
    def comprehensive_benchmark_synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config["comprehensive_benchmark_synthesis_task"],
            output_file="./out/esg_benchmark_analysis.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ESG Data Analyst specialized crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            # process=Process.sequential ,
            verbose=True,
            # memory=True,  # Enable crew memory for better context retention
            # embedder=embedder_settings,
            # max_rpm=10,  # Rate limiting per rispettare API limits
        )
