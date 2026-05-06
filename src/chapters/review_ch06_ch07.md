# Chapters 6 & 7 — True / False Review

> **Note on construction.** The answer key below was produced by `src/scripts/generate_tf_sequence.py` (seed `17`), which yields a balanced 10-True / 10-False sequence. The claims were then authored to match. False claims are written as *right answers to the wrong question* — each false statement is itself a true description of a related concept that the question deliberately mislabels. Students should be able to identify both *that* the statement is wrong and *which* concept the description actually fits.

---

## Chapter 6 — Secure Systems Lifecycle and Hardware Assurance

1. Non-functional security requirements should be documented with testable acceptance criteria so that automated pipelines can verify them, rather than as vague aspirational statements like "the system must be secure."

2. SAST analyzes source code, bytecode, or binaries without executing them, which is what allows it to run early and quickly in a CI pipeline before any test environment exists.

3. Interactive Application Security Testing (IAST) detects vulnerabilities by sending malicious inputs against a running application from the outside without any access to source code or runtime instrumentation, in the same way an external attacker would.

4. A Hardware Security Module (HSM) is a chip soldered to the motherboard of an individual workstation or server whose primary purpose is to record cryptographic measurements of each boot component into Platform Configuration Registers for later remote attestation.

5. A Software Bill of Materials (SBoM) is a machine-readable inventory of every component in a software product, and organizations that maintained current SBoMs were able to identify their Log4Shell exposure in hours rather than weeks.

6. Secure Boot blocks unsigned or untrusted boot components from executing, while Measured Boot records cryptographic hashes of each component into TPM PCRs so that a remote verifier can later attest to what actually ran during startup.

7. Rowhammer is an attack in which a USB device's microcontroller firmware is reprogrammed so that the device impersonates a keyboard and injects an attacker-supplied keystroke payload faster than a user can intervene.

8. Formal methods are mathematical specification and verification techniques used primarily in high-assurance contexts such as cryptographic libraries, operating system kernels, hypervisors, and avionics control software.

9. A Self-Encrypting Drive supports cryptographic erasure, allowing an administrator to render all stored data permanently unreadable in milliseconds simply by destroying the drive's internal encryption key.

10. Typical branch protection rules in modern version-control platforms include requiring pull requests before merging, requiring a minimum number of reviewers, requiring CI status checks to pass, and requiring cryptographically signed commits.

---

## Chapter 7 — Enterprise Cloud and Hybrid Security

11. Across all cloud service models — IaaS, PaaS, and SaaS — the customer is always responsible for data classification, identity management of their users, and configuration of the service itself.

12. A *proxy-based* CASB integrates with a SaaS provider's management API to inspect data already stored in the service, audit configurations retroactively, and apply DLP policies to existing content after the fact.

13. An IPsec site-to-site VPN provides a dedicated physical or logical circuit between the customer's network and the cloud provider's edge, contracted bandwidth, predictable latency, and no traversal of the public internet.

14. In a Platform as a Service deployment, the customer is responsible for patching the guest operating system and runtime libraries on which their application code executes, as well as the application code itself.

15. An over-permissioned function execution role is the dominant serverless misconfiguration pattern, and the primary defense is to apply least privilege to the function's IAM identity and automate that enforcement in the deployment pipeline.

16. Policy-as-code tools such as Checkov, tfsec, and Open Policy Agent run inside production cloud workloads at runtime, inspecting requests as they arrive and blocking exploits in real time before the application code processes them.

17. Data remanence refers to the failure mode in which a cloud storage resource has been misconfigured to allow public read access from unauthenticated users on the open internet, typically due to a permissive bucket or container policy.

18. AWS introduced IMDSv2 to mitigate SSRF-based abuse of the EC2 instance metadata service by requiring a session-based authentication step before instance role credentials can be retrieved.

19. A Cloud-Native Application Protection Platform (CNAPP) is a tool category whose sole function is the continuous assessment of cloud configuration against established security baselines and the detection of configuration drift over time.

20. *Cloud-managed keys* are a key-management pattern in which the customer generates encryption key material outside the cloud, imports it into the provider's KMS, and retains the ability to revoke that key independently of the cloud provider.

---

## Answer Key

1. **True.** "The system must be secure" is not a requirement; testable, automatable acceptance criteria are.

2. **True.** SAST is a static, pre-execution analysis — its speed and CI-friendliness are direct consequences of not needing a running system.

3. **False.** The description fits **DAST**, not IAST. IAST uses an instrumentation agent embedded inside the running application during testing; it has full runtime context, which is exactly what gives it lower false positives than the black-box approach described.

4. **False.** The description fits a **TPM**, not an HSM. TPMs are per-device chips that record boot measurements into PCRs and support attestation. An HSM is a tamper-resistant appliance for high-throughput enterprise crypto operations and master-key protection — it is not soldered to a workstation motherboard.

5. **True.** SBoMs were the operational difference between a multi-day Log4Shell triage and a multi-week one.

6. **True.** This is the canonical Secure Boot vs. Measured Boot distinction: Secure Boot *blocks*, Measured Boot *records*.

7. **False.** The description fits **BadUSB / Rubber Ducky-style HID attacks**. Rowhammer is a DRAM hardware vulnerability in which repeatedly accessing specific memory rows induces bit flips in adjacent rows, enabling privilege escalation through memory corruption.

8. **True.** Formal methods are practical only where the cost is justified by extremely high assurance requirements; the example domains listed are the standard ones.

9. **True.** This is the headline operational benefit of SEDs implementing the TCG Opal standard.

10. **True.** All four are standard branch-protection capabilities on platforms like GitHub, GitLab, and Bitbucket.

11. **True.** This is the unchanging top row of the shared responsibility matrix.

12. **False.** The description fits an **API-based CASB**. A proxy-based CASB sits inline between the user and the cloud service in real time and can block prohibited actions before they happen, rather than auditing data already stored.

13. **False.** The description fits **dedicated private connectivity** services such as AWS Direct Connect, Azure ExpressRoute, or Google Cloud Interconnect. An IPsec site-to-site VPN runs over the public internet, sharing its variable performance.

14. **False.** The description fits **IaaS**. In PaaS the *provider* patches the OS and runtime; the customer is responsible for application code, application configuration, data, and identity.

15. **True.** This is the central serverless security lesson and the focus of the Dorothy Gale case study.

16. **False.** The description fits **RASP** (Runtime Application Self-Protection). Policy-as-code tools like Checkov, tfsec, and OPA scan IaC configuration files at build / pull-request time and reject misconfigurations *before* infrastructure is deployed — they do not run inside production workloads.

17. **False.** The description fits **data exposure**. Data *remanence* is residual data that persists on shared storage after a "delete," which is mitigated through cryptographic erasure.

18. **True.** IMDSv2's session-based protocol substantially raises the bar for SSRF-to-credential-theft attacks of the kind seen in the Capital One breach.

19. **False.** The description fits **CSPM** (Cloud Security Posture Management). CNAPP is a broader, unified platform that combines CSPM, CWPP (Cloud Workload Protection Platform), and IaC scanning into a single product.

20. **False.** The description fits **Bring Your Own Key (BYOK)**. Cloud-managed keys are generated, stored, rotated, and used by the provider on the customer's behalf with minimal customer operational involvement.
