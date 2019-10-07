from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #flask will look for index.html immediately inside a subdirectory called templates 
    return render_template("index.html")
