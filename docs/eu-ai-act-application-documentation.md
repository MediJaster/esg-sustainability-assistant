# ESG Sustainability Assistant - EU AI Act Application Documentation

**Application Owner**: Giorgio [giorgio@email.com]
<br>**Document Version**: v1.0.0 (2025-09-09)
<br>**Reviewers**: ESG Sustainability Assistant Team

## Key Links

-   [Code Repository](https://github.com/your-org/esg-sustainability-assistant)
-   [Deployment Pipeline](docker/Dockerfile.streamlit)
-   [API](src/api/main.py)
-   [Cloud Account](N/A)
-   [Project Management Board](N/A)
-   [Application Architecture](src/esg_sustainability_assistant/main.py)

## General Information

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1, 2, 3
<!-- info: this section covers the AI Act requirement of a description of the intended purpose, version and provider, relevant versions and updates. In Article 11, 2(d) a datasheet is required which describes all training methodologies and techniques as well as the characteristics of the training dataset, general description of the dataset, information about their provenance, scope and main characteristics, how the data was obtained and selected, labelling procedures conducted, and data cleaning methodologies deployed. -->
<p></p>
</div>

**Purpose and Intended Use**:

-   The ESG Sustainability Assistant automates the generation of ESG (Environmental, Social, Governance) reports for companies, supporting compliance, benchmarking, and strategic planning.
-   It addresses the need for efficient, standardized ESG analysis and reporting, reducing manual effort and increasing transparency.
-   Target users: sustainability officers, compliance teams, consultants, and company management.
-   KPIs: report accuracy, user feedback ratings, compliance coverage, and report generation time.
-   Ethical considerations: transparency, fairness, and avoidance of bias in ESG recommendations.
-   Prohibited uses: not for regulatory evasion, falsification of ESG data, or use in critical safety systems.
-   **Operational environment:** Runs as a web application (Streamlit frontend), with a Python backend and REST API, deployable on cloud VMs or containers.

## Risk classification

<div style="color: gray">
Prohibited Risk: EU AI Act Chapter II <a href="https://artificialintelligenceact.eu/article/5/" style="color:blue; text-decoration:underline">Article 5</a>
<br>High-Risk: EU AI Act Chapter III, Section 1 <a href="https://artificialintelligenceact.eu/article/6/" style="color:blue; text-decoration:underline">Article 6</a>, <a href="https://artificialintelligenceact.eu/article/7/" style="color:blue; text-decoration:underline">Article 7</a>  
<br>Limited Risk: Chapter IV <a href="https://artificialintelligenceact.eu/article/50/" style="color:blue; text-decoration:underline">Article 50</a>
<p></p>
</div>

<!--info: The AI Act classifies AI systems into four different risk categories. The EU AI Act categorizes AI systems into four risk levels: unacceptable, high, limited, and minimal risk, each with corresponding regulatory requirements.
Unacceptable risk (Chapter II, Article 5) includes systems that pose a clear threat to safety or fundamental rights (e.g. social scoring, recidivism scoring) and are banned.
High-risk systems are delineated in Chapter III, Section 1, Articles 6 and 7, including AI used in sensitive domains like healthcare, law enforcement, education, employment, and critical infrastructure. These must meet strict requirements and conduct conformity assessment practices, including risk management, transparency, and human oversight.
Limited-risk systems, delineated in Chapter IV Article 50, such as chatbots, must meet transparency obligations (e.g. disclosing AI use).
Minimal-risk systems, like spam filters or AI in video games, face no specific requirements. -->

-   Limited Risk (in accordance with the AI Act)
-   Reasoning: The system provides decision support and transparency tools (e.g., ESG report generation and benchmarking) but does not make autonomous decisions affecting legal rights or safety. It requires human review and approval before any action is taken.

## Application Functionality

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>, paragraph 1, 2, 3
<!-- Info: this section covers the delineation of the general purpose of the system required in Article 1, with a focus on defining what the system should do and how it should work.-->
<p></p>
</div>

-   **Instructions for use for deployers**: <div style="color: gray">(EU AI Act <a href="https://artificialintelligenceact.eu/article/13/" style="color:blue; text-decoration:underline">Article 13</a>)</div>
-   **Model Capabilities**:
    -   What the application can and cannot do (limitations).
    -   Supported languages, data types, or scenarios.
-   **Input Data Requirements**:
    -   Format and quality expectations for input data.
    -   Examples of valid and invalid inputs.
-   **Output Explanation**:
    -   How to interpret predictions, classifications, or recommendations.
    -   Uncertainty or confidence measures, if applicable.
-   **System Architecture Overview**:
    -   Functional description and architecture of the system.
    -   Describe the key components of the system (including datasets, algorithms, models, etc.)

## Models and Datasets

<div style="color: gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2 (d)
<p></p>
</div>

<!--All information about models and datasets that are used in the application should be found in their respective dataset or model documentation.  The purpose here is mainly to provide links to those documentation. -->
<!--In Article 11, 2 (d) a datasheet is required which describes all training methodologies and techniques as well as the charatcteristics of the training dataset, general description of the dataset, information about their provenance, scope and main characteristics, how the data was obtained and selected labelling procedures conducted and data cleaning methodologies deployed -->

### Models

No proprietary or custom ML models are directly integrated; the system orchestrates analysis using rule-based and workflow logic, leveraging external APIs and libraries for NLP and benchmarking where needed.

| Model   | Link to Single Source of Truth | Description of Application Usage |
| ------- | ------------------------------ | -------------------------------- |
| Model 1 | [TechOps Model Document]()     | ...                              |
| Model 2 | [TechOps Model Document]()     | ...                              |
| Model 3 | [GitHub Repo]()                | ...                              |

### Datasets

Link to all dataset documentation and information used to evaluate the AI/ML System.  
(Note, Model Documentation should also contain dataset information and links for all datasets used to train and test each respective model)

| Dataset | Link to Single Source of Truth | Description of Application Usage                                                    |
| ------- | ------------------------------ | ----------------------------------------------------------------------------------- |
| N/A     | N/A                            | No proprietary datasets; uses user-provided company info and public ESG benchmarks. |

## Deployment

-   Infrastructure and environment details (e.g., cloud setup, APIs).
-   Integration with external systems or applications.

### Infrastructure and Environment Details

-   **Cloud Setup**:
    -   Specify cloud provider (e.g., AWS, Azure, GCP) and regions.
    -   List required services: compute (e.g., EC2, Kubernetes), storage (e.g., S3, Blob Storage), and databases (e.g., DynamoDB, Firestore).
    -   Define resource configurations (e.g., VM sizes, GPU/TPU requirements).
    -   Network setup: VPC, subnets, and security groups.
-   **APIs**:
    -   API endpoints, payload structure, authentication methods (e.g., OAuth, API keys).
    -   Latency and scalability expectations.

## Integration with External Systems

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1 (b, c, d, g, h), 2 (a)
  <p></p>
</div>

-   **Systems**:
    -                         Dependencies: Python 3.10+, Streamlit, FastAPI, MLflow, Pydantic, requests, crewai.
    -                         Data flow: User → Streamlit frontend → API backend → ESG analysis flow → report output.
    -                         Error-handling: API returns error messages for invalid input or backend failures; frontend displays user-friendly errors.

## Deployment Plan

-   **Infrastructure**:
    -                         Environments: development, staging, production (via Docker Compose or cloud VM).
    -                         Scaling: stateless, can be horizontally scaled; no persistent state.
    -                         Backup/recovery: not required (stateless); logs and reports can be exported.
-   **Integration Steps**:
    -                         Deploy backend API, then frontend. No database migrations or model uploads required.
    -                         Dependencies: see requirements.txt/pyproject.toml.
    -                         Rollback: redeploy previous container/image.
-   **User Information**: where is this under deployment?

## Lifecycle Management

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 6
  <p></p>
</div>
    
* Monitoring: MLflow tracks all analysis runs, parameters, and outputs.
* Versioning: Codebase is version-controlled (Git); no model versioning required.
* **Metrics**:
  * Application: response time, error rate, user feedback ratings.
  * Infrastructure: CPU/memory usage (via cloud monitoring if deployed).
* **Key Activities**:
  * Monitor API and frontend logs.
  * Address user feedback and bug reports.
  * Update codebase as needed.
* **Documentation Needs**:
  * MLflow logs, API logs, and user feedback records.
  * Change log maintained in version control.
* Change log includes: new features, updates, deprecated/removed features, bug/security fixes.

### Risk Management System

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/9/" style="color:blue; text-decoration:underline">Article 9</a>
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>
  ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>
  <p></p>
</div>
<!--**Instructions:**  A thorough risk management system is mandated by the AI Act, especially for high-risk AI systems. This section documents the  proactive efforts to ensure the AI system operates safely and ethically. In general in this section you should document all the measures undertaken to make sure that a system operates safely on the market. Example: Consider a facial recognition system used for real-time law enforcement in public spaces. This is categorized as high-risk under the EU AI Act. If developers document the risk that the system might misidentify individuals—particularly among minority groups due to biased training data—they can plan for rigorous dataset audits, independent bias testing, and establish human oversight in decision-making. Without documenting this risk, the system might be deployed without safeguards, leading to wrongful detentions and legal liabilities. Systematic documentation ensures these issues are not only identified but addressed before harm occurs.-->

**Risk Assessment Methodology:** Risks are identified and assessed using ISO 31000 principles and regular code review. MLflow is used to trace all analysis steps for auditability.

**Identified Risks:**

-   Biased or incomplete ESG recommendations due to limited input data.
-   Privacy risks if sensitive company data is entered.
-   System downtime or API errors affecting report availability.

**Potential Harmful Outcomes:**

-   Inaccurate ESG reports leading to poor business decisions.
-   Exposure of confidential company information.
-   Misinterpretation of recommendations without human oversight.

**Likelihood and Severity:**

-   Likelihood: Low to moderate (requires user input and review).
-   Severity: Moderate (impacts business decisions, not safety-critical).

#### Risk Mitigation Measures

**Preventive Measures:** Input validation, user review of all outputs, transparency in report generation, and regular code audits.

**Protective Measures:** API error handling, user feedback loop, and ability to update/patch the system rapidly.

## Testing and Validation (Accuracy, Robustness, Cybersecurity)

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/15/" style="color:blue; text-decoration:underline">Article 15</a>
  <p></p>
</div>

**Testing and Validation Procedures (Accuracy):**

-   Unit and integration tests for API and workflow logic.
-   Manual validation of generated reports.
-   User feedback is collected and reviewed for continuous improvement.

**Performance Metrics:** User feedback ratings, report generation time, API error rate.

**Validation Results:** Reports are validated against known ESG benchmarks and expert review; user feedback is monitored for quality.

**Measures for Accuracy:** Input validation, workflow traceability (MLflow), and user review.

### Accuracy throughout the lifecycle

**Data Quality and Management:** All input data is user-provided and validated for completeness and correctness.

**Model Selection and Optimisation:** No ML model selection; workflow logic is modular and can be updated as needed.

**Feedback Mechanisms:** User feedback is collected via the frontend and API for continuous improvement.

### Robustness

<-- Add outlier detection and all possible post analysis, what are the criticalities -->

**Robustness Measures:**

-   Error handling, modular workflow, and user review ensure robustness.

**Scenario-Based Testing:**

-   Handles invalid input gracefully; errors are surfaced to the user.

**Redundancy and Fail-Safes:**

-   System is stateless; can be restarted or redeployed without data loss.

**Uncertainty Estimation:**

-   No explicit uncertainty quantification; user review is required for all outputs.

### Cybersecurity

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2 (h)
  <p></p>
</div>

**Data Security:**

-   No sensitive data stored; all processing is in-memory.
-   Recommend deploying behind secure HTTPS endpoints.

**Access Control:**

-   No authentication by default; recommend API gateway or reverse proxy for production.

**Incident Response :**

-   Monitor logs for errors; patch and redeploy as needed.

These measures include threat modelling, data security, adversarial robustness, secure development practices, access control, and incident response mechanisms.

Post-deployment monitoring, patch management, and forensic logging are crucial to maintaining ongoing cybersecurity compliance.

Documentation of all cybersecurity processes and incidents is mandatory to ensure accountability and regulatory conformity.

## Human Oversight

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>;; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2(e)
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/14/" style="color:blue; text-decoration:underline">Article 14</a>
  <p></p>
</div>

<!-- info: AI Act Article 11, paragraph 2(e) requirements: assessment of the human oversight measures needed in accordance with Article 14, including the assessment of the technical measures needed to facilitate the integration of the outputs of the AI systems by deployers. -->

**Human-in-the-Loop Mechanisms:** All ESG reports require human review and approval before use in decision-making.

**Override and Intervention Procedures:** Users can disregard or override any report output; system can be stopped or redeployed at any time.

**User Instructions and Training:** User guide provided in documentation; intuitive Streamlit interface for input and feedback.

**Limitations and Constraints of the System:** Cannot guarantee regulatory compliance or replace expert judgment; limited by input data quality.

## Incident Management

<!-- what happens when things go wrong. This part is particularly important to provide information on how incidents were dealth with and the processes put in place to minimize damage when things go wrong. -->

-   **Common Issues**:
    -   Invalid input data (missing fields, wrong types): Ensure all required fields are present and correctly formatted in API requests.
    -   API errors or timeouts: Check backend logs for stack traces and error messages; verify that all services are running.
-   **Support Contact**:
    -   Technical support: Giorgio Caddeo (giorgio@email.com)
    -   Community: [GitHub Issues](https://github.com/your-org/esg-sustainability-assistant/issues)
    -   How to reach technical support or community forums.

### Troubleshooting AI Application Deployment

This section outlines potential issues during deployment and their mitigation strategies for the ESG Sustainability Assistant.

#### Infrastructure-Level Issues

##### Insufficient Resources

-   **Problem**: Application crashes or slow performance due to insufficient CPU/memory.
-   **Mitigation**: Monitor resource usage; scale containers/VMs as needed; use cloud auto-scaling if available.

##### Network Failures

-   **Problem**: Frontend cannot reach backend API or external services.
-   **Mitigation**: Check network/firewall settings; ensure correct API URLs; use health checks and retry logic.

##### Deployment Pipeline Failures

-   **Problem**: Build or deployment fails due to misconfiguration or missing dependencies.
-   **Mitigation**: Validate Docker and environment configs; use CI/CD with clear error logs; roll back to last working version.

#### Integration Problems

##### API Failures

-   **Problem**: API endpoints return errors or are unreachable.
-   **Mitigation**: Check backend logs; validate input data; ensure backend is running and accessible.

##### Data Format Mismatches

-   **Problem**: Errors due to unexpected or invalid input data.
-   **Mitigation**: Validate input against API schema; use example payloads from documentation.

#### Data Quality Problems

-   **Problem**: Poor or incomplete input data leads to low-quality reports.
-   **Mitigation**: Require all mandatory fields; validate data before submission.

#### Model-Level Issues

-   **Not applicable**: No proprietary ML models are deployed in this project.

#### Safety and Security Issues

##### Unauthorised Access

-   **Problem**: API exposed without authentication.
-   **Mitigation**: Deploy behind API gateway or reverse proxy; use HTTPS.

##### Data Breaches

-   **Problem**: Sensitive data exposure.
-   **Mitigation**: Do not store sensitive data; process all data in-memory; restrict access to deployment.

#### Monitoring and Logging Failures

##### Missing or Incomplete Logs

-   **Problem**: Lack of logs for debugging.
-   **Mitigation**: Ensure logging is enabled for all services; use MLflow and container logs.

#### Recovery and Rollback

##### Rollback Mechanisms

-   **Problem**: New deployment introduces errors.
-   **Mitigation**: Use versioned Docker images; roll back to previous version if needed.

##### Disaster Recovery

-   **Problem**: Complete system outage.
-   **Mitigation**: Redeploy containers/VMs from source; no persistent data to restore.

This section outlines potential issues that can arise during the deployment of an AI application, along with their causes, resolutions, and best practices for mitigation.

#### Infrastructure-Level Issues

##### Insufficient Resources

-   **Problem**: Inaccurate resource estimation for production workloads.

    -   Unexpected spikes in user traffic can lead to insufficient resources such as compute, memory or storage that can lead to crashes and bad performance

-   **Mitigation Strategy**:
<!-- describe here the resolution strategy such as:

*   Enable autoscaling (e.g., Kubernetes Horizontal Pod Autoscaler).
*   Monitor usage metrics and adjust resource allocation dynamically.
*   Implement rate-limiting for traffic spikes. -->

##### Network Failures

-   **Problem**: network bottlenecks can lead to inaccessible or experiences latency of the application.

-   **Mitigation Strategy**:
<!--
-   Test network connectivity
-   Use content delivery networks (CDNs) or regional load balancers.
-   Ensure proper failover mechanisms.-->

##### Deployment Pipeline Failures

-   **Problem**: pipeline fails to build, test, or deploy because of issues of compatibility between application code and infrastructure, environment variables or credentials misconfiguration.

-   **Mitigation Strategy**:
<!--:
-   Roll back to the last stable build.
-   Fix pipeline scripts and use containerisation for environment consistency.
-   Enable verbose logging for error diagnostics.-->

#### Integration Problems

##### API Failures

-   **Problem**: External APIs or internal services are unreachable due to network errors or authentication failures.

-   **Mitigation Strategy**:
<!--:
-   Implement retries with exponential backoff.
-   Validate API keys or tokens and refresh as needed.
-   Log and monitor API responses for debugging. -->

##### Data Format Mismatches

-   **Problem**: Crashes or errors due to unexpected data formats such as changes in the schema of external data sources or missing data validation steps.

-   **Mitigation Strategy**:

<!--
  - Use schema validation tools (e.g., JSON schema validators).
  - Add versioning to APIs and validate inputs before processing.-->

#### Data Quality Problems

-   **Problem**: Inaccurate or corrupt data leads to poor predictions.
-   **Causes**:

    -   No data validation or cleaning processes.
    -   Inconsistent labelling in training datasets.

-   **Mitigation Strategy**:
<!--

*   **Resolution**:
    -   Automate data quality checks (e.g., Great Expectations framework).
    -   Regularly audit and clean production data.-->

#### Model-Level Issues

##### Performance or Deployment Issues

-   **Problem**: Incorrect or inconsistent results due to data drift or inadequate training data for the real world deployment domain.

-   **Mitigation Strategy**:

<!--
- **Resolution**:
  - Monitoring for data drift and retraining of the model as needed.
  - Regularly update the model -->

#### Safety and Security Issues

##### Unauthorised Access

-   **Problem**: Sensitive data or APIs are exposed due to misconfigured authentication and authorization.

##### Data Breaches

-   **Problem**: User or model data is compromised due to insecure storage or lack of monitoring and logging of data access.

-   **Mitigation Strategy**:
<!--

*   **Resolution**:
    -   Use secure storage services (e.g., AWS KMS).
    -   Implement auditing for data access and alerts for unusual activity.
        6.1. Delayed or Missing Data-->

#### Monitoring and Logging Failures

##### Missing or Incomplete Logs

-   **Problem**: Lack of information to debug issues due to inefficient logging. Critical issues go unnoticed, or too many false positives occur by lack of implementation ofactionable information in alerts.

-   **Mitigation Strategy**:

<!--
- **Resolution**:
  - Fine-tune alerting thresholds and prioritise critical alerts.
  - Use tools like Prometheus Alertmanager to manage and group alerts. -->

#### Recovery and Rollback

##### Rollback Mechanisms

-   **Problem**: New deployment introduces critical errors.

-   **Mitigation Strategy**:

<!--
- **Resolution**:
  - Use blue-green or canary deployments to minimise impact.
  - Maintain backups of previous versions and configurations. -->

##### Disaster Recovery

-   **Problem**: Complete system outage or data loss.

-   **Mitigation Strategy**:

<!--
- **Resolution**:
  - Test and document disaster recovery plans.
  - Use automated backups and verify restore procedures.-->

### EU Declaration of conformity

Not applicable. The ESG Sustainability Assistant is not certified under EU conformity assessment procedures and does not process personal data requiring such declaration. If certification is pursued in the future, this section will be updated accordingly.

<div style="color: gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/47/" style="color:blue; text-decoration:underline">Article 47</a>
  <p></p>
</div>

<!-- when applicable and certifications are available: it requires a systems name as well as the name and address of the provider; a statement that the EU declaration of conformity referred to in Article 47 is issued under the sole responsibility of the provider; a statement that the AI system is in conformity with this Regulation and, if applicable, with any other relevant Union law that provides for the issuing of the EU declaration of conformity referred to in Article 47, Where an AI system involves the processing of personal data;  a statement that that AI system complies with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, reference to the harmonised standards used or any other common specification in relation to which
conformity is declared; the name and identification number of the notified body, a description of the conformity
assessment procedure performed, and identification of the certificate issued; the place and date of issue of the declaration, the name and function of the person who signed it, as well as an
indication for, or on behalf of whom, that person signed, a signature.-->

### Standards applied

-   ISO 31000 (Risk Management Principles, for risk assessment methodology)
-   Pydantic (data validation)
-   MLflow (experiment tracking and traceability)
-   Docker (containerization best practices)
-   EU AI Act (regulatory alignment)

<!-- Document here the standards and frameworks used-->

## Documentation Metadata

### Template Version

-   Based on [EU AI Act Model Documentation Template](https://github.com/your-org/eu-ai-act-template) v1.0.0

<!-- info: link to model documentation template (i.e. could be a GitHub link) -->

### Documentation Authors

-   Giorgio, ESG Sustainability Assistant Team: Contributor

<!-- info: Give documentation authors credit

Select one or more roles per author and reference author's
emails to ease communication and add transparency. -->

-   **Nicolò Resta, ESG Sustainability Assistant Team:** (Owner)
-   **Cherki Meziane, ESG Sustainability Assistant Team:** (Contributor)
-   **Giorgio Caddeo, ESG Sustainability Assistant Team:** (Contributor)
