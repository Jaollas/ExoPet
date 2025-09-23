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

def obter_animal_por_id(animal_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, especie, descricao, preco, dono_id FROM animais WHERE id = ?", (animal_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nome": row[1], "especie": row[2], "descricao": row[3], "preco": row[4], "dono_id": row[5]}
    return None

def listar_animais(dono_id: int | None = None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if dono_id:
        cursor.execute("SELECT id, nome, especie, descricao, preco, dono_id FROM animais WHERE dono_id = ?", (dono_id,))
    else:
        cursor.execute("SELECT id, nome, especie, descricao, preco, dono_id FROM animais")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nome": r[1], "especie": r[2], "descricao": r[3], "preco": r[4], "dono_id": r[5]} for r in rows]

def atualizar_animal(animal_id: int, animal: Animal, usuario_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT dono_id FROM animais WHERE id = ?", (animal_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return False, "Animal não encontrado"
    if row[0] != usuario_id:
        conn.close()
        return False, "Usuário não autorizado"

    cursor.execute("""
        UPDATE animais 
        SET nome=?, especie=?, descricao=?, preco=?
        WHERE id=? AND dono_id=?
    """, (animal.nome, animal.especie, animal.descricao, animal.preco, animal_id, usuario_id))
    conn.commit()
    conn.close()
    return True, "Animal atualizado com sucesso"

def deletar_animal(animal_id: int, usuario_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT dono_id FROM animais WHERE id = ?", (animal_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return False, "Animal não encontrado"
    if row[0] != usuario_id:
        conn.close()
        return False, "Usuário não autorizado"

    cursor.execute("DELETE FROM animais WHERE id=?", (animal_id))
    conn.commit()
    conn.close()
    return True, "Animal removido com sucesso"
