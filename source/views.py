from . import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	posts = [
		{
			'user': 'Anon',
			'time': '21:00',
			'date': '26th Semptember',
			'message': 'Test message'
			'verify': 'Verify',
			'unverify': 'Unverify'
		}
	]
	return render_template('index.html', posts=posts)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404