from langchain_core.tools import tool

@tool
def calcular_orcamento(voo_preco: float, hotel_preco_total: float) -> str:
    """Calcular o orçamento total estimado da viagem.
    
    Args:
        voo_preco: Preço total dos voos (já multiplicado pelos passageiros)
        hotel_preco_total: Preço total da hospedagem (já multiplicado pelas noites/quartos)
    """
    total = voo_preco + hotel_preco_total
    
    return f"""
RESUMO DO ORÇAMENTO:
---------------------------
Voos:  R$ {voo_preco:.2f}
Hotel: R$ {hotel_preco_total:.2f}
---------------------------
TOTAL: R$ {total:.2f}
"""
