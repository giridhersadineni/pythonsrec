import mysql.connector
cnx = mysql.connector.connect(host="127.0.0.1",user="root",password="skillverse",database="inspire")
cur=cnx.cursor()
author=input("enter the name of the author")
quote=input("Quote:")
query="insert into quotes(author,quote) values('"+author+"','"+quote+"')"
cur.execute(query)
cnx.commit()
cnx.close()
