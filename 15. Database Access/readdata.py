import mysql.connector

cnx = mysql.connector.connect(host="127.0.0.1",user="root",password="skillverse",database="inspire")
cur=cnx.cursor()
cur.execute("select * from quotes")
quotes=cur.fetchall()
for quote in quotes:
    print(quote[2],":",quote[1])
cnx.close()
