# CompTIA SecurityX (CAS-005) Writing Guidelines

This document outlines the editorial standards, formatting rules, and stylistic approach for the CompTIA SecurityX textbook. It serves as the primary reference for all chapter drafts.

## 1. Chapter Template and Style Sheet
Every chapter must adhere to the following structural elements and callouts:
- **Learning Outcomes:** Bulleted list at the start of the chapter, mapped to Bloom's Taxonomy.
- **Introduction:** A brief hook setting the stage for the chapter.
- **Section Headings:** Major headings (H2) phrased as questions to engage the reader.
- **Callout Styles:** Use specific formatting (e.g., Markdown blockquotes or bolded prefixes) for the following:
  - **[Case Study]**: Real-world or fictional scenarios illustrating concepts.
  - **[Warning]**: Critical security pitfalls, common mistakes, or high-risk areas.
  - **[Thought Question]**: Rhetorical or reflective questions to test student comprehension.
  - **[Key Point]**: Summary of a vital concept that might appear on the exam.
- **Chapter Review and Conclusion:** A wrap-up of the chapter, followed by a review of key terms introduced in the text.

## 2. Reading Level and Tone
- **Target Audience:** 10th to 12th-grade reading level. 
- **Tone:** Somewhat conversational, encouraging, and engaging.
- **Clarity and Explicitness:** Do not assume prior advanced knowledge. Explain concepts clearly.
- **Concrete Connections:** Use analogies and concrete examples. Explain things in multiple ways if necessary. Point out nuances, connections, and "the why" that might seem obvious to a seasoned security professional but are vital for a learner.

## 3. Formatting and Layout
- **Mix of Elements:** Break up large walls of text. Use a healthy mix of paragraph text, bulleted/numbered lists, and tables where appropriate to improve scannability.
- **Key Terms:** The first time a key term is introduced, it must be **bolded** and immediately defined in clear language within the paragraph or bullet point. A consolidated review of these terms should appear at the end of the chapter.

## 4. Figures and Diagrams
- **Visuals:** Complex architectures and workflows should be accompanied by diagrams.
- **Tools & Workflow:** Diagrams will be scripted using Graphviz, Mermaid, or Matplotlib. Because Pressbooks requires static images, a separate script will be used to render these codes into `.png` files.
- **Captions:** Every figure must be included as a PNG and be properly captioned explaining its relevance.

## 5. Examples and Case Studies
To make abstract concepts concrete, every chapter must utilize strong examples using one of two methods:

### Method A: Historical Cases
Use well-documented, real-world cyber incidents. Explain the mechanics of what happened, why it matters, and how it relates to the learning objective. *Crucially, these are pre-assigned in the Table of Contents to avoid repetition across chapters.*

### Method B: Fictional Modern Businesses
Utilize characters from public domain literature working in modern corporate or tech environments to illustrate security scenarios. 

**Approved Fictional Universe Roster (25 Examples)**
*Alice in Wonderland*
1. **Alice Liddell** (Female) - Incident Response Manager at *Wonderland Logistics*
2. **The Mad Hatter / Hatta** (Male) - Lead Cryptographer at *Teatime Tech*
3. **The Red Queen** (Female) - Chief Information Security Officer (CISO) at *Hearts Financial*

*The Wizard of Oz*
4. **Dorothy Gale** (Female) - Cloud Architect at *Emerald City Solutions*
5. **Oscar Diggs / The Wizard** (Male) - CEO of *Illusion Cloud Services*
6. **Nick Chopper / Tin Woodman** (Male) - Industrial Control Systems (OT) Engineer at *Yellow Brick Manufacturing*

*Jane Austen*
7. **Elizabeth Bennet** (Female) - Security Analyst at *Pemberley Data Systems*
8. **Fitzwilliam Darcy** (Male) - Director of Risk Management at *Derbyshire Holdings*
9. **Emma Woodhouse** (Female) - Identity and Access Management (IAM) Specialist at *Highbury Networks*

*William Shakespeare*
10. **Hamlet** (Male) - Threat Hunter at *Denmark Cyber Defense*
11. **Lady Macbeth** (Female) - Insider Threat & Compliance Officer at *Glamis Enterprise*
12. **Prospero** (Male) - Network Architect at *Milan Island Telecom*
13. **Juliet Capulet** (Female) - Security Awareness Trainer at *Verona Health*
14. **Iago** (Male) - Red Team Penetration Tester at *Venice Shipping Co.*

*Sherlock Holmes*
15. **Sherlock Holmes** (Male) - Lead Digital Forensics Investigator at *Baker Street Consulting*
16. **Irene Adler** (Female) - Data Privacy Officer (DPO) at *Bohemia Global*
17. **Professor Moriarty** (Male) - Chief Information Officer (CIO) turned Insider Threat at *Syndicate Inc.*

*Grimm's Fairy Tales*
18. **Cinderella / Ella** (Female) - Systems Administrator at *Glass Slipper Tech*
19. **Rumpelstiltskin** (Male) - Blockchain/Cryptocurrency Engineer at *GoldSpinners LLC*
20. **Snow White** (Female) - GRC Analyst at *Seven Dwarfs Mining*
21. **The Big Bad Wolf** (Male) - External Auditor / Social Engineer at *Forest Edge Security*

*Classic Horror & Sci-Fi*
22. **Victor Frankenstein** (Male) - Bio-Tech Security Engineer at *Geneva Labs*
23. **Mina Harker** (Female) - Security Operations Center (SOC) Manager at *Carfax Logistics*
24. **Count Dracula** (Male) - CISO at *Transylvanian Blood Bank*
25. **Dr. Henry Jekyll** (Male) - Access Management Admin battling compromised accounts at *Soho Pharmaceuticals*
