from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from config import Confi

app = Flask(__name__)


#Create conection whith data base
def get_db_connection():
    conn = psycopg2.connect(**Confi.DATABASE)
    return conn


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        hashed = generate_password_hash(password)
        conne = get_db_connection()
        cur = conne.cursor()
        
        try:
            cur.execute('INSERT INTO users (user_password, user_name, enmail) VALUES(%s, %s, %s)', (hashed, username, email))
            conne.commit()
            return redirect(url_for('login'))
        
        except psycopg2.IntegrityError:
            conne.rollback()
            return redirect(url_for('register'))

        finally:
            if cur:
                cur.close()
            if conne:
                conne.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conne = get_db_connection()
        cur = conne.cursor()
        cur.execute('SELECT * FROM users WHERE user_name = %s', (username,))
        user = cur.fetchone()
        cur.close()
        conne.close()

        if user and check_password_hash(user[1], password):
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/index' )
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3050, host='0.0.0.0', debug=True)