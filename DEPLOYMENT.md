# Amia Workspace Setup & Deployment Guide

> **Purpose**: Instructions for initializing, configuring, and running **Amia** (Personal AI Assistant & Strategic Advisor) across any machine or LLM provider (Copilot, Claude, Gemini, ChatGPT/Cursor, etc.).

---

## 1. Core Concept & Architecture

Amia operates as a **model-vendor-agnostic** executive assistant and strategic partner. The workspace configuration defines her persona, long-term memory, and operational directives independently of any specific AI engine or client runtime.

---

## 2. Automatic System Directive (`AGENT.md`)

The master configuration for Amia is maintained in **[AGENT.md](AGENT.md)**.

### Provider-Agnostic Entry Points:
To ensure compatibility across different LLM runners and IDE extensions, entry-point configuration files link directly back to [AGENT.md](AGENT.md):

| Provider / Runner | Entry Point File | Description |
| :--- | :--- | :--- |
| **Canonical Directive** | [AGENT.md](AGENT.md) | Primary source of truth for Amia's identity & directives |
| **Gemini / Antigravity** | [GEMINI.md](GEMINI.md) | Entry point for Gemini-based tools |
| **Claude Code** | [CLAUDE.md](CLAUDE.md) | Entry point for Claude CLI / Code |
| **GitHub Copilot** | [.github/copilot-instructions.md](.github/copilot-instructions.md) | Instructions for Copilot workspace sessions |

Additional compatibility files ([RULES.md](RULES.md), [.agent/rules/assistant.md](.agent/rules/assistant.md)) redirect to [AGENT.md](AGENT.md) for tools that auto-discover workspace rules.

---

## 3. Workspace Directory Structure

Deploy or clone the workspace to your target planning location:

```text
./                               # Workspace root directory (home)
|-- AGENT.md                     # Master system directive (vendor-agnostic)
|-- RULES.md                     # Redirect to AGENT.md (vendor compatibility)
|-- README.md                    # Workspace index & navigation
|-- DEPLOYMENT.md                # Environment setup guide (this file)
|-- GEMINI.md                    # Gemini/AGY entry point -> AGENT.md
|-- CLAUDE.md                    # Claude entry point -> AGENT.md
|-- LICENSE                      # License file
|-- .gitignore                   # Git ignore rules
|-- .github/
|   +-- copilot-instructions.md  # Copilot entry point -> AGENT.md
|-- projects/                    # All managed project directories
|   +-- <project-name>/          # Individual project directory
|       |-- README.md            # Project overview & navigation
|       |-- contacts.md          # Stakeholder tracking
|       +-- references/          # Free-style reference materials
|-- amia/                        # Dedicated folder for Amia's personal artifacts
|-- media/                       # General workspace visual assets & diagrams
|-- reports/                     # Generated strategic documents & executive summaries
|-- .planning/                   # Agent infrastructure
|   |-- MEMORY.md                # Long-term memory & profile
|   |-- DECISION_LOG.md          # Strategic decision tracking
|   +-- TEMPLATES.md             # Standardized operational templates
+-- .agent/                      # Local agent configuration & rules
    |-- rules/
    |   +-- assistant.md         # Redirect to AGENT.md (vendor compatibility)
    +-- skills/                  # Integrated assistant skills
```

---

## 4. Tool Execution & Environment

When launching Amia via any CLI runner or assistant tool (e.g., `claude`, `agy`, Copilot, Cursor):

* **Working Directory**: Open or launch the tool inside the workspace root (`./`).
* **Zero-Coding Policy**: Ensure the session respects the strategic planning focus.
* **Automatic Context Loading**: The assistant client automatically reads [AGENT.md](AGENT.md) or its corresponding provider entry file (`CLAUDE.md`, `GEMINI.md`, etc.). No special environment variables or manual flags are required.

---

## 5. Verification & Setup Checklist

- `[ ]` **Identity Test**: Asking *"Who are you and what is your role?"* returns Amia as Executive Assistant & Strategic Advisor.
- `[ ]` **Artifact Storage**: Personal artifacts write to `amia/`, media to `media/`, reports to `reports/`, project files to `projects/<name>/`.
- `[ ]` **Memory Maintenance**: [.planning/MEMORY.md](.planning/MEMORY.md) is consulted for personal goals and preferences.
