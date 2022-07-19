from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#this is the name of our application
app = Flask(__name__)

#form validator


#routes
@app.route('/')
@app.route("/home")
def hello():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/book",methods = ['POST'])
def book():
	#handle form data
	name = request.form.get("user_name")
	package = request.form.get("user_name")
	booking_date = request.form.get("booking_date")
	booking_time = request.form.get("booking_time")
	phone = request.form.get("phone")
	message = request.form.get("phone")

	#validate
	
	#check availability
	
	#confirm and send SMS

	#return feedback
	return render_template("index.html")

if __name__ == "__main__":
    #this gives us the details of an error when it occurs
    #it also allows the app to update on the fly
    app.run(debug=True)