import sqlite3
from sqlite3 import Error

# Criando conexão
def ConexaoBanco():
    caminho = 'D:\\Cursos e Estudos\\curso_python\\server\\data\\dbpy.db'
    con = None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()

codigo=input("Coódigo")
descricao=input("Descrição")
data=input("Data")

vsql="INSERT INTO CST_ICMS(codigo, descricao, data)VALUES('"+codigo+"','"+descricao+"','"+data+"')"

def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql) #execute é um metodo do cursor
        conexao.commit()
        print('Registro Inserido')
    except Error as ex:
        print(ex)
inserir(vcon,vsql)