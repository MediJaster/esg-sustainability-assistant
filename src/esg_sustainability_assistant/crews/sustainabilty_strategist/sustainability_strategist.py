from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from src.settings import embedder_settings


@CrewBase
class SustainabilityStrategistCrew:
    """Sustainability Strategist specialized crew for actionable ESG strategic planning"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def environmental_strategy_designer(self) -> Agent:
        return Agent(
            config=self.agents_config["environmental_strategy_designer"],
            verbose=True,
            max_iter=3,
            memory=True,
        )

    @agent
    def social_impact_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["social_impact_strategist"],
            verbose=True,
            max_iter=3,
            memory=True,
        )

    @agent
    def governance_excellence_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["governance_excellence_advisor"],
            verbose=True,
            max_iter=2,
            memory=True,
        )

    @agent
    def roi_impact_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["roi_impact_analyst"],
            verbose=True,
            max_iter=2,
            memory=True,
        )

    @agent
    def strategic_prioritization_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["strategic_prioritization_expert"],
            verbose=True,
            max_iter=2,
            memory=True,
        )

    @task
    def environmental_initiatives_design_task(self) -> Task:
        return Task(
            config=self.tasks_config["environmental_initiatives_design_task"],
        )

    @task
    def social_impact_programs_task(self) -> Task:
        return Task(
            config=self.tasks_config["social_impact_programs_task"],
        )

    @task
    def governance_framework_design_task(self) -> Task:
        return Task(
            config=self.tasks_config["governance_framework_design_task"],
        )

    @task
    def roi_impact_quantification_task(self) -> Task:
        return Task(
            config=self.tasks_config["roi_impact_quantification_task"], context=[]
        )

    @task
    def integrated_strategic_action_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config["integrated_strategic_action_plan_task"],
            output_file="esg_strategic_action_plan.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Sustainability Strategist specialized crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            # process=Process.sequential ,
            verbose=True,
            # memory=True,
            # embedder=embedder_settings,
            # max_rpm=15,  # Più alto perché non usa search tools
        )
