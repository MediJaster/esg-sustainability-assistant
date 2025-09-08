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


mlflow.crewai.autolog(log_traces=True, silent=False)
mlflow.litellm.autolog(log_traces=True, silent=False)

mlflow.set_experiment("ESG Sustainability Assistant")


class ESGAnalysisState(BaseModel):
    # Provide a default CompanyInfo for testing if none is set
    company_info: CompanyInfo = CompanyInfo(
        name="Ernst & Young", industry_sector="Consultancy"
    )
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
        import mlflow

        print("\n📊 STEP 1: ESG Data Analysis...")
        print("Tasks: Market research, competitor analysis, ESG benchmarking")
        print("-" * 60)

        with mlflow.start_run(run_name="Data Analysis", nested=True):
            mlflow.log_param("step", "data_analysis")
            mlflow.log_param("azienda_nome", self.state.company_info.name)
            mlflow.log_param("settore", self.state.company_info.industry_sector)

            if not hasattr(self, "data_analyst_crew") or self.data_analyst_crew is None:
                self.data_analyst_crew = ESGDataAnalystCrew()

            result = self.data_analyst_crew.crew().kickoff(
                inputs={
                    "azienda_nome": self.state.company_info.name,
                    "settore": self.state.company_info.industry_sector,
                }
            )

            self.state.benchmark_analysis = str(result)
            mlflow.log_param(
                "benchmark_analysis",
                self.state.benchmark_analysis
                if len(str(self.state.benchmark_analysis)) < 500
                else str(self.state.benchmark_analysis)[:500] + "...",
            )
            print("✅ Data analysis completed")
        return "Data analysis completed"

    @listen(run_data_analysis)
    def run_compliance_mapping(self, _):
        """Step 2: Compliance & Framework Mapping"""
        import mlflow

        print("\n⚖️ STEP 2: Compliance & Framework Mapping...")
        print("Tasks: Regulatory mapping, standards selection, compliance roadmap")
        print("-" * 60)

        with mlflow.start_run(run_name="Compliance Mapping", nested=True):
            mlflow.log_param("step", "compliance_mapping")
            mlflow.log_param("azienda_nome", self.state.company_info.name)
            mlflow.log_param("settore", self.state.company_info.industry_sector)
            mlflow.log_param(
                "benchmark_analysis",
                self.state.benchmark_analysis
                if len(str(self.state.benchmark_analysis)) < 500
                else str(self.state.benchmark_analysis)[:500] + "...",
            )

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
            mlflow.log_param(
                "compliance_roadmap",
                self.state.compliance_roadmap
                if len(str(self.state.compliance_roadmap)) < 500
                else str(self.state.compliance_roadmap)[:500] + "...",
            )
            print("✅ Compliance mapping completed")
        return "Compliance mapping completed"

    @listen(run_compliance_mapping)
    def run_strategic_planning(self, _):
        """Step 3: Strategic Action Planning"""
        import mlflow

        print("\n💡 STEP 3: Strategic Action Planning...")
        print("Tasks: Initiative design, impact quantification, strategic roadmap")
        print("-" * 60)

        with mlflow.start_run(run_name="Strategic Planning", nested=True):
            mlflow.log_param("step", "strategic_planning")
            mlflow.log_param("azienda_nome", self.state.company_info.name)
            mlflow.log_param("settore", self.state.company_info.industry_sector)
            mlflow.log_param(
                "benchmark_analysis",
                self.state.benchmark_analysis
                if len(str(self.state.benchmark_analysis)) < 500
                else str(self.state.benchmark_analysis)[:500] + "...",
            )
            mlflow.log_param(
                "compliance_roadmap",
                self.state.compliance_roadmap
                if len(str(self.state.compliance_roadmap)) < 500
                else str(self.state.compliance_roadmap)[:500] + "...",
            )

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
            mlflow.log_param(
                "strategic_plan",
                self.state.strategic_plan
                if len(str(self.state.strategic_plan)) < 500
                else str(self.state.strategic_plan)[:500] + "...",
            )
            print("✅ Strategic planning completed")
        return "Strategic planning completed"

    @listen(run_strategic_planning)
    def generate_final_report(self, _):
        """Step 4: Final Report Creation"""
        import mlflow

        print("\n✍️ STEP 4: Final Report Creation...")
        print("Tasks: Report synthesis, executive summary, recommendations")
        print("-" * 60)

        with mlflow.start_run(run_name="Final Report", nested=True):
            mlflow.log_param("step", "final_report")
            mlflow.log_param("azienda_nome", self.state.company_info.name)
            mlflow.log_param("settore", self.state.company_info.industry_sector)
            mlflow.log_param(
                "benchmark_analysis",
                self.state.benchmark_analysis
                if len(str(self.state.benchmark_analysis)) < 500
                else str(self.state.benchmark_analysis)[:500] + "...",
            )
            mlflow.log_param(
                "compliance_roadmap",
                self.state.compliance_roadmap
                if len(str(self.state.compliance_roadmap)) < 500
                else str(self.state.compliance_roadmap)[:500] + "...",
            )
            mlflow.log_param(
                "strategic_plan",
                self.state.strategic_plan
                if len(str(self.state.strategic_plan)) < 500
                else str(self.state.strategic_plan)[:500] + "...",
            )

            if (
                not hasattr(self, "report_writer_crew")
                or self.report_writer_crew is None
            ):
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
            mlflow.log_param(
                "final_report",
                self.state.final_report
                if len(str(self.state.final_report)) < 500
                else str(self.state.final_report)[:500] + "...",
            )

            print("\n🎉 ESG ANALYSIS COMPLETE!")
            print("📄 Final report: complete_esg_sustainability_report.md")
            print("=" * 80)

        return {
            "benchmark_analysis": self.state.benchmark_analysis,
            "compliance_roadmap": self.state.compliance_roadmap,
            "strategic_action_plan": self.state.strategic_plan,
            "final_report": self.state.final_report,
            "trace_id": mlflow.get_active_trace_id(),
        }


def kickoff():
    """Execute the complete ESG analysis flow with full mlflow tracing"""
    import mlflow

    with mlflow.start_run(run_name="ESG Full Analysis", nested=False) as parent_run:
        mlflow.log_param("company_name", "Ernst & Young")
        mlflow.log_param("industry_sector", "Consultancy")
        flow = ESGSustainabilityFlow()
        result = flow.kickoff()
        # Log final outputs as artifacts or params
        if isinstance(result, dict):
            for k, v in result.items():
                mlflow.log_param(k, v if len(str(v)) < 500 else str(v)[:500] + "...")
        return result


def plot():
    """Generate flow visualization"""
    flow = ESGSustainabilityFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()
