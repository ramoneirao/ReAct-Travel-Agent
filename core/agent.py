import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools.voos import buscar_voos, reservar_voo
from tools.hoteis import buscar_hoteis, reservar_hotel
from tools.orcamento import calcular_orcamento
from core.prompts import SYSTEM_PROMPT

# Carrega as variáveis do arquivo .env
load_dotenv()

def create_travel_agent():
    # Inicializar o modelo LLM apontando para o OpenRouter
    model = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model="baidu/cobuddy:free", 
        temperature=0
    )
    
    # Criar o agente com as ferramentas
    agent = create_agent(
        model=model, 
        tools=[
            buscar_voos, 
            buscar_hoteis, 
            reservar_voo, 
            reservar_hotel, 
            calcular_orcamento
        ],
        system_prompt=SYSTEM_PROMPT
    )
    return agent
