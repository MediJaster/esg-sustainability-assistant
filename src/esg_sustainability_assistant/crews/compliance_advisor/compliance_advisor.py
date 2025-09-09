import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, WebsiteSearchTool
from typing import List

from src.settings import llm_settings, embedder_settings


@CrewBase
class ESGComplianceAdvisorCrew:
    """ESG Compliance Advisor specialized crew for regulatory mapping and framework selection"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        super().__init__()
        # Initialize search tools for compliance research
        self.search_tool = SerperDevTool()
        # self.website_search_tool = WebsiteSearchTool(
        #     config={
        #         "llm": llm_settings,
        #         "embedder": embedder_settings,
        #     }
        # )

    @agent
    def regulatory_framework_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["regulatory_framework_specialist"],
            tools=[self.search_tool],
            verbose=True,
            max_iter=4,  # Normative complesse richiedono più iterazioni
            memory=True,
        )

    @agent
    def international_standards_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["international_standards_advisor"],
            tools=[
                self.search_tool,
                # self.website_search_tool
            ],
            verbose=True,
            max_iter=3,
            memory=True,
        )

    @agent
    def sector_compliance_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["sector_compliance_analyst"],
            tools=[self.search_tool],
            verbose=True,
            max_iter=3,
            memory=True,
        )

    @agent
    def implementation_timeline_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config["implementation_timeline_coordinator"],
            verbose=True,
            max_iter=2,  # Timeline development richiede meno ricerca
            memory=True,
        )

    @agent
    def compliance_synthesis_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["compliance_synthesis_expert"],
            verbose=True,
            max_iter=2,  # Solo sintesi, no ricerca
            memory=True,
        )

    @task
    def mandatory_regulations_mapping_task(self) -> Task:
        return Task(
            config=self.tasks_config["mandatory_regulations_mapping_task"],
        )

    @task
    def voluntary_standards_selection_task(self) -> Task:
        return Task(
            config=self.tasks_config["voluntary_standards_selection_task"],
        )

    @task
    def sector_specific_requirements_task(self) -> Task:
        return Task(
            config=self.tasks_config["sector_specific_requirements_task"],
        )

    @task
    def comprehensive_compliance_roadmap_task(self) -> Task:
        return Task(
            config=self.tasks_config["comprehensive_compliance_roadmap_task"],
            output_file="./out/esg_compliance_roadmap.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ESG Compliance Advisor specialized crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            # process=Process.sequential ,
            verbose=True,
            # memory=True,
            # embedder=embedder_settings,
            # max_rpm=10,
        )
