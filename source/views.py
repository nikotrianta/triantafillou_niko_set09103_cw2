from . import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired 

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

@app.route('/post')
def post():
	form = PostForm()
	return render_template('post.html', form=form)