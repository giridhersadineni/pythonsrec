from flask import Flask, escape, request,render_template
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

@app.route('/quotes/view')
def viewquote():
    return render_template("quotes/view.html")

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
        query="insert into keywords(keyword,category) values('"+keyword+"','"+category+"')"
        cur.execute(query)
        cur.close()
        cnx.commit()
    except mysql.connector.Error as e:
        print(e)

    return render_template('keywords/index.html')

@app.route('/keywords/view')
def viewkeyword():
    return render_template("keywords/view.html")