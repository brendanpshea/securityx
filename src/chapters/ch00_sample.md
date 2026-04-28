# Chapter 0: The Architecture of Wonder

**Learning Outcomes:**

- **Identify** the core components of a secure cloud infrastructure.
- **Explain** the mechanics of an SSRF attack.

## Introduction
Security is not just about building walls; it's about understanding how the pieces fit together. In this sample chapter, we will explore the formatting and aesthetic elements that make up our premium textbook experience.

---

## What Does a Modern Architecture Look Like?
A modern architecture relies heavily on dynamic scaling and identity management. By leveraging APIs, microservices can communicate seamlessly.

> **[Key Point]** 
> An API Gateway acts as the single point of entry for all clients, handling routing, composition, and translation.

### The Role of IAM
Identity and Access Management (IAM) is the cornerstone of cloud security. If you lose control of your identities, you lose control of your data.

> **[Warning]** 
> Never hardcode AWS Access Keys into your source code. If committed to a public repository, attackers will scrape and exploit them within seconds.

---

## How Do Attackers Exploit Architecture?

Consider a scenario where a Web Application Firewall (WAF) is misconfigured to blindly trust internal traffic.

> **[Case Study]** 
> **The Capital One AWS Breach**
> In 2019, an attacker exploited a misconfigured open-source WAF to perform a Server-Side Request Forgery (SSRF) attack. The WAF, acting with high-privilege IAM roles, queried the AWS metadata service and returned temporary credentials to the attacker. This resulted in the theft of data belonging to over 100 million customers. 

<!-- -->

> **[Thought Question]**
> How would implementing Zero Trust principles have mitigated the impact of the SSRF vulnerability in the Capital One breach?

---

## Chapter Review and Conclusion
Understanding the interconnected nature of cloud resources is essential. A single misconfiguration can lead to catastrophic data loss.

### Key Terms Review
- **SSRF**: Server-Side Request Forgery, an attack where an application is coerced into making unauthorized requests on behalf of the attacker.
- **IAM**: Identity and Access Management, the framework of policies and technologies ensuring proper resource access.
