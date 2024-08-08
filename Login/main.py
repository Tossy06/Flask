from flask import Flask, request, redirect, url_for, render_template, session, flash
import psycopg2
from werkzeug.security import generate_password_hash
from config import Config
app = Flask(__name__)
app.secret_key = 'supersecretKey'

def get_db_connection():
    conn = psycopg2.connect(**Config.DATABASE)
    return conn

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        conne = get_db_connection()
        cur = conne.cursor()
        try:
            cur.execute('INSERT INTO users (username, password) VALUES (%s,%s)', (username, hashed_password))
            conne.commit()
        except psycopg2.IntegrityError:
            conne.rollback()
            flash('Username already exists', 'danger')
        finally:
            cur.close()
            conne.close()
        flash('Registration successful')
        
    return render_template ('register.html')

app.run(host='0.0.0.0', port='3050', debug= True)