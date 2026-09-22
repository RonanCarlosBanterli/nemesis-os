# Meu OS

Sistema operacional pessoal montado pelo Nemesis Studio. Este arquivo
é lido pelo Claude Code em TODA sessão: é o que faz o seu time entender VOCÊ.

## Quem sou eu

Detalhe em `contexto/perfil.md`. Resumo:
- Você é o BI Specialist da Kronor Capital, cuidando de KPIs, dashboards e relatórios pra uma equipe de 32 pessoas entre assessores, operacional e produtos.
- O maior ralo do seu tempo é puxar dado da plataforma da XP na mão, login toda vez, antes de sequer começar a tratar e montar o Power BI.
- Não existe hoje nenhum export automático: cada atualização de dashboard começa com esse trabalho manual repetitivo.
- O time abaixo ataca isso na raiz (automação de coleta) e depois cuida do que vem depois: tratamento, indicador de performance dos assessores e a entrega pros stakeholders.

## Meu time (subagents reais em `.claude/agents/`)

Delegue pra eles quando a tarefa pedir a especialidade de cada um:
- `analista-performance-assessores`: Use para definir, revisar ou documentar medidas DAX e KPIs de performance dos 17 assessores comerciais e das demais áreas (oper...
- `integrador-dados-xp`: Use quando for preciso desenhar, revisar ou documentar o caminho de automação da coleta de dados na plataforma da XP (Developer...
- `relator-para-stakeholders`: Use quando um resultado já pronto no Power BI (KPI, painel, número de performance) precisar virar relatório ou apresentação obj...
- `design-system`: **OBRIGATÓRIO**. Use SEMPRE que o OS for gerar ou revisar qualquer coisa visual (dashboard, landing page, slide, carrossel, app, mockup, relatór...
- `especialista-analise-dados`: **Use SEMPRE que o pedido for um RELATÓRIO ou uma ANÁLISE de dados** (KPI, número, tendência, correlação, estrutura de dashboard) — vá direto nele, sem avaliar outros agentes antes.

## Minhas skills (`.claude/skills/`)

- `/analisar`: Audita e analisa planilha (.xlsx, .csv) antes de responder qualquer pergunta sobre ela. Perfila o arquivo inteiro, mostra as ar...
- `/apresentar`: Transforma um assunto em apresentação widescreen 16:9 que abre no navegador e exporta PDF. Aplica a gramática editorial de slid...
- `/atualiza-dashboard`: Pega o dado já tratado e gera a especificação de medidas DAX e o checklist de aplicação no Power BI, seguindo o padrão de model...
- `/captacao-liquida`: Calcula a captação líquida da Kronor pra qualquer período (ano, mês ou intervalo de meses), puxando de contexto/dados/Captacao_Liquida.xlsx com reconciliação automática.
- `/conectar`: Conecta o OS às ferramentas que a pessoa já usa (CRM, ERP, planilha na nuvem, ferramenta de anúncio, sistema de atendimento). F...
- `/extrai-xp`: Roteiro passo a passo pra deixar a extração de dados da plataforma da XP repetível, cortando o login manual toda vez que um das...
- `/extrair-design-system`: Extrai o design system de um HTML/URL/print e gera um design-system.html canônico (11 seções, anatomia replicável, regras do/do...
- `/relatorio-assessores`: Gera o resumo de KPI por assessor pronto pra apresentar, puxando do modelo de dados já mantido e escrito no tom de comunicação...
- `/site-reveal-cinematico`: Cria sites scroll-driven com reveal cinematográfico, um vídeo controlado quadro a quadro pelo scroll (estilo "Apple product rev...

## Minha fonte de dados

**Sua extração da plataforma da XP**: Hoje é manual, login e download toda vez. O primeiro passo é estruturar essa extração num formato fixo (planilha ou pasta padrão) pra depois automatizar a atualização do Power BI em cima dela. (detalhe em `contexto/fonte.md`)

## Como meu OS trabalha

- Português do Brasil, direto e honesto. Nunca invente número ou dado que você não tem.
- **Todo entregável vai em `producao/<pasta>/`, NUNCA na raiz do repo.** Qualquer arquivo que uma skill ou um pedido produzir (relatório, roteiro, peça, deck, export) grava em `producao/<tema>/`, por exemplo `producao/eventos/`, `producao/relatorios/`. Criar pasta nova na RAIZ é erro: a raiz é só a estrutura do OS (`.claude/`, `contexto/`, `producao/`). Na dúvida sobre a subpasta, use o tema da skill.
- O dado de entrada vem de `contexto/dados/` (planilhas) e `contexto/referencia/` (docs do negócio).
- Consistência visual é inegociável: todo entregável visual passa pelo agente `design-system`.
- **Pergunta sobre planilha ou dado (`contexto/dados/`, `.xlsx`, `.csv`): INVOQUE a skill `analisar`.**
  Invoque a skill de verdade, não reimplemente o que ela faz. Ela roda um profiler
  determinístico que lê 100% das linhas e é coberto por teste de regressão. Script
  escrito na hora não tem essa garantia, mesmo quando parece dar certo.
- **Conectar ferramenta ou sistema externo: INVOQUE a skill `conectar`.**
  Invoque a skill de verdade. Ela carrega o procedimento e o catálogo de receitas
  verificadas, que você não tem como reproduzir de memória sem inventar endpoint.
