#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FLASK BACKEND APP
from flask import Flask
from flask_mysqldb import MySQL
import json

app = Flask(__name__)


with open('dbconfig.json') as json_file:
    dbconfig = json.load(json_file)
app.config['MYSQL_HOST'] = dbconfig['mysql_host']
app.config['MYSQL_USER'] = dbconfig["mysql_user"]
app.config['MYSQL_PASSWORD'] = dbconfig["mysql_password"]
app.config['MYSQL_DB'] = dbconfig["mysql_db"]
mysql = MySQL(app)


from FoodApi import routes