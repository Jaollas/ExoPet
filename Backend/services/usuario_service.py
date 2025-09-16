import sqlite3
from models.usuario import Usuario

DB_NAME = "database.db"

def criar_tabela_usuarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def adicionar_usuario(usuario: Usuario):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                   (usuario.nome, usuario.email, usuario.senha))
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, senha FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nome": r[1], "email": r[2], "senha": r[3]} for r in rows]
