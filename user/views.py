from flask import Blueprint, render_template
import bcrypt

from user.models import User
from user.forms import RegisterForm

user_app = Blueprint('user_app', __name__)

@user_app.route('/login')
def user_login():
    return "User login"
    
@user_app.route('/register', methods=('GET', 'POST'))
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            form.username.data,
            hashed_password,
            form.email.data,
            form.first_name.data,
            form.last_name.data,
        )
        user.save()
        return "User registered"
    return render_template('user/register.html', form=form)