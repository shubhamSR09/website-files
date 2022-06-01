from os import name
from typing import Dict
from flask import Flask, render_template, request
import MySQLdb
from flask_mysqldb import MySQL

app =Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "telematics"


mysql = MySQL(app)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        fname=request.form['fname']
        lname=request.form['lname']
        gender=request.form['gender']
        email=request.form['email']
        number=request.form['number']
        pwd=request.form['pwd']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO registration (Fname,Lname,Gender,Email,PhoneNo,Password) VALUES (%s,%s,%s,%s,%s,%s)",(fname,lname,gender,email,number,pwd))
        mysql.connection.commit()
        cur.close()

        conn = MySQLdb.connect("localhost", "root", "", "telematics")
        cursor=conn.cursor(MySQLdb.cursors.DictCursor)
        #dbcon = MySQLdb.connect("localhost", "root", "", "demo")
        #cur = dbcon.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute("SELECT email FROM registration")
        users = cursor.fetchall()
        print(type(users))

        
       

        

    return render_template("new_registration.html")
        

        
if __name__ == "__main__":
    app.run(debug=True)


      