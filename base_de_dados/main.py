# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
import pymysql
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

connection = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    charset=os.getenv("DB_CHARSET")
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute( '''
            CREATE TABLE IF NOT EXISTS custumers(
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            nome varchar(50) NOT NULL,
            idade INT NOT NULL
            )
            '''
        )
        connection.commit()
        print(cursor)
