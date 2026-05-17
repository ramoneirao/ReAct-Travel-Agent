import sqlite3
from datetime import datetime
from langchain_core.tools import tool

DB_PATH = "database/database.sqlite"

@tool
def buscar_hoteis(destino: str, checkin: str, checkout: str, quartos: int = 1) -> str:
    """Buscar hotéis disponíveis numa cidade para datas específicas direto no banco de dados.
    
    Args:
        destino: Cidade onde quer se hospedar (ex: "Rio de Janeiro")
        checkin: Data de entrada em formato YYYY-MM-DD
        checkout: Data de saída em formato YYYY-MM-DD
        quartos: Número de quartos necessários (padrão: 1)
    """
    # Calcular a quantidade de noites
    try:
        data_checkin = datetime.strptime(checkin, "%Y-%m-%d")
        data_checkout = datetime.strptime(checkout, "%Y-%m-%d")
        noites = (data_checkout - data_checkin).days
        
        if noites <= 0:
            return "Erro: A data de checkout deve ser posterior à data de checkin."
    except ValueError:
        return "Erro: Formato de data inválido. Use YYYY-MM-DD."

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Query filtrando por cidade (destino) e disponibilidade de quartos
        query = """
            SELECT nome, estrelas, preco_noite, conforto, quartos_disponiveis 
            FROM hoteis 
            WHERE cidade = ? AND quartos_disponiveis >= ?
        """
        cursor.execute(query, (destino, quartos))
        hoteis = cursor.fetchall()
        conn.close()
        
        if not hoteis:
            return f"Desculpe, não há hotéis com {quartos} quarto(s) disponível(is) em {destino} para o período informado."
            
        resposta = f"\nHotéis disponíveis em {destino} de {checkin} a {checkout} ({noites} noites):\n\n"
        for hotel in hoteis:
            preco_total = hotel["preco_noite"] * noites * quartos
            estrelas_str = "⭐" * int(hotel["estrelas"])
            
            resposta += f" {hotel['nome']} ({estrelas_str})\n"
            resposta += f" Preço: R${hotel['preco_noite']:.2f}/noite/quarto (Total: R${preco_total:.2f} para {noites} noites)\n"
            resposta += f" Categoria: {hotel['conforto']}\n"
            resposta += f" Quartos disponíveis: {hotel['quartos_disponiveis']}\n\n"
                
        return resposta

    except sqlite3.Error as e:
        return f"Erro ao acessar o banco de dados de hotéis: {e}"

@tool
def reservar_hotel(hotel_nome: str, checkin: str, checkout: str, quartos: int, nome_hospede: str) -> str:
    """Reservar um hotel específico.
    
    Args:
        hotel_nome: Nome do hotel
        checkin: Data de entrada em formato YYYY-MM-DD
        checkout: Data de saída em formato YYYY-MM-DD
        quartos: Número de quartos
        nome_hospede: Nome do hóspede principal
    """
    # Aqui você poderia adicionar uma lógica de UPDATE no SQLite para reduzir os 'quartos_disponiveis'.
    
    # Gera um prefixo de 3 letras baseado no nome do hotel (ex: "Hotel Copacabana" -> "HOT")
    prefixo = hotel_nome.replace(" ", "")[:3].upper()
    
    return f"✅ Hotel {hotel_nome} reservado com sucesso para {nome_hospede}.\nCheck-in: {checkin} | Check-out: {checkout} ({quartos} quarto(s))\nLocalizador: HT{prefixo}5432"
