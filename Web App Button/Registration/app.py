from flask import Flask, render_template, request
app = Flask(__name__)
import MySQLdb
from flask_mysqldb import MySQL

app =Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "telematics"


#define actuators GPIOs
ledRed = 130
ledYlw = 19
ledGrn = 26
ledBlu = 10
#initialize LED status variables
ledRedSts = 0
ledYlwSts = 0
ledGrnSts = 0
ledredcheck=1
ledYlwcheck=1
ledGrncheck=1
ledBlucheck=1
devices={'ledRed':1, 'ledYlw':1, 'ledGrn':1, 'ledBlu':1}
device=0
@app.route("/")
def index():
	#Read GPIO Status
#	LedSts = LED.input
    ledRedSts = devices['ledGrn']
    ledYlwSts = devices['ledGrn']
    ledGrnSts = devices['ledGrn']
    ledBluSts = devices['ledBlu']
    print(devices)
    templateData = {
      		'ledRed'  : ledRedSts,
      		'ledYlw'  : ledYlwSts,
      		'ledGrn'  : ledGrnSts,
            'ledBlu'  : ledBluSts,
            'ledredcheck':ledredcheck,
            'ledYlwcheck':ledYlwcheck,
            'ledGrncheck':ledGrncheck,
            'ledBlucheck':ledGrncheck
            }
    return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'ledRed':
        actuator = ledRed
    if deviceName == 'ledYlw':
        actuator = ledYlw
    if deviceName == 'ledGrn':
        actuator = ledGrn
    if deviceName == 'ledBlu':
        actuator = ledBlu
    if action == "on":
        devices[deviceName]=1 #update annc 1
        cur = mysql.connection.cursor()
        cur.execute("UPDATE newled Set "+deviceName+ "= 1")
        mysql.connection.commit()
        cur.close()
    if action == "off":
        devices[deviceName]=0 #update dkjbjkds 0
        cur = mysql.connection.cursor()
        cur.execute("UPDATE newled Set "+deviceName+ "= 0")
        mysql.connection.commit()
        cur.close()
    ledRedSts = devices['ledRed']
    ledYlwSts = devices['ledYlw']
    ledGrnSts = devices['ledGrn']
    ledBluSts = devices['ledBlu']
    templateData = {
      		'ledRed'  : ledRedSts,
      		'ledYlw'  : ledYlwSts,
      		'ledGrn'  : ledGrnSts,
            'ledBlu'  : ledBluSts,
            'ledredcheck':ledredcheck,
            'ledYlwcheck':ledYlwcheck,
            'ledGrncheck':ledGrncheck,
            'ledBlucheck':ledBlucheck
            
            }	   
    print(devices)
    return render_template('index.html', **templateData)  
    
if __name__ == "__main__":
   app.run( debug=True)