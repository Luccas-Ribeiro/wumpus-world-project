# Wumpus World

**Disciplina:** Introdução à Inteligência Artificial  
**Semestre:** 2026.2  
**Professor:** Andre Luis Fonseca Faustino 
**Turma:** T01

## Integrantes do Grupo
* Lucas Emanuel da Paz Ribeiro (20250051945)
* Erick Alberth da Silva Santos (20250044619)
* Pedro Vitor de Oliveira Moura (20230036093)

## Descrição do Projeto
Este projeto implementa o **Mundo de Wumpus**, um clássico da IA em que um agente explora uma caverna em grade às cegas, sem saber onde estão os poços nem o Wumpus. O objetivo é pegar o ouro e voltar à saída com vida, usando apenas as percepções locais (brisa perto de poços, fedor perto do Wumpus, brilho do ouro, impacto quando a flecha atinge uma parede e grito quando o Wumpus é atingido pela flecha).

O foco do trabalho é **comparar formas de raciocinar sob incerteza**. O mesmo mundo pode ser explorado por:

* **Agentes lógicos**, que mantêm uma base de conhecimento em lógica proposicional e só se movem para células provadamente seguras. Os motores de inferência disponíveis são Forward Chaining, Resolução por refutação e DPLL.
* **Agentes probabilísticos**, que estimam a probabilidade de poço em cada célula e escolhem o caminho de menor risco. Os motores são Inferência por enumeração e Eliminação de variáveis.
* **Você mesmo**, controlando o agente pelo teclado, apenas pra brincar um pouco.

Tudo é configurável e executado por uma interface de terminal construída com [Textual](https://textual.textualize.io), e os resultados podem ser comparados com gráficos e estatísticas.

**Tecnologias:** Python · Textual · pytest

## Guia de Instalação e Execução
[Descreva os passos para instalação e execução do projeto. Inclua um passo a passo claro de como utilizar a proposta desenvolvida. Veja o exemplo abaixo.]

### 1. Instalação das Dependências
Certifique-se de ter o **Python 3.14+** instalado. Clone o repositório e instale as bibliotecas listadas no `requirements.txt`:

```bash
# Clone o repositório
git clone https://github.com/Luccas-Ribeiro/world-of-wumpus-project.git

# Entre na pasta do projeto
cd world-of-wumpus-project

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

## Resultados e Demonstração

[Adicione prints da aplicação em execução ou gráficos com os resultados do modelo/agente. Se for uma aplicação Web, coloque um print da interface.]

## Referências

  * [Link para o Dataset original]
  * [Artigo, Documentação ou Tutorial utilizado como base]
