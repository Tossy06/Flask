from flask import Flask, request, redirect, url_for, render_template, session, flash
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

app = Flask(__name__)
app.secret_key = 'supersecretKey'

def get_db_connection():
    conn = psycopg2.connect(**Config.DATABASE)
    return conn

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conne = get_db_connection()
        cur = conne.cursor()

        cur.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cur.fetchone()
        cur.close()
        conne.close()

        if user and check_password_hash(user[2], password):  # Asume que la contraseña está en la tercera columna
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            return render_template('error.html')
        
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
            cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
            conne.commit()
            flash('Registration successful', 'success')
            return redirect(url_for('login'))
        except psycopg2.IntegrityError:
            conne.rollback()
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        finally:
            cur.close()
            conne.close()

    return render_template('register.html')

app.run(host='0.0.0.0', port=3050, debug=True)
