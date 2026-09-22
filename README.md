# Meu OS

Gerado pelo Nemesis Studio. 4 agentes, 8 skills, feitos sob medida pra você.

Estrutura do seu OS:
- `.claude/agents/`: **o seu time, como subagents reais do Claude Code** (invocáveis)
- `contexto/`: quem você é. Jogue seus docs em `contexto/referencia/` ANTES de montar, o time nasce sabendo
- `contexto/dados/`: onde entram suas PLANILHAS (`.csv`, `.xlsx`). É daqui que o time lê seu número, e a skill `/analisar` audita antes de responder
- `producao/`: onde as entregas do seu time caem
- `.claude/skills/`: suas skills sob medida
- `meu-os.json`: o manifesto do OS

O agente `design-system` é obrigatório: garante que todo entregável visual saia coeso.
