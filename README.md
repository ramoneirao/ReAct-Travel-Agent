# ReAct Travel Agent

O **ReAct-Travel-Agent** é um agente de inteligência artificial autônomo construído para atuar como um assistente de viagens inteligente. Desenvolvido com **Python** e **LangChain**, ele utiliza o padrão de raciocínio **ReAct (Reasoning and Acting)** para ir muito além de um simples chatbot.

A partir do pedido do usuário (destinos, datas e limite financeiro), o agente é capaz de raciocinar sobre o problema, utilizar ferramentas customizadas para consultar um banco de dados SQLite de voos e hotéis, calcular os gastos matematicamente e retornar a opção mais otimizada e real para a viagem.

---

## Funcionalidades e Diferenciais

- **Raciocínio Autônomo (ReAct):** O agente avalia a requisição, define os passos necessários e toma ações concretas sem intervenção humana.
- **Integração com Ferramentas (Tools):** Acesso a ferramentas de consulta em banco de dados e calculadoras matemáticas.
- **Information Retrieval Deterministico:** O LLM não "alucina" informações de viagens; ele busca dados reais/simulados em um banco SQLite, garantindo precisão.
- **Gestão de Orçamento:** Uma ferramenta específica garante que o voo e o hotel escolhidos caibam no orçamento estipulado pelo usuário.

---

## Estrutura do Projeto

O projeto adota uma arquitetura modularizada, separando claramente as responsabilidades:

```text
ReAct-Travel-Agent/
├── database/                 # O "Mundo" de dados
│   ├── make_db.py            # Script para gerar tabelas e popular o mock
│   └── database.sqlite       # Banco de dados SQLite com dados de voos/hotéis
│
├── tools/                    # As "Mãos" do agente
│   ├── __init__.py           
│   ├── voos.py               # Ferramenta de busca de voos
│   ├── hoteis.py             # Ferramenta de busca de hotéis
│   └── orcamento.py          # Ferramenta para cálculo financeiro
│
├── core/                     # O "Cérebro" do sistema
│   ├── __init__.py
│   ├── agent.py              # Inicialização do agente e do fluxo ReAct
│   └── prompts.py            # System prompts e instruções comportamentais
│
└── main.py                   # Ponto de entrada (CLI com streaming do raciocínio)
```

---

## Como executar o projeto

### Pré-requisitos
- Python 3.9+
- Chave de API de um provedor de LLM (ex: OpenAI, Anthropic, Gemini) configurada no ambiente.

### Passos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ramoneirao/ReAct-Travel-Agent.git
   cd ReAct-Travel-Agent
   ```

2. **Instale as dependências:**
   *(Certifique-se de instalar as dependências de seu gerenciador de pacotes, como `langchain`, `langgraph` e o provedor do LLM escolhido).*
   ```bash
   uv sync
   ```

3. **Crie o Banco de Dados Simulado:**
   Antes de rodar o agente, você precisa inicializar o banco de dados.
   ```bash
   uv run database/make_db.py
   ```

4. **Execute o Agente:**
   ```bash
   uv run main.py
   ```

---

## Próximos Passos (Roadmap)
- [ ] Implementar função de reserva para diminuir a quantidade de assentos e quartos disponíveis.
- [ ] Adição de Memória de Sessão para conversas contínuas.
- [ ] Integração com Gradio para interface.
