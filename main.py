from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5



class LoginForm(FlaskForm):
    email = StringField('Email',  validators=[DataRequired(), Email(message='invalid email')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message='password must be at least 8 characters')])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = ".......your_pass....."
ADMIN_MAIL = 'admin@email.com'
ADMIN_PASS = '12345678'
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == ADMIN_MAIL and password == ADMIN_PASS:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
