from app import app, login_manager
from flask import render_template, flash, redirect, url_for
from app.models.forms import LoginForm
from app.models.tables import User
from flask_login import login_user, logout_user


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route('/', defaults={'user': None})
@app.route('/index/<user>')
def index(user):
    return render_template('index.html', user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid Login')
            return 'erro'
    else:
        return render_template('login.html', form=form)


def load_user(user_id):
    return User.get(user_id)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
