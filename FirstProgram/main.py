from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from Blog.app import create_app
from app.forms import LoginForm

app = create_app()
items = ["ARROZ", "HUEVOS", "LECHE", "AVENA"]

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error = error)

@app.route("/index")
def index ():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    session["user_ip_infromation"] = user_ip_information
    return response
    
@app.route("/show_information_address")
def show_infromation():
    user_ip = session.get("user_ip_infromation")
    username =session.get("username")
  
    context = {
        "user_ip": user_ip,
        "items": items,
        "username": username
    }
    return render_template("ip_information.html", **context)
   
app.run(host='0.0.0.0', port= 3000, debug= True)