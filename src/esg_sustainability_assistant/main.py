#!/usr/bin/env python
from pydantic import BaseModel

import mlflow
from crewai.flow import Flow, start, listen

from esg_sustainability_assistant.crews.analisi_dati.analisi_dati import (
    ESGDataAnalystCrew,
)
from esg_sustainability_assistant.crews.compliance_advisor.compliance_advisor import (
    ESGComplianceAdvisorCrew,
)
from esg_sustainability_assistant.crews.sustainabilty_strategist.sustainability_strategist import (
    SustainabilityStrategistCrew,
)
from esg_sustainability_assistant.crews.report_writer.report_writer import (
    ReportWriterCrew,
)
from models.company_info import CompanyInfo


mlflow.crewai.autolog()
mlflow.set_experiment("ESG Sustainability Assistant")


class ESGAnalysisState(BaseModel):
    company_info: CompanyInfo = None

    website: str = ""
    benchmark_analysis: str = ""
    compliance_roadmap: str = ""
    strategic_plan: str = ""
    final_report: str = ""


class ESGSustainabilityFlow(Flow[ESGAnalysisState]):
    """
    Complete ESG analysis workflow orchestrating 4 specialized crews:
    1. Data Analysis - Benchmark and market research
    2. Compliance Mapping - Regulatory requirements and frameworks
    3. Strategic Planning - Action plans and initiatives
    4. Report Generation - Final comprehensive report
    """

    @start()
    def run_data_analysis(self):
        """Step 1: ESG Data Analysis and Benchmarking"""
        print("\n📊 STEP 1: ESG Data Analysis...")
        print("Tasks: Market research, competitor analysis, ESG benchmarking")
        print("-" * 60)

        if not hasattr(self, "data_analyst_crew") or self.data_analyst_crew is None:
            self.data_analyst_crew = ESGDataAnalystCrew()

        result = self.data_analyst_crew.crew().kickoff(
            inputs={
                "azienda_nome": self.state.company_info.name,
                "settore": self.state.company_info.industry_sector,
            }
        )

        self.state.benchmark_analysis = str(result)
        print("✅ Data analysis completed")
        return "Data analysis completed"

    @listen(run_data_analysis)
    def run_compliance_mapping(self, _):
        """Step 2: Compliance & Framework Mapping"""
        print("\n⚖️ STEP 2: Compliance & Framework Mapping...")
        print("Tasks: Regulatory mapping, standards selection, compliance roadmap")
        print("-" * 60)

        if not hasattr(self, "compliance_crew") or self.compliance_crew is None:
            self.compliance_crew = ESGComplianceAdvisorCrew()

        result = self.compliance_crew.crew().kickoff(
            inputs={
                "azienda_nome": self.state.company_info.name,
                "settore": self.state.company_info.industry_sector,
                "benchmark_analysis": self.state.benchmark_analysis,
            }
        )

        self.state.compliance_roadmap = str(result)
        print("✅ Compliance mapping completed")
        return "Compliance mapping completed"

    @listen(run_compliance_mapping)
    def run_strategic_planning(self, _):
        """Step 3: Strategic Action Planning"""
        print("\n💡 STEP 3: Strategic Action Planning...")
        print("Tasks: Initiative design, impact quantification, strategic roadmap")
        print("-" * 60)

        if not hasattr(self, "strategist_crew") or self.strategist_crew is None:
            self.strategist_crew = SustainabilityStrategistCrew()

        result = self.strategist_crew.crew().kickoff(
            inputs={
                "azienda_nome": self.state.company_info.name,
                "settore": self.state.company_info.industry_sector,
                "benchmark_analysis": self.state.benchmark_analysis,
                "compliance_roadmap": self.state.compliance_roadmap,
            }
        )

        self.state.strategic_plan = str(result)
        print("✅ Strategic planning completed")
        return "Strategic planning completed"

    @listen(run_strategic_planning)
    def generate_final_report(self, _):
        """Step 4: Final Report Creation"""
        print("\n✍️ STEP 4: Final Report Creation...")
        print("Tasks: Report synthesis, executive summary, recommendations")
        print("-" * 60)

        if not hasattr(self, "report_writer_crew") or self.report_writer_crew is None:
            self.report_writer_crew = ReportWriterCrew()

        result = self.report_writer_crew.crew().kickoff(
            inputs={
                "azienda_nome": self.state.company_info.name,
                "settore": self.state.company_info.industry_sector,
                "benchmark_analysis": self.state.benchmark_analysis,
                "compliance_roadmap": self.state.compliance_roadmap,
                "strategic_plan": self.state.strategic_plan,
            }
        )

        self.state.final_report = str(result)

        print("\n🎉 ESG ANALYSIS COMPLETE!")
        print("📄 Final report: complete_esg_sustainability_report.md")
        print("=" * 80)

        return {
            "benchmark_analysis": self.state.benchmark_analysis,
            "compliance_roadmap": self.state.compliance_roadmap,
            "strategic_action_plan": self.state.strategic_plan,
            "final_report": self.state.final_report,
        }


def kickoff():
    """Execute the complete ESG analysis flow"""
    flow = ESGSustainabilityFlow()
    return flow.kickoff()


def plot():
    """Generate flow visualization"""
    flow = ESGSustainabilityFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
