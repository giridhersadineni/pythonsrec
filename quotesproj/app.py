from flask import Flask, escape, request,render_template

app = Flask(__name__)

@app.route('/')
def submitquote():
    return render_template("submitquote.html")