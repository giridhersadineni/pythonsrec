from flask import Flask, escape, request,render_template

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



#quotes routes
@app.route('/quotes')
def quotes():
    return render_template("quotes/index.html")

@app.route('/quotes/create')
def createquote():
    return render_template("quotes/create.html")

@app.route('/quotes/view')
def viewquote():
    return render_template("quotes/view.html")


