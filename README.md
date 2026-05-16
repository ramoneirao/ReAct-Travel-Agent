# ReAct-Travel-Agent
Um agente inteligente autônomo baseado na arquitetura ReAct para buscar, planejar e reservar voos e hotéis utilizando LangChain e LLMs.

---

## Estrutura do Projeto

```python
chat-bot/
├── database/                 
│   ├── make_db.py            
│   └── database.sqlite       
│
├── tools/                    
│   ├── __init__.py           
│   ├── voos.py               
│   ├── hoteis.py             
│   └── orcamento.py          
│
├── core/                     
│   ├── __init__.py
│   ├── agent.py              
│   └── prompts.py            
│
└── main.py                   
```