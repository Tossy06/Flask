from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener datos del formulario
        username = request.form['username']
        password = request.form['password']
        # Aquí puedes añadir la lógica de autenticación
        if username == 'David' and password == '1234':
            return render_template('user.html', username = username)
        else:
            return render_template('error.html')
    
    # Mostrar el formulario
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3050', debug=True)