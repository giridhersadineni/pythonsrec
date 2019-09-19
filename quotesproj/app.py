from flask import Flask, escape, request,redirect, render_template
import mysql.connector
app = Flask(__name__)


@app.route('/')
def mainpage():
    return render_template("mainpage.html")


#category routes

@app.route('/categories')
def categories():
    return render_template("category/index.html")

@app.route('/categories/create')
def createcategory():
    return render_template("category/create.html")

@app.route('/categories/view')
def viewcategory():
    return render_template("category/view.html")

@app.route('/storecategory',methods=['POST'])
def storecategory():
    category=request.form.get('category')
    description=request.form.get('description')
    try:
        cnx=mysql.connector.connect(user="root",host="localhost",password="skillverse",database="quotes")
        cur=cnx.cursor()
        query="insert into categories(category name,description) values('"+category+"','"+description+"')"
        cur.execute(query)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)

    return render_template('categories/index.html')



#quotes routes
@app.route('/quotes')
def quotes():
    try:
        cnx=mysql.connector.connect(user="root",host="localhost",password="skillverse",database="quotes")
        cur=cnx.cursor()
        query="select * from quote"
        cur.execute(query)
        quotes=cur.fetchall()
        print(quotes)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)

    return render_template("quotes/index.html",quotes=quotes)

@app.route('/quotes/create')
def createquote():
    
    return render_template("quotes/create.html")



@app.route('/quotes/view/<quoteid>')
def viewquote(quoteid):
    try:
        cnx=mysql.connector.connect(user="root",host="localhost",password="skillverse",database="quotes")
        cur=cnx.cursor()
        query="select * from quote where ID="+quoteid
        cur.execute(query)
        quote=cur.fetchone()
        print(quote)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)

    return render_template("quotes/view.html",quote=quote)


@app.route('/quotes/<quoteid>/edit')
def editquote(quoteid):
    try:
        cnx=mysql.connector.connect(user="root",host="localhost",password="skillverse",database="quotes")
        cur=cnx.cursor()
        query="select * from quote where ID="+quoteid
        cur.execute(query)
        quote=cur.fetchone()
        print(quote)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)

    return render_template("quotes/edit.html",quote=quote)


@app.route('/storequote',methods=['POST'])
def storequote():
    quote=request.form.get('quote')
    author=request.form.get('author')
    category=request.form.get('category')
    keyword=request.form.get('keyword')
    try:
        cnx=mysql.connector.connect(user="root",host="localhost",password="skillverse",database="quotes")
        cur=cnx.cursor()
        query="insert into quote(quote,author,category,keyword) values('"+quote+"','"+author+"','"+category+"','"+keyword+"')"
        cur.execute(query)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)

    return render_template('quotes/index.html')

@app.route('/quotes/updatequote',methods=['post'])
def updatequote():
    quote=request.form.get('quote')
    author=request.form.get('author')
    category=request.form.get('category')
    keyword=request.form.get('keyword')
    quoteid=request.form.get('quoteid')
    try:
        cnx=mysql.connector.connect(user="root",host="localhost",password="skillverse",database="quotes")
        cur=cnx.cursor()
        query="update quote set quote='"+quote+"', author='"+author+"', category="+category+", keyword='"+keyword+"' where id="+quoteid
        print(query)
        cur.execute(query)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)



    return redirect('/quotes')



#keywords routes
@app.route('/keywords')
def keywords():
    return render_template("keywords/index.html")

@app.route('/keywords/create')
def createkeyword():
    return render_template("keywords/create.html")

@app.route('/storekeyword',methods=['POST'])
def storekeyword():
    keyword=request.form.get('keyword')

    print(keyword)
    try:
        cnx=mysql.connector.connect(user="root",host="localhost",password="skillverse",database="quotes")
        cur=cnx.cursor()
        query="insert into keywords(keyword) values('"+keyword+"')"
        cur.execute(query)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)

    return render_template('keywords/index.html')

@app.route('/keywords/view')
def viewkeyword():
    return render_template("keywords/view.html")