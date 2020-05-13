from flask import *

app= Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/register')
def register():
	return render_template('register.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/demo')
def demo():
	return render_template('demo.html')

@app.route('/login')
def login():
	return render_template('login.html')
if __name__=='__main__':
	app.run(debug=True)
