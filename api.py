from flask import Flask, render_template, request, redirect, url_for
from models.model import user_exists, create_user, login_user

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html', title='Sign-in')

@app.route('/login', methods=['POST'])
def login():

	#user = { 'username': 'tashvin','password' : '1234'}
	if request.method == 'POST':

		username = request.form['username']
		password = request.form['password']

		user = login_user(username)

		if user is None:
			return "User does not exists"

		if user['username'] == username and user['password'] == password:
				return "User logged in successfully"
	else:
		return redirect(url_for('home'))

@app.route('/signup', methods=['POST'])
def signup():

	user_info = {}

	user_info['username'] = request.form['username']
	user_info['email'] = request.form['email']
	user_info['password'] = request.form['password']
	rpassword = request.form['rpassword']
	
	if user_exists(user_info['username']) is False:
		if user_info['password'] == rpassword:
			create_user(user_info)
			return "user created"

if __name__ == '__main__':
	app.run(debug=True)