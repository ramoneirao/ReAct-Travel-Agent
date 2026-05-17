from core.agent import create_travel_agent

def main():
    agent = create_travel_agent()
    
    # Pergunta do usuário
    pergunta = """
    Olá! Preciso viajar de São Paulo para Rio de Janeiro no dia 15 de janeiro de 2026.
    Vou ficar 2 noites (checkin dia 15, checkout dia 17).
    Meu orçamento é de R$500,00.
    Reserve para mim a melhor opção.
    """
    
    print("=" * 80)
    print("USUARIO:", pergunta)
    print("-" * 80)
    print("\n AGENTE PENSANDO E AGINDO...\n")
    
    # Executar o agente com streaming para ver cada passo
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": pergunta}]}, stream_mode="values"
    ):
        latest_message = chunk["messages"][-1]
        
        # Se é resposta do agente
        if hasattr(latest_message, "content") and latest_message.content:
            print(f"Agente: {latest_message.content}\n")
        
        # Se está chamando ferramentas
        if hasattr(latest_message, "tool_calls") and latest_message.tool_calls:
            for tool_call in latest_message.tool_calls:
                print(f"[Ferramenta] chamando {tool_call['name']} com argumentos: {tool_call['args']}")

if __name__ == "__main__":
    main()
