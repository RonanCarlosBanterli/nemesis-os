# Meu OS

Sistema operacional pessoal montado pelo Nemesis Studio. Este arquivo
é lido pelo Claude Code em TODA sessão: é o que faz o seu time entender VOCÊ.

## Quem sou eu

Detalhe em `contexto/perfil.md`. Resumo:
- Você é o BI da Kronor Capital, hoje o maior ladrão do seu tempo é montar relatórios e apresentações na mão a partir de planilhas Excel.
- A meta é clara: tirar esse trabalho manual das suas costas pra sobrar tempo e você assumir mais projetos de automação.
- O time abaixo ataca direto isso: quem automatiza o processo, quem transforma número em apresentação pronta pra stakeholder, e quem cuida do visual padrão da casa.

## Meu time (subagents reais em `.claude/agents/`)

Delegue pra eles quando a tarefa pedir a especialidade de cada um:
- `analista-de-indicadores-de-assessores`: Use para cruzar dados de performance e engajamento dos assessores comerciais, identificar desvios em relação ao esperado, inves...
- `automatizador-de-processos`: Use quando for preciso desenhar ou construir um fluxo de automação que tire uma planilha Excel manual da jogada, escolhendo ent...
- `storyteller-de-indicadores`: Use quando os indicadores já estiverem prontos e for preciso transformá-los em narrativa e apresentação para stakeholders (gest...
- `design-system`: **OBRIGATÓRIO**. Use SEMPRE que o OS for gerar ou revisar qualquer coisa visual (dashboard, landing page, slide, carrossel, app, mockup, relatór...

## Minhas skills (`.claude/skills/`)

- `/analisar`: Audita e analisa planilha (.xlsx, .csv) antes de responder qualquer pergunta sobre ela. Perfila o arquivo inteiro, mostra as ar...
- `/apresentacao-stakeholders`: Transforma os indicadores do mês em uma apresentação pronta, com narrativa executiva e visual sóbrio no padrão da Kronor, deleg...
- `/apresentar`: Transforma um assunto em apresentação widescreen 16:9 que abre no navegador e exporta PDF. Aplica a gramática editorial de slid...
- `/conectar`: Conecta o OS às ferramentas que a pessoa já usa (CRM, ERP, planilha na nuvem, ferramenta de anúncio, sistema de atendimento). F...
- `/extrair-design-system`: Extrai o design system de um HTML/URL/print e gera um design-system.html canônico (11 seções, anatomia replicável, regras do/do...
- `/raio-x-assessor`: Gera um panorama rápido de engajamento e performance de um assessor específico ou de toda a equipe comercial, cruzando a base d...
- `/relatorio-mensal`: Gera o relatório gerencial mensal a partir da planilha de indicadores da Kronor, puxando os dados direto da fonte, delegando a...
- `/site-reveal-cinematico`: Cria sites scroll-driven com reveal cinematográfico, um vídeo controlado quadro a quadro pelo scroll (estilo "Apple product rev...

## Minha fonte de dados

**sua planilha de indicadores no Excel**: É de onde os relatórios e apresentações saem hoje. Conecte ela como base viva pra os agentes trabalharem em cima do dado real, sem retrabalho manual. (detalhe em `contexto/fonte.md`)

## Como meu OS trabalha

- Português do Brasil, direto e honesto. Nunca invente número ou dado que você não tem.
- **Todo entregável vai em `producao/<pasta>/`, NUNCA na raiz do repo.** Qualquer arquivo que uma skill ou um pedido produzir (relatório, roteiro, peça, deck, export) grava em `producao/<tema>/`, por exemplo `producao/eventos/`, `producao/relatorios/`. Criar pasta nova na RAIZ é erro: a raiz é só a estrutura do OS (`.claude/`, `contexto/`, `producao/`). Na dúvida sobre a subpasta, use o tema da skill.
- **Todo relatório, dashboard ou análise entregue vai em `producao/relatorios/`: é de lá que a aba "Relatórios" da Sala de Controle lê.** Relatório com visual (dashboard, HTML) = pasta `producao/relatorios/<slug>/` com `index.html` autocontido (sem CDN, com botão "Gerar PDF" via `window.print()` e `@media print` A4 paisagem) e um `relatorio.json` ao lado: `{"titulo", "descricao" (1 frase), "tipo" ("dashboard", "análise"...), "agente" (quem fez), "criado_em" (ISO 8601), "arquivo": "index.html"}`. Relatório em texto/PDF = arquivo `.md`/`.pdf` solto na mesma pasta. Sem isso ele não aparece na aba.
- **Relatório/dashboard de captação (mensal, por ano/mês/assessor): INVOQUE a skill `relatorio-captacao`, SEMPRE.** Ela reprocessa a planilha mais recente de `contexto/dados/` ANTES de enviar ou abrir o HTML. Nunca abra nem entregue um `index.html` de captação que já está em `producao/relatorios/` sem rodar a atualização primeiro: ele guarda os números da última geração e fica velho.
- **Qualquer outro relatório, dashboard ou análise que eu pedir: INVOQUE a skill `relatorio-html`.** Ela conecta na base `contexto/dados/` (lendo do disco, sempre), analisa com a skill `analisar`, apresenta em HTML com botão "Exportar PDF" depois da análise e salva na aba Relatórios do Painel **somente quando o relatório for diferente** de um que já existe (mesmo conteúdo = não duplica, só reabre o existente).
- **Todo pedido que eu fizer aparece no Painel, na coluna "Rodando" de Tarefas** (hook `.nemesis/tarefas_hook.py`, ligado em `.claude/settings.json`): não precisa fazer nada pra isso, e não apague esses hooks.
- O dado de entrada vem de `contexto/dados/` (planilhas) e `contexto/referencia/` (docs do negócio).
- Consistência visual é inegociável: todo entregável visual passa pelo agente `design-system`.
- **Pergunta sobre planilha ou dado (`contexto/dados/`, `.xlsx`, `.csv`): INVOQUE a skill `analisar`.**
  Invoque a skill de verdade, não reimplemente o que ela faz. Ela roda um profiler
  determinístico que lê 100% das linhas e é coberto por teste de regressão. Script
  escrito na hora não tem essa garantia, mesmo quando parece dar certo.
- **Conectar ferramenta ou sistema externo: INVOQUE a skill `conectar`.**
  Invoque a skill de verdade. Ela carrega o procedimento e o catálogo de receitas
  verificadas, que você não tem como reproduzir de memória sem inventar endpoint.
