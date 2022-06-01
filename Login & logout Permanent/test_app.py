
from distutils.log import error
import email
import profile
import re
from flask import Flask, redirect,render_template,request,session, url_for
from flask_mail import Mail,Message
from random import randint
import MySQLdb
from flask_mysqldb import MySQL
from datetime import timedelta

app=Flask(__name__)

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "telematics"

mail=Mail(app)
mysql = MySQL(app)


app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='shubhamrajput0201@gmail.com'
app.config['MAIL_PASSWORD']='975650srSR@123'                    #you have to give your password of gmail account
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours = 24)

mail=Mail(app)

otp=randint(000000,999999) 


@app.route('/')
def index():
    
    return render_template("fpassword.html")

@app.route('/validate',methods=['POST'])
def validate():
    error="Please Try Again"
    user_otp=request.form['otp']
    if otp==int(user_otp):
        
        return redirect(url_for("dashboard"))
    return render_template("otp.html",error=error)


@app.route('/verify',methods=["POST","GET"])
def verify():
        global email
        if request.method == "POST": 
            session.permanent = True
            email=request.form['email']
            
            #num=request.form['number']
            msg=Message(subject='OTP',sender='shubhamrajput0201@gmail.com',recipients=[email])
            msg.body=str(otp)
            mail.send(msg)

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO newtable (Email,OTP) VALUES (%s,%s)",(email,otp))
            mysql.connection.commit()
            cur.close()

            return render_template('otp.html')
        else:
            if "user" in session:
                return redirect(url_for("validate"))

@app.route('/logout')
def logout():
    session.pop('email',None,)
    return render_template("fpassword.html")


@app.route('/dashboard')
def dashboard():
    
    return render_template("dashboard.html")

@app.route('/profile',methods=["POST","GET"])
def profile():
    name=""
    if request.method=="POST":
        name=request.form["name"]
        
    return render_template('dashboard.html', name=name)

if __name__ == "__main__":
    app.secret_key = 'shubu'
    app.debug = True
    app.run()

