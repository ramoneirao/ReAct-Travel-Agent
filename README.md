# ReAct-Travel-Agent
Um agente inteligente autônomo baseado na arquitetura ReAct para buscar, planejar e reservar voos e hotéis utilizando LangChain e LLMs.

---

## Estrutura do Projeto

chat-bot/
├── database/                 # Tudo relacionado aos dados
│   ├── make_db.py            # O script que usamos para gerar as tabelas
│   └── database.sqlite       # O arquivo de banco de dados gerado
│
├── tools/                    # Ferramentas do agente separadas por contexto
│   ├── __init__.py           
│   ├── voos.py               # buscar_voos, reservar_voo
│   ├── hoteis.py             # buscar_hoteis, reservar_hotel
│   └── orcamento.py          # calcular_orcamento
│
├── core/                     # O cérebro do seu bot
│   ├── __init__.py
│   ├── agent.py              # Inicializa o LLM, puxa as tools e cria o Agente ReAct
│   └── prompts.py            # Guarda os System Prompts 
│
└── main.py                   # Ponto de entrada do programa
