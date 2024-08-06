from . import auth
from app.forms import LoginForm
from flask import render_template, flash, session, redirect, url_for

@auth.route('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    context = {
        "login_form": login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash("Nombre de usuario registrado correctamente")
        return redirect(url_for("index"))
   
    return render_template("login.html", **context)