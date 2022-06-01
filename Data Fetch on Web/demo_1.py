from typing import Dict
from flask import Flask, render_template, request
import MySQLdb
from flask_mysqldb import MySQL

app =Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "demo"


mysql = MySQL(app)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        pwd=request.form['pwd']
        #imgPath=%path known%+%filename%
        
        
        

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO regiatration (Fname,Lname,email,pwd) VALUES (%s,%s,%s,%s)",(fname,lname,email,pwd))
        mysql.connection.commit()
        cur.close()

        conn = MySQLdb.connect("localhost", "root", "", "demo")
        cursor=conn.cursor(MySQLdb.cursors.DictCursor)
        #dbcon = MySQLdb.connect("localhost", "root", "", "demo")
        #cur = dbcon.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute("SELECT email FROM regiatration")
        users = cursor.fetchall()
        
        
        
        #users=cur.execute("SELECT * FROM regiatration")
        print(type(users))
        print(users)

        
        if email== "shubhamrajput@gmail.com":
            return render_template("login.html")
        else:
            return render_template("error.html")

        return render_template("users.html", userDetails=users)#userDetails=users
    

    return render_template("registration.html")











if __name__ == "__main__":
    app.run(debug=True)
