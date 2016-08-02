from flask_wtf import Form
from wtforms import StringField, BooleanField, validators, SubmitField, PasswordField


class LoginForm(Form):
    loginname = StringField('Login Name', validators=[validators.data_required()])
    password = PasswordField('Password', validators=[validators.data_required()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Submit')
