from flask import Flask, escape, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ff8256d2711eca644d87f3903757b839'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from forms import RegistrationForm, LoginForm
from datetime import datetime

posts = [
	{
		'author': 'Eva Nanyonga',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'July 21st 2019'
	},
	{
		'author': 'Mary Jane',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'July 29th, 2019'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html',
							posts=posts
							)

@app.route('/about')
def about():
	return render_template('about.html',
							title='About'
							)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html',
							title='Register',
							form=form
							)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'evewish@gmail.com' and form.password.data == 'allahu':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html',
							title='Login',
							form=form
							)


if __name__ == '__main__':
	app.run(debug=True)