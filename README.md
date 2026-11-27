# Wumpus World Lab

**Disciplina:** Introdução à Inteligência Artificial  
**Semestre:** 2026.2  
**Professor:** Andre Luis Fonseca Faustino 
**Turma:** T01

---

## Integrantes do Grupo
* Lucas Emanuel da Paz Ribeiro (20250051945)
* Erick Alberth da Silva Santos (20250044619)
* Pedro Vitor de Oliveira Moura (20230036093)
* Mateus Sousa da Silva (20220046908)
* Thallys Augusto Torres de Souza (20240011552)

## Descrição do Projeto
Este projeto implementa o **Mundo de Wumpus**, um clássico da IA em que um agente explora uma caverna em grade às cegas, sem saber onde estão os poços nem o Wumpus. O objetivo é pegar o ouro e voltar à saída com vida, usando apenas as percepções locais (brisa perto de poços, fedor perto do Wumpus, brilho do ouro e grito quando o Wumpus é atingido pela flecha).

O foco do trabalho é **comparar formas de raciocinar sob incerteza**. O mesmo mundo pode ser explorado por:

* **Agentes lógicos**, que mantêm uma base de conhecimento em lógica proposicional e só se movem para células provadamente seguras. Os motores de inferência disponíveis são Forward Chaining, Resolução por refutação e DPLL.
* **Agentes probabilísticos**, que estimam a probabilidade de poço em cada célula e escolhem o caminho de menor risco. Os motores são Inferência por enumeração e Eliminação de variáveis.
* **Você mesmo**, controlando o agente pelo teclado, apenas pra brincar um pouco.

Tudo é configurável e executado por uma interface de terminal construída com [Textual](https://textual.textualize.io), e os resultados podem ser comparados com gráficos e estatísticas.

**Tecnologias:** Python · Textual · pytest

---

## ✨ Funcionalidades

| Área | Funcionalidade | Status |
|------|----------------|:------:|
| **Mundo** | Tamanho da grade configurável pela interface | [ ] |
| | Geração aleatória ou por *seed*, com *seed* sempre exibida e reutilizável | [ ] |
| | Quantidade de poços fixa ou proporcional ao tamanho da grade | [ ] |
| | **Wumpus móvel**, que se desloca pela caverna ao longo da expedição | [ ] |
| | **Flecha única** para o agente | [ ] |
| **Agentes lógicos** | Base de conhecimento com `TELL` / `ASK` | [ ] |
| | Motores: DPLL, Resolução (CNF) e Encadeamento para frente, selecionáveis pela interface | [ ] |
| **Agentes probabilísticos** | Motores: Enumeração e Eliminação de variáveis, selecionáveis pela interface | [ ] |
| | **Heatmap em tempo real**, embutido na própria grade (apenas no modelo probabilístico) | [ ] |
| **Interface** | Escolha do atuador (você ou um agente) | [ ] |
| | Avanço da simulação por tecla, com percepções e ações exibidas em log lateral a cada passo | [ ] |
| | Tela de benchmark: mesma configuração e mesmas seeds para todos os agentes | [ ] |
| | Métricas comparáveis: vitória, pontuação (média e desvio), mortes por poço e por Wumpus, tempo por decisão | [ ] |
| | Limite de passos e de tempo por decisão, para nenhum motor travar o benchmark | [ ] |
| | Gráficos comparativos e histórico de benchmarks salvos | [ ] |
| **Opcional** | Modo "mundo claro" (o usuário vê o mundo todo, o agente continua às cegas) | [ ] |


---

## Guia de Instalação e Execução
[Descreva os passos para instalação e execução do projeto. Inclua um passo a passo claro de como utilizar a proposta desenvolvida. Veja o exemplo abaixo.]

### 1. Instalação das Dependências
Certifique-se de ter o **Python 3.14+** instalado. Clone o repositório e instale as bibliotecas listadas no `requirements.txt`:

```bash
# Clone o repositório
git clone https://github.com/Luccas-Ribeiro/wumpus-world-project.git

# Entre na pasta do projeto
cd wumpus-world-project

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
````

### 2. Como Executar

Execute o comando abaixo no terminal para iniciar o programa:

```bash
python3 main.py
```

A interface Textual abre no terminal. Na tela de configuração você escolhe o tamanho do mundo, a quantidade de poços, a seed, o atuador (humano ou agente) e o motor de inferência.

## Estrutura dos Arquivos

[Descreva brevemente a organização das pastas]

  * `src/`: Código-fonte da aplicação ou scripts de processamento.
  * `notebooks/`: Análises exploratórias, testes e prototipagem.
  * `data/`: Datasets utilizados (se o tamanho permitir o upload).
  * `assets/`: Imagens, logos ou gráficos de resultados.

  ## 🗺️ Roadmap e TODO
  ---
  
  ### Fase 1 — Mundo (`core`)
  
  **Objetivo:** ter um mundo de Wumpus jogável e reproduzível por script, sem interface.
  
  - [ ] **1.1** `WorldConfig`: tamanho da grade, quantidade de poços **ou** proporção, e *seed* opcional.
  - [ ] **1.2** Gerador usando uma instância própria de `random.Random(seed)`, nunca o `random` global. Se não houver seed, sortear uma e guardá-la na config.
  - [ ] **1.3** Regras de posicionamento: início livre de poço e Wumpus, e ouro fora de poço.
  - [ ] **1.4** Garantir que o mundo seja **solucionável** (o ouro é alcançável sem passar por poço), regenerando de forma determinística se necessário.
  - [ ] **1.5** Percepções: brisa, fedor, brilho e grito.
  - [ ] **1.6** Ações e física: andar, girar, pegar, **atirar flecha** (uma única, acerta o primeiro Wumpus na linha de tiro) e sair.
  - [ ] **1.7** Pontuação e condições de fim de jogo (vitória, morte por poço, morte pelo Wumpus, saída sem ouro).
  - [ ] **1.8** **Wumpus móvel:** mover o Wumpus a cada *k* turnos (parâmetro de `WorldConfig`, k=1 por padrão) para uma célula vizinha livre, usando o `random.Random(seed)` do episódio, para o movimento continuar reprodutível. Reaplicar a regra de solucionabilidade (1.4) considerando que o Wumpus pode bloquear e desbloquear caminhos.
  - [ ] **1.9** Registro de partidas: salvar config + seed em JSON e permitir refazer um mundo a partir dele.
  - [ ] **1.10** **Teste obrigatório** (`tests/test_world.py`): mesma seed gera o mesmo mundo e a mesma sequência de movimentos do Wumpus. Os demais testes desta fase são opcionais.
  
  ✅ **Pronto quando:** um script roda um episódio com ações fixas, o Wumpus se move de forma determinística pela seed, e o resultado se repete usando a mesma seed.
  
  ---
  
  ### Fase 2 — Interface base e modo humano (`gui`)
  
  **Objetivo:** poder jogar e enxergar o mundo. A interface também vira a principal ferramenta de depuração das fases seguintes.
  
  - [ ] **2.1** Esqueleto do app Textual com navegação entre telas: Configuração → Jogo → Resultado.
  - [ ] **2.2** Tela de configuração: tamanho da grade, poços (quantidade ou proporção), seed (aleatória ou digitada) e seletor de atuador.
  - [ ] **2.3** Widget da grade: agente com direção, poço, Wumpus, ouro, indicadores de brisa e fedor, células visitadas e não visitadas. Cada célula deve aceitar uma **cor de fundo dinâmica**, já preparando o heatmap da Fase 6.
  - [ ] **2.4** Modo humano: controle por teclado, painel com percepções atuais, pontuação e flecha restante.
  - [ ] **2.5** Modo agente (passo a passo): uma tecla (ex.: espaço) avança uma ação do agente por vez. A cada passo, a percepção e a ação são adicionadas a um `RichLog` na lateral, para acompanhar o raciocínio em tempo real. Incluir também um modo automático com controle de velocidade.
  - [ ] **2.6** Exibir a seed da partida, com opção de copiar e de reutilizá-la na próxima.
  - [ ] **2.7** *(opcional, mas recomendado agora)* Alternância "mundo claro / escuro". No claro, o usuário vê tudo, enquanto o agente continua às cegas.
  
  ✅ **Pronto quando:** uma pessoa joga uma partida completa pela interface e consegue refazer o mesmo mundo pela seed.
  
  ---
  
  ### Fase 3 — Bases de Conhecimento (`kb`)
  
  **Objetivo:** ter a memória do agente pronta, com `TELL` e `ASK` funcionando.
  
  - [ ] **3.1** Representação de sentenças: `Literal`, `Clause` e convenção de símbolos (`P_x_y`, `B_x_y`, `S_x_y`, `W_x_y`).
  - [ ] **3.2** `KnowledgeBase` abstrata com `tell()` e `ask()`, recebendo o motor no construtor.
  - [ ] **3.3** `LogicalKB`: guarda as cláusulas e gera os axiomas do mundo para qualquer tamanho N×M. Os axiomas são: início seguro, `B ⇔ poço adjacente`, `S ⇔ Wumpus adjacente` e *exatamente um* Wumpus.
  - [ ] **3.4** `LogicalKB.tell()` traduz percepções em sentenças a cada passo.
  - [ ] **3.5** `ProbabilisticKB`: variáveis de poço com prior `p`, evidências observadas (brisas, fedores, células visitadas) e construção da rede.
  - [ ] **3.6** *(opcional)* Testes com o cenário clássico do AIMA (mundo 4×4). O mesmo exemplo já é coberto pelo teste obrigatório da tarefa 6.5.
  - [ ] **3.7** **Conhecimento revisável sobre o Wumpus:** como ele se move, separar as cláusulas sobre poços (estáticas, nunca removidas) das cláusulas sobre o Wumpus (reconstruídas a cada vez que o ambiente avisa que ele se moveu). Documentar a estratégia escolhida (ex.: descartar e reconstruir os axiomas do Wumpus vs. indexar no tempo com `W_x_y_t`).
  
  ✅ **Pronto quando:** as duas KBs aceitam percepções, entregam a consulta a um motor "dummy", e a `LogicalKB` não mantém crenças obsoletas sobre o Wumpus após ele se mover.
  
  ---
  
  ### Fase 4 — Motores lógicos (`inference/logical`)
  
  **Objetivo:** três formas de provar a mesma coisa, todas atrás da mesma interface.
  
  - [ ] **4.1** Conversor para **CNF**: eliminar `⇔` e `⇒`, aplicar De Morgan e distribuir `∨` sobre `∧`. DPLL e Resolução dependem dele.
  - [ ] **4.2** **DPLL**: propagação de unidade, símbolo puro e *backtracking*. O `entails(KB, α)` é feito checando se `KB ∧ ¬α` é insatisfazível.
  - [ ] **4.3** **Resolução por refutação**: resolve pares de cláusulas até achar a cláusula vazia, com controle contra explosão.
  - [ ] **4.4** **Encadeamento para frente**: traduzir as regras do Wumpus para cláusulas de Horn (usar símbolos positivos como `SemPoço_x_y`) e propagar até o ponto fixo.
  - [ ] **4.5** Interface comum `LogicalEngine` e registro `nome → classe`, para a GUI listar e selecionar os motores.
  - [ ] **4.6** **Teste obrigatório** (`tests/test_inference.py`): as mesmas consultas devem dar o mesmo resultado em DPLL e Resolução. Documentar onde o Encadeamento é incompleto.
  - [ ] **4.7** Instrumentação: contar inferências e medir o tempo de cada consulta. Isso alimenta as estatísticas da Fase 7.
  
  ✅ **Pronto quando:** os três motores respondem a um conjunto fixo de consultas de benchmark.
  
  ---
  
  ### Fase 5 — Agente lógico (`agents`)
  
  **Objetivo:** um agente que explora o mundo usando a KB lógica.
  
  - [ ] **5.1** `Agent` base: o ciclo `percepção → ação`.
  - [ ] **5.2** Agente aleatório, que serve de **baseline** para as estatísticas.
  - [ ] **5.3** Agente lógico: faz `TELL` das percepções e `ASK` de quais células são seguras. Mantém a fronteira de células seguras ainda não visitadas.
  - [ ] **5.4** Planejamento de caminho (BFS ou A\*) apenas por células seguras, considerando orientação e custo de giro.
  - [ ] **5.5** Política da flecha: `ASK` "o Wumpus está em (x,y)?" e atirar quando a posição for inferida. Como a flecha é única, decidir um critério de confiança mínima antes de atirar.
  - [ ] **5.6** **Wumpus móvel:** ao ser avisado de que o Wumpus se moveu (3.7), o agente deve reconsultar a KB antes de confiar numa célula como "livre de Wumpus", já que esse tipo de inferência pode ter ficado desatualizado. Crenças sobre poços continuam valendo normalmente.
  - [ ] **5.7** Política de fallback quando não há célula provadamente segura: voltar ao início e sair, ou arriscar. Definir e documentar.
  - [ ] **5.8** Integrar na GUI: usar o modo passo a passo e o log lateral da Fase 2.5 para exibir a percepção, a consulta feita à KB e a ação escolhida a cada turno.
  - [ ] **5.9** *(opcional)* Testes: com motor completo e fallback seguro, o agente lógico nunca morre quando existe caminho seguro, mesmo com o Wumpus em movimento.
  
  ✅ **Pronto quando:** pela interface dá para escolher o motor e assistir o agente jogar um episódio completo.
  
  ---
  
  ### Fase 6 — Agente probabilístico (`inference/probabilistic`)
  
  **Objetivo:** raciocínio sob incerteza, com heatmap em tempo real.
  
  - [ ] **6.1** Modelo: cada célula tem poço independente com probabilidade `p`, e a brisa é determinística em função dos vizinhos.
  - [ ] **6.2** **Inferência por enumeração**: calcular `P(Poço_x_y | evidências)` separando células de fronteira das demais.
  - [ ] **6.3** **Eliminação de variáveis**: fatores, restrição por evidência, produto, soma, normalização e ordem de eliminação.
  - [ ] **6.4** Interface comum `ProbabilisticEngine` e registro de motores para a GUI.
  - [ ] **6.5** **Teste obrigatório** (`tests/test_inference.py`): validar com o exemplo do AIMA (`p = 0,2`, brisas em duas células vizinhas à origem): ≈ 0,31 para `[1,3]` e `[3,1]` e ≈ 0,86 para `[2,2]`. Enumeração e Eliminação devem coincidir.
  - [ ] **6.6** **Wumpus móvel:** como o fedor só reflete a posição do Wumpus no momento da percepção (3.7), a evidência sobre ele deve ser descartada a cada vez que ele se move, mantendo apenas a evidência de poços (estática). Documentar essa simplificação: o heatmap trata o risco de poço, que é estável; o risco de Wumpus é tratado à parte, com a evidência mais recente apenas.
  - [ ] **6.7** Agente probabilístico: escolhe a célula de menor risco, com limiar de risco configurável, e decide quando atirar com base na probabilidade do Wumpus.
  - [ ] **6.8** **Heatmap em tempo real, embutido na grade:** a cada passo, recalcular `P(Poço_x_y | evidências)` para todas as células e atualizar a cor de fundo do widget da grade (Fase 2.3) proporcionalmente ao risco, sem abrir uma tela separada. Isso é viável porque o widget já é redesenhado a cada turno, então basta mapear probabilidade → cor (ex.: verde a vermelho) e aplicar como estilo da célula.
  - [ ] **6.9** Integrar na GUI: o heatmap aparece ligado durante toda a expedição do agente probabilístico, e desligado nos demais modos.
  
  ✅ **Pronto quando:** o agente probabilístico joga pela interface e a própria grade muda de cor a cada passo, refletindo o risco de poço em tempo real (somente neste modelo).
  
  ---
  
  ### Fase 7 — Benchmark (`simulation`)
  
  **Objetivo:** comparar os agentes de forma justa, com a mesma configuração e as mesmas seeds para todos.
  
  > **Ordem:** o **7.A** pode começar logo após a Fase 2, usando o agente aleatório. Assim o pipeline fica testado antes de existirem os agentes inteligentes. O **7.B** depende da Fase 2 (GUI base). O **7.C** depende das Fases 5 e 6.
  
  #### 7.A — Runner sem interface (`simulation/`)
  
  - [ ] **7.A.1** `BenchmarkConfig` (dataclass imutável): tamanho da grade, poços (quantidade ou proporção), quantidade de episódios, lista de seeds, combinações agente + motor, limite de passos por episódio e limite de tempo por decisão. Esse objeto é o contrato entre a GUI e o `simulation/`.
  - [ ] **7.A.2** `seeds.py`: gera a lista de seeds **uma única vez** por benchmark (faixa `0..N-1` ou lista explícita). Todos os agentes usam exatamente essa lista.
  - [ ] **7.A.3** `runner.py`: executa os episódios de cada combinação e reporta progresso por callback, para a GUI poder mostrar a barra sem depender do `runner`.
  - [ ] **7.A.4** `metrics.py`: métricas por episódio. Resultado (vitória, morte por poço, morte pelo Wumpus, sem saída, timeout), pontuação, passos, flechas usadas, células exploradas, nº de inferências e tempo por decisão.
  - [ ] **7.A.5** `stats.py`: agregação por combinação agente + motor e por configuração. Inclui taxa de vitória, pontuação média e desvio padrão, taxa de morte por poço e por Wumpus, e tempo médio por decisão.
  - [ ] **7.A.6** `storage.py`: grava em `data/benchmarks/<timestamp>/` a config (JSON), os resultados por episódio (CSV) e o resumo agregado (JSON).
  - [ ] **7.A.7** *(opcional)* Testes: a mesma config produz os mesmos resultados, e o limite de tempo encerra o episódio sem travar o benchmark.
  
  ✅ **Pronto quando:** um script roda N episódios com o agente aleatório e grava config + resultados, e rodar a mesma config de novo produz exatamente os mesmos números.
  
  #### 7.B — Tela de benchmark na GUI (`gui/screens/`)
  
  - [ ] **7.B.1** `benchmark_screen.py`: monta o `BenchmarkConfig` com tamanho, poços, número de episódios, faixa de seeds e seleção de agentes e motores. Não contém regra de experimento.
  - [ ] **7.B.2** Execução em *worker* do Textual, com barra de progresso, sem travar a interface.
  - [ ] **7.B.3** `benchmark_results.py`: tabela comparativa por combinação agente + motor, com as métricas do 7.A.5.
  - [ ] **7.B.4** Gráficos comparativos: taxa de vitória, pontuação média e tempo de decisão × tamanho da grade. Decidir entre `plotext` ou widgets próprios do Textual.
  - [ ] **7.B.5** Histórico: listar os benchmarks salvos em `data/benchmarks/` para reabrir e comparar.
  
  ✅ **Pronto quando:** pela GUI dá para configurar, rodar e comparar agentes com as mesmas seeds, e reabrir um benchmark salvo.
  
  #### 7.C — Experimentos do relatório
  
  - [ ] **7.C.1** Rodar as configurações do relatório com as mesmas seeds para todos os agentes (mínimo sugerido: 100 por configuração).
  - [ ] **7.C.2** Exportar tabelas e gráficos finais para `assets/`.
  
  ✅ **Pronto quando:** qualquer integrante reproduz as tabelas do relatório a partir de `data/benchmarks/`.
  
  ---

## Resultados e Demonstração

[Adicione prints da aplicação em execução ou gráficos com os resultados do modelo/agente. Se for uma aplicação Web, coloque um print da interface.]

## Referências

  * [Link para o Dataset original]
  * [Artigo, Documentação ou Tutorial utilizado como base]
