from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from src.settings import embedder_settings


@CrewBase
class ReportWriterCrew:
    """Report Writer specialized crew for final ESG report assembly and presentation"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def executive_summary_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["executive_summary_writer"],
            verbose=True,
            max_iter=2,
            memory=True,
        )

    @agent
    def technical_content_editor(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_content_editor"],
            verbose=True,
            max_iter=3,  # Più iterazioni per editing complesso
            memory=True,
        )

    @agent
    def data_visualization_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["data_visualization_specialist"],
            verbose=True,
            max_iter=2,
            memory=True,
        )

    @agent
    def final_report_assembler(self) -> Agent:
        return Agent(
            config=self.agents_config["final_report_assembler"],
            verbose=True,
            max_iter=2,
            memory=True,
        )

    @task
    def executive_summary_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config["executive_summary_creation_task"],
        )

    @task
    def technical_sections_editing_task(self) -> Task:
        return Task(
            config=self.tasks_config["technical_sections_editing_task"],
        )

    @task
    def data_visualization_design_task(self) -> Task:
        return Task(
            config=self.tasks_config["data_visualization_design_task"],
        )

    @task
    def final_report_assembly_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_report_assembly_task"],
            output_file="complete_esg_sustainability_report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Report Writer specialized crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # memory=True,
            # embedder=embedder_settings,
            max_rpm=20,
        )
