import sqlite3
from sqlite3 import Error, sqlite_version


def createDatabase(data_base_name):
    print(f'Criando DB SqLite, {data_base_name}')

    conn = None

    try:
        conn = sqlite3.connect(data_base_name)
        print(sqlite_version)
        print(sqlite3.version_info)
    except Error as e:
        print('Error: {e}')
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    dbName = 'D:\Cursos e Estudos\curso_python\server\data\dbpy.db'
    createDatabase(dbName)
