import sqlite3
from models.animal import Animal

DB_NAME = "database.db"

def criar_tabela_animais():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS animais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            dono_id INTEGER,
            FOREIGN KEY (dono_id) REFERENCES usuarios(id)
        )
    """)
    conn.commit()
    conn.close()

def adicionar_animal(animal: Animal):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animais (nome, especie, descricao, preco, dono_id) VALUES (?, ?, ?, ?, ?)",
                   (animal.nome, animal.especie, animal.descricao, animal.preco, animal.dono_id))
    conn.commit()
    conn.close()

def listar_animais():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, especie, descricao, preco, dono_id FROM animais")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nome": r[1], "especie": r[2], "descricao": r[3], "preco": r[4], "dono_id": r[5]} for r in rows]
