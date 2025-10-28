import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
BD_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'custumers'

connection = sqlite3.connect(BD_FILE)
cursor = connection.cursor()

# Também pode deletar a tabela inteira
cursor.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')
connection.commit()

# CUIDADO: Fazer delete sem where
# cursor.execute(f'DELETE FROM {TABLE_NAME}')
# connection.commit()

# Cuidado com sql injection (usar sempre parâmetros)
# Cria a tabela
cursor.execute(f'''
               CREATE TABLE IF NOT EXISTS {TABLE_NAME}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                weight REAL
                )
                ''')
connection.commit()

#  Insere na tabela
sql = f'''
               INSERT INTO {TABLE_NAME} (name, weight)
               VALUES
               (:nome, :peso)
               '''
# cursor.execute(sql, ('Buddha', 80.5,
#                'Ana', 63.5,
#                'João', 85))

# ou
connection.executemany(sql, [
    {'nome': 'Buddha', 'peso': 80.5},
    {'nome': 'Ana', 'peso': 63.5},
    {'nome': 'João', 'peso': 85}
])
connection.commit()

# Seleciona na tabela

sql = f'SELECT * FROM {TABLE_NAME} WHERE ? > ?'
cursor.execute(sql, ('weight', 70))

for linha in cursor.fetchall():
    print(linha)

# UPDATE
sql = f'UPDATE {TABLE_NAME} SET weight = :peso WHERE name = :nome'
cursor.execute(sql, {'peso': 60, 'nome': 'Ana'})
connection.commit()

cursor.close()
connection.close()
