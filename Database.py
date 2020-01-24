#! /usr/bin/python3
import pymysql

# config = {
#     'user':'Alvo',
#     'password':'S@naipei',
#     'host':'127.0.0.1',
#     'database':'wizard'
# }
# con = pymysql.connect(**config)
con = pymysql.connect(host="localhost", database="mystore", user="Alvo", password="McDoogle")
cur = con.cursor()
#cur.execute("CREATE TABLE boys(name varchar(20))")
#cur.execute("insert into boys values('alvin')")
cur.execute("describe customers")
for data in cur:
    print(data)