from distutils.util import execute
import sqlite3
from sqlite3 import Error

# Criando conexão
def ConexaoBanco():
    caminho = 'D:\\Cursos e Estudos\\curso_python\\server\\data\\dbpy.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print(ex)

# Criando Tabela
vsql = """CREATE TABLE IF NOT EXISTS cst_icms(
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo    INTEGER NOT NULL,
        descricao VARCHAR (200),
        data      DATE    NOT NULL)"""

criarTabela(vcon, vsql)

vcon.close()
