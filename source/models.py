from flask import Flask, g
import sqlite3

from flask import Flask
app = Flask(__name__)
db_location = 'var/sqlite3.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/post', methods=['GET', 'POST'])
def post():
	form = PostForm()
	if form.validate_on_submit():
        user = 'AnonUser'
		# User(form.user.data) if user is not None else "Anon"
		message = 'Test message'
		# Message(form.message.data)
        db = get_db()
        db.cursor().execute('insert into post values ("'user'", "'message'")')
        db.commit()
		flash('Thanks for posting!')
		return redirect('/index')
	return render_template('post.html', form=form)