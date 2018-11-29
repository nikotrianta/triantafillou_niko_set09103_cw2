from __future__ import print_function
from . import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from models import get_db

import sys

@app.route('/')
@app.route('/index')
def index():
	posts = [
		{
			'user': 'Anon',
			'time': '21:00',
			'date': '26th Semptember',
			'message': 'Test message',
			'verify': 'Verify',
			'unverify': 'Unverify'
		}
	]
	return render_template('index.html', posts=posts)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

class PostForm(FlaskForm):
    user = StringField('User')
    message = StringField('Message', validators=[DataRequired(), Length(min=10, max=100)])
    submit = SubmitField('Submit')

@app.route('/post', methods=['GET', 'POST'])
def post():
	form = PostForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			db = get_db()
			user = User(form.user.data) if user is not None else "Anon"
			print(user, file=sys.stdout)
			message = Message(form.message.data)
			db.cursor().execute("INSERT INTO post (user,message) VALUES (?,?)",(user,message))
			db.commit()
			flash('Thanks for posting!')
			return redirect('/index')
	return render_template('post.html', form=form)