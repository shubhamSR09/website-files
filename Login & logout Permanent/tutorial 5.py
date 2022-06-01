import re
from flask import Flask, redirect,render_template,request,session, url_for
from flask_mail import Mail,Message
from random import randint
import MySQLdb
from flask_mysqldb import MySQL
from datetime import timedelta

app=Flask(__name__)

mail=Mail(app)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "telematics"

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='shubhamrajput0201@gmail.com'
app.config['MAIL_PASSWORD']='975650srSR@123'                    #you have to give your password of gmail account
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours = 24)


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/", methods=['POST', 'GET'])
def home():
	if request.method == "POST":
		session.permanent = True
		user = request.form["email"]
		session["user"] = user
		otp=randint(000000,999999)
		msg=Message(subject='OTP',sender='shubhamrajput0201@gmail.com',recipients=[user])
		msg.body=str(otp)
		mail.send(msg)
		return redirect(url_for("user"))
	else:
		if "user" in session:
			return redirect(url_for("user"))

		return render_template("fpassword.html")
	return render_template("fpassword.html")


@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return render_template("dashboard.html")
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug=True)