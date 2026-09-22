# AGENTS.md

## Project purpose
This repository is a personal operating system for a Kronor Capital BI specialist. The work centers on KPI analysis, reports, data extraction workflows, and stakeholder-ready outputs.

## Primary project docs
- [README.md](README.md): project overview and OS structure
- [CLAUDE.md](CLAUDE.md): role context, team structure, and workflow expectations
- [contexto/fonte.md](contexto/fonte.md): source-data context and XP extraction assumptions
- [contexto/perfil.md](contexto/perfil.md): user profile and working context

## Core workflow conventions
- Keep all generated outputs under [producao/](producao/). Do not create new deliverables in the repository root.
- Treat [contexto/dados/](contexto/dados/) as the inbound data location for spreadsheets and extracted exports.
- Treat [contexto/referencia/](contexto/referencia/) as the repository for business context and reference material.
- Prefer the project’s task-specific agents and skills before inventing ad hoc workflows.

## Agent behavior to follow
- If the task involves spreadsheets, CSV/XLSX files, or data validation, use the `/analisar` workflow instead of writing a one-off script.
- If the task involves external systems or integrations, use `/conectar` rather than guessing endpoints or credentials.
- If the task involves visual deliverables, involve the `design-system` agent and align with the project’s visual system.
- For KPI/model questions, prefer the `analista-performance-assessores` guidance and keep definitions explicit. Do not invent metrics without a clear business definition.
- For automation or XP extraction design, follow the `integrador-dados-xp` guidance and prioritize official/approved access paths.

## Quality bar
- Be honest with numbers; do not fabricate metrics or source data.
- Keep English/Portuguese explanations clear and concise.
- Prefer small, reviewable changes over broad rewrites.
- When uncertain, link back to the project docs rather than creating undocumented assumptions.
