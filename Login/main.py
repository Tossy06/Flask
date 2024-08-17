from flask import Flask, request, redirect, url_for, render_template, session, flash
import psycopg2
from werkzeug.security import generate_password_hash
from config import Config
app = Flask(__name__)
app.secret_key = 'supersecretKey'

def get_db_connection():
    conn = psycopg2.connect(**Config.DATABASE)
    return conn


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conne = get_db_connection()
        cur = conne.cursor()
        try:
            cur.execute(f'SELECT *FROM users WHERE username=%s AND password=%s',(username, password))
        except psycopg2.IntegrityError:
            conne.rollback()
            flash('Username already exists', 'danger')
            
        
        user = cur.fetchone()
        cur.close()
        conne.close()
        
        if user:
             # Si el usuario existe, se inicia sesión
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index.html'))
        else:
            flash('Invalid username or password', 'danger')
        
    return render_template('login.html')





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