from sqlite3 import connect
import firebirdsql

conn = firebirdsql.connect(
    host="localhost",
    port=3050,
    database="C:\Syspro\Server\Data\SYSPRO.FDB",
    user="SYSDBA",
    password="Trilink098")

cur=conn.cursor()
cur.execute("Select * from participante")
for c in cur.fetchall():
    print(c)



# Connecting via 'dsn'

#con = fdb.connect(dsn='/path/database.fdb', user='sysdba', password='pass')# Local database (local protocol, if supported)
#con = fdb.connect(dsn='localhost:/path/database.fdb', user='sysdba', password='pass')# Local database (TCP/IP)
#con = fdb.connect(dsn='localhost/3050:/path/database.fdb', user='sysdba', password='pass')# Local database (TCP/IP with port specification)
#con = fdb.connect(dsn='host:/path/database.db', user='sysdba', password='pass')# Remote database
#con = fdb.connect(dsn='host/3050:/path/database.db', user='sysdba', password='pass')# Remote database with port specification

# Connecting via 'database', 'host' and 'port'

#con = fdb.connect(database='/path/database.db', user='sysdba', password='pass')# Local database (local protocol, if supported)
#con = fdb.connect(host='localhost', database='/path/database.db', user='sysdba', password='pass')# Local database (TCP/IP)
#con = fdb.connect(host='localhost', port=3050, database='/path/database.db', user='sysdba', password='pass')# Local database (TCP/IP with port specification)
#con = fdb.connect(host='myhost', database='/path/database.db', user='sysdba', password='pass')# Remote database

