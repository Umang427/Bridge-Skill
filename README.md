# SkillBridge — AI Adaptive Onboarding Engine

> **Hackathon Submission 2025** — AI-driven, adaptive learning engine that parses a new hire's capabilities and dynamically maps a personalized training pathway.

![SkillBridge Banner](https://img.shields.io/badge/AI-Adaptive%20Onboarding-00d4ff?style=for-the-badge)
![Groq](https://img.shields.io/badge/Powered%20by-Groq%20%7C%20Llama%203.3%2070B-7c3aed?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)

---

## 🚀 Quick Start (Zero Setup)

```bash
# Just open the HTML file in any browser
open adaptive-onboarding-engine.html
```

No server. No install. No dependencies. Pure browser app.

---

## 📌 What It Does

SkillBridge is a single-file, AI-powered onboarding engine that:

1. **Parses** a candidate's resume to extract skills and experience levels
2. **Analyzes** the target job description for required competencies
3. **Computes** the skill gap using an adaptive mapping algorithm
4. **Generates** a personalized, prioritized learning pathway (5–8 modules)
5. **Explains** every recommendation via a full AI reasoning trace

---

## ✅ Features

| Feature | Description |
|---|---|
| 📄 Resume Parsing | Upload PDF/TXT or paste text — LLM extracts skills, tools, experience levels |
| 🎯 JD Analysis | Extracts required skills, seniority expectations, domain-specific tools |
| ⚡ Skill Gap Engine | Computes exact delta between candidate profile and role requirements |
| 📊 Readiness Score | 0–100% role-readiness meter based on matched vs required skills |
| 🗺️ Adaptive Pathway | 5–8 sequenced modules, ordered by priority + skill dependencies |
| 🧠 Reasoning Trace | Transparent AI explanation of why each module was included |
| 🏭 12 Job Domains | Software Eng, Data Science, HR, Finance, Healthcare, Manufacturing, and more |
| 🖱️ Drag & Drop Upload | PDF and TXT file upload with instant text extraction |

---

## 🏗️ Architecture & Workflow

```
┌─────────────────────────────────────────────────────────┐
│                      BROWSER (Client)                    │
│                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────┐  │
│  │  Resume  │    │    JD    │    │  Domain Selector │  │
│  │  Upload  │    │  Upload  │    │  (12 categories) │  │
│  └────┬─────┘    └────┬─────┘    └────────┬─────────┘  │
│       └───────────────┴──────────────────┘             │
│                        │                                │
│              ┌──────────▼──────────┐                   │
│              │   Prompt Builder    │                   │
│              │  (Structured LLM    │                   │
│              │   instruction set)  │                   │
│              └──────────┬──────────┘                   │
│                         │                               │
└─────────────────────────┼───────────────────────────────┘
                          │ HTTPS API Call
                          ▼
┌─────────────────────────────────────────────────────────┐
│              GROQ API (Llama 3.3 70B)                   │
│                                                         │
│  Input:  Resume text + JD text + domain context        │
│  Output: Structured JSON (skills, gaps, modules)       │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  ADAPTIVE ENGINE                        │
│                                                         │
│  1. Skill Extraction    → skills_have[], skills_need[] │
│  2. Gap Computation     → skills_gap[], partial[]      │
│  3. Readiness Scoring   → 0–100% match score           │
│  4. Module Sequencing   → priority × dependency order  │
│  5. Reasoning Trace     → step-by-step justification   │
└─────────────────────────────────────────────────────────┘
```

---

## 🧠 Skill Gap Analysis Logic

### Step 1 — Skill Extraction
The LLM is prompted with a structured instruction set to extract:
- **Hard skills** (tools, languages, frameworks, certifications)
- **Soft skills** (leadership, communication, project management)
- **Proficiency signals** (years of experience, "basic/intermediate/advanced" cues)

### Step 2 — Gap Computation (Adaptive Pathing Algorithm)
```
gap = required_skills − (candidate_skills ∩ required_skills)
partial = skills where candidate has partial overlap (detected by LLM)
readiness_score = |candidate_skills ∩ required_skills| / |required_skills| × 100
```

### Step 3 — Module Prioritization
Modules are ranked by a composite priority score:

```
priority_score = gap_severity × role_weight × dependency_order
```

- **CRITICAL**: Core job function, missing entirely
- **HIGH**: Frequently required, has partial knowledge
- **MEDIUM**: Supporting skill, partial knowledge exists
- **LOW**: Nice-to-have, foundational already present

### Step 4 — Pathway Sequencing
Modules are sequenced using a dependency graph heuristic:
- Foundational skills → domain tools → role-specific application → capstone project
- Skills with existing partial knowledge are de-prioritized (skip or accelerate)
- Redundant training is explicitly skipped when skill already exists

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Vanilla HTML5, CSS3, JavaScript (ES6+) — zero frameworks |
| **AI Model** | Llama 3.3 70B via Groq API |
| **Skill Extraction** | LLM-based NER with structured JSON output |
| **Adaptive Logic** | Custom gap-mapping + priority scoring (original implementation) |
| **File Parsing** | Browser FileReader API (TXT, PDF text extraction) |
| **Fonts** | Syne, Space Mono, DM Sans (Google Fonts) |

---

## 📦 Dependencies

**None.** This is a zero-dependency single-file application.

- No npm, no pip, no virtual environments
- No backend server required
- No database required
- Runs in any modern browser (Chrome, Firefox, Edge, Safari)

---

## 📊 Datasets Referenced

| Dataset | Source | Usage |
|---|---|---|
| Resume Dataset | [Kaggle — snehaanbhawal](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset/data) | Skill vocabulary reference |
| O*NET Database | [onetcenter.org](https://www.onetcenter.org/db_releases.html) | Occupational skill taxonomy |
| Jobs & JD Dataset | [Kaggle — kshitizregmi](https://www.kaggle.com/datasets/kshitizregmi/jobs-and-job-description) | JD skill pattern reference |

---

## 🐳 Docker (Optional)

```bash
# Build
docker build -t skillbridge .

# Run (serves on http://localhost:8080)
docker run -p 8080:80 skillbridge
```

---

## 📁 Project Structure

```
skillbridge/
├── adaptive-onboarding-engine.html   # Complete application (single file)
├── README.md                          # This file
└── Dockerfile                         # Optional containerization
```

---

## 🎯 Evaluation Criteria Coverage

| Criterion | Implementation |
|---|---|
| Technical Sophistication | LLM skill extraction + custom adaptive gap algorithm |
| Grounding & Reliability | Strict JSON schema, no hallucination on course catalog |
| Reasoning Trace | Full step-by-step AI reasoning panel (expandable) |
| Product Impact | Skips known skills, accelerates gaps — reduces redundant training |
| User Experience | Dark futuristic UI, drag-drop upload, visual pathway timeline |
| Cross-Domain Scalability | 12 job domains from Software Eng to Manufacturing to Healthcare |
| Documentation | This README + inline code comments + 5-slide deck |

---

## 👥 Team

Built for Hackathon 2025 — AI Adaptive Onboarding Challenge

---

## 📄 License

MIT License — free to use, modify, and distribute.
