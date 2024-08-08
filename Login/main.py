from flask import Flask, request, redirect, url_for, render_template, session, flash
import psycopg2
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'supersecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://david:Santi_Aleja@localhost/login_db'
db = SQLAlchemy(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            db.session.execute('INSERT INTO users (username, password) VALUES (%s, %s)', username, password)
            db.session.commit()
            flash('Registration successful!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('An error occurred: ' + str(e), 'danger')

    return render_template('register.html')
app.run(host='0.0.0.0', port='3050', debug= True)