from flask import Flask

#This line means that I want to create a web application which is a flask application
#__name__ is just representing this current file
#HEre app is just a variable and using that variable 
app = Flask(__name__)

#when the user goes to "/", i want to run the function immediately below it
#default page
#decorator
@app.route("/")
def index():
    return "Hello, world!"
 


