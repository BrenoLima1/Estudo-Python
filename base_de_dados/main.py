# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
import pymysql
from dotenv import load_dotenv
from pymysql.cursors import DictCursor


TABLE_NAME = 'customers'  # corrigi o nome

# Carrega as variáveis do .env
load_dotenv()

connection = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    charset=os.getenv("DB_CHARSET"),
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                idade INT NOT NULL
            )
            '''
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit()

    with connection.cursor() as cursor:
        # sql =   f'''
        #     INSERT INTO {TABLE_NAME} (nome, idade) VALUES
        #     (%s, %s)
        #     '''
        sql_chave_dicionario = f'''
            INSERT INTO {TABLE_NAME} (nome, idade) VALUES
            ( %(nome)s, %(idade)s)
            '''

        # data = (('Breno', 27), ('Ana', 32), ('Carlos', 35))
        data_json = (
            {'nome': 'Breno', 'idade': 27},
            {'nome': 'Ana', 'idade': 32},
            {'nome': 'Carlos', 'idade': 38}
        )
        cursor.executemany(sql_chave_dicionario, data_json)
        connection.commit()

        #Ler dados da tabela
        query = f'SELECT * FROM {TABLE_NAME} WHERE idade >= %s'
        idade_maxima = (30)
        cursor.execute(query, idade_maxima)
        resultados = cursor.fetchall()
        for row in resultados:
            id, name, age = row.keys()
            print(f'ID: {row[id]}, Nome: {row[name]}, Idade: {row[age]}')

        # deletar dados da tabela
        delete_query = f'DELETE FROM {TABLE_NAME} WHERE nome = %s'
        nome_deletar = 'Ana'
        cursor.execute(delete_query, nome_deletar)
        connection.commit()

        #  atualizar dados
        update_query = f'UPDATE {TABLE_NAME} SET nome = %s WHERE id = %s'
        novo_nome = 'João Pedro'
        id_atualizar = 3
        cursor.execute(update_query, (novo_nome, id_atualizar))
        connection.commit()

print("Tabela criada e dados inseridos com sucesso!")
