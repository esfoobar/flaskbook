from flask import Blueprint, render_template, request, redirect, session, flash
import bcrypt

from user.models import User
from user.forms import RegisterForm, LoginForm

user_app = Blueprint('user_app', __name__)

@user_app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.objects.filter(
            username=form.username.data,
            ).first()
        if user:
            if bcrypt.hashpw(form.password.data, user.password) == user.password:
                session['username'] = form.username.data
                flash("User %s logged in" % user.username)
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return "User logged in"
            else:
                user = None
        if not user:
            error = "Incorrect credentials"
    return render_template('user/login.html', form=form, error=error)

@user_app.route('/register', methods=('GET', 'POST'))
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            username=form.username.data,
            password=hashed_password,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        user.save()
        return "User registered"
    return render_template('user/register.html', form=form)