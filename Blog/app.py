from flask import Flask
import psycopg2
from datetime import datetime
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

def get_db_connection():
    conn = psycopg2.connect(**Config.DATABASE)
    return conn
    


@app.route("/")
def hello ():
    return("Hola mundo")
    
app.run(host='0.0.0.0', port= 3000, debug= True)