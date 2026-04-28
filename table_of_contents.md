# CompTIA SecurityX (CAS-005) Textbook Table of Contents

This document outlines the detailed pedagogical structure for a 12-chapter textbook covering the CompTIA SecurityX (CAS-005) exam objectives. 
Sections are phrased as questions, subsections are concise, and each chapter includes designated spots for Historical Case Studies, Fictional Scenarios, Diagrams, and Tables. Every chapter follows the standard bookend structure of Introduction and Review/Conclusion, and includes specific Learning Outcomes mapped to Bloom's Taxonomy.

---

### Part I: Foundations of Security Governance & Risk

#### Chapter 1: Security Governance, Compliance, and Ethics
*Maps to Objectives: 1.1, 1.3*

**Learning Outcomes:**
1. **Define** the components of a comprehensive security program documentation suite.
2. **Design** a security awareness and training program tailored to organizational needs.
3. **Compare** and contrast industry-standard governance frameworks such as COBIT and ITIL.
4. **Implement** data governance strategies across staging and production environments.
5. **Evaluate** the impact of industry-specific compliance standards (Healthcare, Financial, etc.) on security strategies.
6. **Analyze** cross-jurisdictional compliance requirements, including GDPR, CCPA, and data sovereignty.
7. **Integrate** privacy regulations and reporting frameworks into organizational security policies.
8. **Assess** the effectiveness of governance risk and compliance (GRC) tools in automating compliance tracking.

**Chapter Outline:**
- **Introduction**
- **Why is Governance the Foundation of Security?**
  - Policies, Procedures, Standards, and Guidelines
  - *Table:* Comparing Policies, Standards, Procedures, and Guidelines
  - RACI Matrices and Management Commitment
  - *Diagram:* The Governance Documentation Hierarchy
  - *Diagram:* Example RACI Matrix for Incident Response
- **How Do We Build a Culture of Security Awareness?**
  - Phishing and Social Engineering
  - Operational Security
  - *Fictional Case Study:* Snow White (GRC Analyst at Seven Dwarfs Mining) establishes a security awareness training program.
- **Which Governance Frameworks Matter Most?**
  - COBIT vs. ITIL
  - Data Governance in Staging and Production
  - *Table:* Comparing Major IT Governance Frameworks
- **How Does Compliance Shape Security Strategy?**
  - Industry Standards (PCI DSS, ISO 27000)
  - Privacy Regulations (GDPR, CCPA)
  - *Historical Case Study:* Meta GDPR Fine (€1.2 Billion Data Transfer Ruling) 
- **Chapter Review and Conclusion**

#### Chapter 2: Risk Management and Threat Modeling
*Maps to Objectives: 1.2, 1.4*

**Learning Outcomes:**
1. **Conduct** impact analyses using quantitative and qualitative risk assessment methodologies.
2. **Formulate** strategies for third-party risk management, including supply chain and vendor risks.
3. **Evaluate** availability, confidentiality, and integrity risk considerations within business continuity planning.
4. **Design** a crisis management and breach response plan.
5. **Differentiate** between threat actor characteristics (motivation, resources, capabilities).
6. **Apply** industry frameworks (MITRE ATT&CK, Cyber Kill Chain, STRIDE) to threat-modeling activities.
7. **Determine** an organization's attack surface through architecture reviews and enumeration discovery.
8. **Assess** the applicability of threats to organizations with and without existing systems in place.

**Chapter Outline:**
- **Introduction**
- **How Do We Measure and Prioritize Risk?**
  - Quantitative vs. Qualitative Analysis
  - *Diagram:* The Risk Assessment Workflow
  - Risk Appetite and Tolerance
  - *Table:* Quantitative vs. Qualitative Risk Metrics
  - *Fictional Case Study:* Fitzwilliam Darcy (Director of Risk Management) calculates SLE and ALE for Derbyshire Holdings.
- **Who Are Our Adversaries?**
  - Threat Actor Motivations and Resources
  - *Table:* Threat Actor Characteristics (Nation-State, Hacktivist, Insider)
  - Supply Chain and Vendor Risk
  - *Historical Case Study:* The Target HVAC Vendor Breach (Third-Party Supply Chain)
- **How Do We Model Threats Effectively?**
  - Frameworks: MITRE ATT&CK, STRIDE, and Cyber Kill Chain
  - Determining the Attack Surface
  - *Diagram:* Visualizing the Cyber Kill Chain
- **What is the Plan for the Worst-Case Scenario?**
  - Crisis Management and Breach Response
  - BCDR and Availability Risk
  - *Diagram:* BCDR Planning Lifecycle
- **Chapter Review and Conclusion**

#### Chapter 3: Navigating Emerging Threats: AI and the Evolving Landscape
*Maps to Objectives: 1.5*

**Learning Outcomes:**
1. **Summarize** the legal, ethical, and privacy implications of organizational AI adoption.
2. **Analyze** threats specific to AI models, including prompt injection, data poisoning, and model inversion.
3. **Evaluate** the risks associated with AI-enabled attacks such as deepfakes and automated exploit generation.
4. **Formulate** guardrails and DLP strategies for the use of AI-enabled assistants and digital workers.
5. **Assess** the risks of sensitive information disclosure and excessive agency in AI systems.
6. **Design** organizational policies to safely govern the use of generative AI tools.
7. **Evaluate** the impact of explainable versus non-explainable AI models on security investigations.

**Chapter Outline:**
- **Introduction**
- **What Are the Security Implications of AI Adoption?**
  - Legal, Ethical, and Privacy Concerns
  - Explainable vs. Non-Explainable Models
  - *Diagram:* The AI/ML Development Pipeline and Trust Boundaries
  - *Fictional Case Study:* Count Dracula (CISO at Transylvanian Blood Bank) mitigating excessive agency in a medical AI system.
- **How Are Adversaries Weaponizing AI?**
  - Deepfakes and Digital Interactivity
  - Automated Exploit Generation
  - *Diagram:* Deepfake Generation Workflow vs. Detection
  - *Historical Case Study:* 2019 UK Energy Firm Deepfake CEO Voice Fraud
- **How Do We Protect AI Models from Attack?**
  - Prompt Injection and Data Poisoning
  - Model Theft and Inversion
  - *Table:* AI Threats vs. Traditional Software Threats
- **How Can We Safely Govern AI in the Enterprise?**
  - Guardrails for AI Assistants
  - Data Loss Prevention (DLP) for LLMs
  - *Table:* Enterprise AI Acceptable Use Guidelines
- **Chapter Review and Conclusion**

---

### Part II: Designing Secure Architectures

#### Chapter 4: Principles of Security Architecture and Zero Trust
*Maps to Objectives: 2.1, 2.3, 2.6*

**Learning Outcomes:**
1. **Analyze** security requirements to determine optimal component placement.
2. **Design** systems that incorporate load balancing, recoverability, and geographic considerations.
3. **Integrate** Zero Trust concepts into system designs.
4. **Architect** network segmentation and microsegmentation strategies.
5. **Apply** deperimeterization concepts such as SASE and SD-WAN.
6. **Design** information and data security models, including classification, labeling, and tagging strategies.
7. **Implement** Data Loss Prevention (DLP) controls for data at rest and in transit.
8. **Evaluate** the effectiveness of security controls using assessments, scanning, and metrics.

**Chapter Outline:**
- **Introduction**
- **How Do We Architect Resilient Systems?**
  - Component Placement (Firewalls, WAFs, Proxies)
  - Load Balancing and Scaling
  - *Diagram:* High-Availability Enterprise Network Architecture
  - *Diagram:* Active-Active vs. Active-Passive Load Balancing
- **What Does Zero Trust Actually Mean?**
  - Deperimeterization and Continuous Authorization
  - Defining Subject-Object Relationships
  - *Table:* Traditional Perimeter vs. Zero Trust Architecture
  - *Fictional Case Study:* Prospero (Network Architect at Milan Island Telecom) implements SASE for a remote workforce.
- **How Do We Enforce Security Boundaries?**
  - Microsegmentation and SASE
  - Software-Defined Networking (SDN)
  - *Historical Case Study:* Google BeyondCorp (Shifting to Zero Trust Architecture)
  - *Table:* Physical vs. Logical Security Boundaries
- **How Do We Protect Data at Scale?**
  - Classification, Labeling, and Tagging
  - DLP at Rest and in Transit
  - *Diagram:* DLP Implementation Across Network Layers
- **Chapter Review and Conclusion**

#### Chapter 5: Identity and Access Management Architecture and Engineering
*Maps to Objectives: 2.4, 3.1*

**Learning Outcomes:**
1. **Design** robust provisioning and deprovisioning workflows.
2. **Implement** advanced access control models such as ABAC, MAC, DAC, and RBAC.
3. **Architect** federation, SSO, and conditional access systems using modern identity providers.
4. **Troubleshoot** common subject access control issues for users, processes, devices, and services.
5. **Manage** secrets effectively, including the rotation and deletion of tokens, certificates, passwords, and keys.
6. **Analyze** and resolve issues with authentication protocols.
7. **Apply** endpoint privilege management and privileged access management (PAM) solutions.
8. **Troubleshoot** IAM components across cloud and on-premises environments.

**Chapter Outline:**
- **Introduction**
- **How Do We Manage the Identity Lifecycle?**
  - Provisioning and Deprovisioning
  - Federation and SSO
  - *Diagram:* Federated Identity and SSO Workflow (SAML/OIDC)
  - *Fictional Case Study:* Emma Woodhouse (IAM Specialist at Highbury Networks) rapidly revoking access during an offboarding crisis.
- **Which Access Control Model is Right for the Job?**
  - ABAC, MAC, DAC, and RBAC
  - Conditional Access and Geographic Location
  - *Table:* Access Control Models Comparison
  - *Diagram:* Biometric Authentication Process Flow
- **How Do We Secure High-Privilege Accounts?**
  - Privileged Access Management (PAM)
  - Secrets Management and Credential Rotation
  - *Historical Case Study:* SolarWinds and the Golden SAML Attack
- **How Do We Troubleshoot Authentication Failures?**
  - Resolving SAML, OAuth, and Kerberos Issues
  - Investigating Biometric and MFA Anomalies
  - *Table:* SAML vs. OAuth vs. OpenID Connect
- **Chapter Review and Conclusion**

#### Chapter 6: Secure Systems Lifecycle and Hardware Assurance
*Maps to Objectives: 2.2, 3.4*

**Learning Outcomes:**
1. **Define** functional and non-functional security requirements during the early stages of the systems life cycle.
2. **Implement** software assurance testing techniques, including SAST, DAST, IAST, and RASP.
3. **Design** continuous integration and continuous deployment (CI/CD) pipelines with integrated security checks.
4. **Evaluate** supply chain risk management strategies for both software and hardware.
5. **Implement** hardware roots of trust, including TPMs, HSMs, and vTPMs.
6. **Assess** security coprocessors and secure enclaves to protect sensitive computation.
7. **Design** self-healing hardware mechanisms and tamper detection countermeasures.
8. **Evaluate** threat-actor tactics targeting firmware, memory, and electromagnetic interfaces.

**Chapter Outline:**
- **Introduction**
- **How Do We Bake Security into the SDLC?**
  - Functional vs. Non-Functional Requirements
  - Trade-offs Between Security and Usability
  - *Diagram:* Integrating Security into the CI/CD Pipeline
- **What Are the Best Tools for Software Assurance?**
  - SAST, DAST, IAST, and RASP
  - Software Composition Analysis and SBoMs
  - *Table:* When to Use SAST, DAST, and RASP
  - *Historical Case Study:* Log4Shell and the Importance of SBoMs
- **How Do We Establish Hardware Roots of Trust?**
  - TPMs, HSMs, and vTPMs
  - Secure Enclaves and Coprocessors
  - *Table:* Hardware vs. Software Roots of Trust
  - *Fictional Case Study:* Victor Frankenstein (Bio-Tech Security Engineer at Geneva Labs) auditing embedded IoT hardware.
- **How Do We Defend Against Hardware-Level Attacks?**
  - Firmware Tampering (BIOS/UEFI)
  - Memory and EMI Exploitation
  - *Diagram:* Secure Boot and Measured Boot Process
- **Chapter Review and Conclusion**

#### Chapter 7: Enterprise Cloud and Hybrid Security
*Maps to Objectives: 2.5*

**Learning Outcomes:**
1. **Design** secure cloud architectures utilizing Cloud Access Security Brokers (CASBs).
2. **Apply** the shared responsibility model to cloud infrastructure security.
3. **Implement** container security and orchestration controls in cloud environments.
4. **Architect** secure serverless workloads, functions, and resources.
5. **Design** API security mechanisms including authorization, logging, and rate limiting.
6. **Evaluate** cloud data security considerations, including exposure, leakage, and data remanence.
7. **Formulate** customer-to-cloud connectivity strategies for hybrid infrastructures.
8. **Implement** proactive, detective, and preventative cloud control strategies.

**Chapter Outline:**
- **Introduction**
- **Who is Responsible for Cloud Security?**
  - The Shared Responsibility Model
  - Customer-Managed vs. Cloud-Managed Keys
  - *Diagram:* The Cloud Shared Responsibility Model (IaaS/PaaS/SaaS)
  - *Table:* Security Responsibilities by Cloud Service Model
- **How Do We Secure Cloud Workloads and Containers?**
  - Container Orchestration Security
  - Serverless Functions and Resources
  - *Table:* Security Controls for Containers vs. Serverless
  - *Fictional Case Study:* Dorothy Gale (Cloud Architect at Emerald City Solutions) securing a sprawling serverless architecture.
- **How Do We Govern Cloud Access and APIs?**
  - CASBs and Shadow IT Detection
  - API Authorization and Rate Limiting
  - *Diagram:* API Gateway Architecture
  - *Historical Case Study:* The Capital One AWS SSRF Breach
- **How Do We Protect Cloud Data?**
  - Data Exposure and Remanence
  - Customer-to-Cloud Connectivity
- **Chapter Review and Conclusion**

---

### Part III: Security Engineering and Applied Cryptography

#### Chapter 8: Cryptography and Public Key Infrastructure
*Maps to Objectives: 3.7, 3.8*

**Learning Outcomes:**
1. **Architect** a Public Key Infrastructure (PKI).
2. **Evaluate** the impact of post-quantum cryptography (PQC).
3. **Analyze** advanced cryptographic concepts, including key stretching, key splitting, and homomorphic encryption.
4. **Apply** cryptographic techniques to secure data at rest, in transit, and in use.
5. **Implement** envelope encryption and hardware acceleration.
6. **Design** certificate-based and passwordless authentication mechanisms.
7. **Formulate** data sanitization, anonymization, and tokenization strategies.
8. **Evaluate** the use cases for immutable databases, blockchain, and secure multiparty computation.

**Chapter Outline:**
- **Introduction**
- **How Do We Architect a Robust PKI?**
  - Certificate Authorities and Registration
  - Certificate Extensions and OCSP Stapling
  - *Diagram:* The PKI Certificate Issuance and Validation Process
  - *Table:* Types of Digital Certificates
- **How Do We Apply Cryptography in the Real World?**
  - Data at Rest, in Transit, and in Use
  - Code Signing and Software Provenance
  - *Table:* Symmetric vs. Asymmetric Cryptography Use Cases
  - *Fictional Case Study:* The Mad Hatter (Lead Cryptographer at Teatime Tech) preventing an outage due to an expired root certificate.
- **What Are Advanced Cryptographic Concepts?**
  - Envelope Encryption and Hardware Acceleration
  - Key Stretching and Splitting
  - *Historical Case Study:* The DigiNotar Certificate Authority Compromise
  - *Diagram:* The TLS Handshake Explained
- **How Will Quantum Computing Change Cryptography?**
  - Post-Quantum Cryptography (PQC)
  - Resistance to Decryption Attacks
- **Chapter Review and Conclusion**

#### Chapter 9: Network, Endpoint, and Infrastructure Engineering
*Maps to Objectives: 3.2, 3.3*

**Learning Outcomes:**
1. **Analyze** requirements to enhance the security of endpoints using EDR, anti-malware, and host-based firewalls.
2. **Troubleshoot** complex network misconfigurations, including routing errors, switching errors, and VPN issues.
3. **Resolve** IPS/IDS issues related to rule misconfigurations, placement, and false positives/negatives.
4. **Investigate** and mitigate DNS security vulnerabilities, including DNS poisoning and zone transfers.
5. **Troubleshoot** Transport Layer Security (TLS) errors, cipher mismatches, and PKI integration issues.
6. **Implement** email security protocols, including DKIM, SPF, DMARC, and S/MIME.
7. **Mitigate** DoS and DDoS attacks targeting network and application resources.
8. **Manage** and secure mobile devices using MDM technologies and browser isolation.

**Chapter Outline:**
- **Introduction**
- **How Do We Lock Down Endpoints and Servers?**
  - EDR, Anti-Malware, and Host Firewalls
  - Browser Isolation and Configuration Management
  - *Table:* Endpoint Protection Features Comparison
  - *Diagram:* EDR Architecture vs. Traditional Antivirus
- **How Do We Troubleshoot Network Defenses?**
  - Resolving IPS/IDS False Positives
  - Correcting Routing and Switching Errors
  - *Historical Case Study:* WannaCry Ransomware (Network Propagation and Unpatched Systems)
- **How Do We Secure Core Network Services?**
  - DNS Security (DNSSEC, Sinkholing)
  - Email Security (DKIM, SPF, DMARC)
  - *Diagram:* How SPF, DKIM, and DMARC Prevent Email Spoofing
  - *Table:* Common Email Attack Types and Mitigations
- **How Do We Manage Mobile and Remote Devices?**
  - MDM Technologies and App Containment
  - *Fictional Case Study:* Juliet Capulet executing a BYOD MDM rollout at Verona Health.
- **Chapter Review and Conclusion**

#### Chapter 10: Securing Specialized, OT, and Legacy Systems
*Maps to Objectives: 3.5*

**Learning Outcomes:**
1. **Analyze** the security requirements of Operational Technology (OT), including SCADA, ICS, and HVAC systems.
2. **Design** security controls for Internet of Things (IoT), System-on-Chip (SoC), and embedded systems.
3. **Implement** security measures for wireless and radio frequency (RF) technologies.
4. **Formulate** segmentation, monitoring, and hardening strategies for highly constrained environments.
5. **Evaluate** industry-specific challenges in securing specialized systems (Utilities, Healthcare, Manufacturing).
6. **Design** compensating controls for obsolete, unsupported, and legacy systems.
7. **Assess** the environmental, regulatory, and safety implications of securing OT and legacy infrastructure.

**Chapter Outline:**
- **Introduction**
- **How is OT Different from IT?**
  - SCADA, ICS, and HVAC Systems
  - Safety and Environmental Constraints
  - *Table:* IT Security vs. OT Security vs. IoT Security Constraints
  - *Fictional Case Study:* Nick Chopper (OT Engineer at Yellow Brick Manufacturing) establishing air-gaps for legacy assembly lines.
- **How Do We Secure IoT and Embedded Systems?**
  - System-on-Chip (SoC) and RF Technologies
  - Wireless Security Considerations
  - *Diagram:* Purdue Model for ICS Security Architecture
  - *Diagram:* Segmenting a Corporate Wireless Network
- **What Are the Industry-Specific Infrastructure Challenges?**
  - Utilities, Healthcare, and Defense
  - *Historical Case Study:* The Oldsmar, Florida Water Treatment Plant Hack
- **How Do We Protect What We Cannot Patch?**
  - Compensating Controls for Obsolete Systems
  - Segmentation and Hardening of Legacy Assets
  - *Table:* Compensating Controls for Common Legacy Vulnerabilities
- **Chapter Review and Conclusion**

---

### Part IV: Security Operations, Automation, and Incident Response

#### Chapter 11: Security Operations, Monitoring, and Threat Hunting
*Maps to Objectives: 4.1, 4.3*

**Learning Outcomes:**
1. **Analyze** data from SIEM solutions to identify trends, prioritize alerts, and reduce audit logs.
2. **Establish** behavior baselines and analytics for networks, systems, users, and applications (UBA/UEBA).
3. **Incorporate** diverse data sources into monitoring activities.
4. **Formulate** alerting rules and metrics to minimize false positives and measure security effectiveness.
5. **Apply** threat-hunting concepts using hypothesis-based searches, honeypots, and internal reconnaissance.
6. **Evaluate** external threat intelligence sources, including OSINT, dark web monitoring, and ISACs.
7. **Implement** threat intelligence platforms (TIPs) and indicator of compromise (IoC) sharing standards (STIX/TAXII).
8. **Develop** rule-based detection logic using languages such as Sigma, YARA, and Snort.

**Chapter Outline:**
- **Introduction**
- **How Do We Make Sense of Security Data?**
  - SIEM Log Aggregation and Correlation
  - Prioritizing Alerts and Reducing Noise
  - *Diagram:* The SIEM Data Pipeline (Collection to Alerting)
  - *Table:* STIX vs. TAXII (Threat Intelligence Sharing)
- **How Do We Baseline Normal Behavior?**
  - User and Entity Behavior Analytics (UEBA)
  - Identifying Anomalies in Systems and Apps
  - *Fictional Case Study:* Hamlet (Threat Hunter at Denmark Cyber Defense) spots a sophisticated insider using UEBA anomalies.
- **How Do We Proactively Hunt for Threats?**
  - Internal Reconnaissance and Honeypots
  - Hypothesis-Based Searches
  - *Historical Case Study:* Marriott/Starwood Data Breach (Uncovering a Long-Dwelling APT)
  - *Diagram:* Honeypot and Honeynet Architecture
- **How Do We Leverage Threat Intelligence?**
  - External Feeds, OSINT, and ISACs
  - STIX, TAXII, and Rule-Based Languages (YARA, Sigma)
  - *Table:* Types of Threat Intelligence (Strategic vs. Tactical)
- **Chapter Review and Conclusion**

#### Chapter 12: Vulnerability Management, Automation, and Incident Response
*Maps to Objectives: 4.2, 3.6, 4.4*

**Learning Outcomes:**
1. **Analyze** common vulnerabilities and implement appropriate mitigations.
2. **Automate** security operations using scripting, Infrastructure as Code (IaC), and generative AI.
3. **Implement** Security Orchestration, Automation, and Response (SOAR) playbooks and runbooks.
4. **Utilize** Security Content Automation Protocol (SCAP) standards for vulnerability scanning and reporting.
5. **Analyze** malware artifacts using detonation, sandboxing, and reverse engineering.
6. **Conduct** volatile and non-volatile storage, network, and host analysis during incident response.
7. **Perform** root cause analysis and timeline reconstruction following a security breach.
8. **Organize** and execute preparedness exercises to enhance enterprise threat response capabilities.

**Chapter Outline:**
- **Introduction**
- **How Do We Manage and Mitigate Vulnerabilities?**
  - Input Validation and Memory-Safe Functions
  - SCAP standards (OVAL, CVE, CVSS)
  - *Table:* Common Software Vulnerabilities and Mitigations
  - *Table:* Understanding CVSS Scoring Metrics
- **How Can Automation Force-Multiply Security?**
  - Scripting (Python, PowerShell) and IaC
  - SOAR Playbooks and Auto-Containment
  - *Diagram:* An Automated SOAR Phishing Response Workflow
  - *Fictional Case Study:* Alice Liddell (IR Manager at Wonderland Logistics) automates containment with a custom Python script.
- **How Do We Respond to an Active Security Incident?**
  - Timeline Reconstruction and Root Cause Analysis
  - Malware Sandboxing and Reverse Engineering
  - *Historical Case Study:* The Equifax Breach (Failed Vulnerability Management & IR)
  - *Diagram:* The NIST Incident Response Lifecycle
- **How Do We Extract and Analyze Artifacts?**
  - Volatile vs. Non-Volatile Storage Analysis
  - Metadata and Hardware (JTAG) Analysis
- **Chapter Review and Conclusion**
