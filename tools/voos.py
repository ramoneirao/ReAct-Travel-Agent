import sqlite3
from langchain_core.tools import tool

DB_PATH = "database/database.sqlite"

@tool
def buscar_voos(origem: str, destino: str, data_ida: str, passageiros: int = 1) -> str:
    """Buscar voos disponíveis entre duas cidades numa data específica direto no banco de dados.
    
    Args:
        origem: Cidade de origem (ex: "São Paulo")
        destino: Cidade de destino (ex: "Rio de Janeiro")
        data_ida: Data do voo em formato YYYY-MM-DD
        passageiros: Número de passageiros (padrão: 1)
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        # Permite acessar as colunas por nome como se fosse um dicionário: linha["preco"]
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        
        # Query filtrando por origem, destino, data e se há assentos suficientes
        query = """
            SELECT id, horario, preco, assentos 
            FROM voos 
            WHERE origem = ? AND destino = ? AND data = ? AND assentos >= ?
        """
        cursor.execute(query, (origem, destino, data_ida, passageiros))
        voos = cursor.fetchall()
        conn.close()
        
        if not voos:
            return f"Desculpe, não há voos disponíveis de {origem} para {destino} em {data_ida} para {passageiros} passageiro(s)."
        
        resposta = f"\nVoos disponíveis de {origem} para {destino} em {data_ida}:\n\n"
        for voo in voos:
            preco_total = voo["preco"] * passageiros
            resposta += f" ID: {voo['id']} | Horário: {voo['horario']} | R${voo['preco']:.2f}/pessoa (Total: R${preco_total:.2f}) | Assentos Livres: {voo['assentos']}\n"
        
        return resposta

    except sqlite3.Error as e:
        return f"Erro ao acessar o banco de dados de voos: {e}"


@tool
def reservar_voo(voo_id: str, passageiros: int, nome_passageiro: str) -> str:
    """Reservar um voo específico.
    
    Args:
        voo_id: ID do voo (ex: "VG001")
        passageiros: Número de passageiros
        nome_passageiro: Nome do passageiro principal
    """
    # Aqui você poderia adicionar uma lógica de UPDATE no SQLite para reduzir os 'assentos' disponíveis, se desejar.
    
    return f"✅ Voo {voo_id} reservado com sucesso para {nome_passageiro} ({passageiros} passageiro(s)).\nLocalizador de reserva: BR{voo_id}789"
