from flask import Flask, render_template, request, redirect, \
    url_for, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import os

# create the application object
app = Flask(__name__)

# Config the application object
# app.config.from_object('config.DevelopmentConfig')
# For the environments to be detected on the fly,
# Change the way configs are imported
app.config.from_object(os.environ['APP_SETTINGS'])
# print os.environ['APP_SETTINGS']

# This shouldn't be in actual environemnt find better ways.
# Use random key generator and then use sessions.
# app.secret_key = 'my precious'
# Now we are switching to the main config file
# Configuration fo the sequel lite 3
# app.database = "sample.db"
# Configuring the database to be dealt through alchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# Now we are switching to the main config file

# Create the alchemy
db = SQLAlchemy(app)

# Import model after the database is created, hence not topmost post
from models import *


# Use login required decorator
# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


# use Decorator for routing
@app.route('/')
# Adding login required decorator
@login_required
def home():
    # Remove the string and get the index page now.
    # return "Hello, world!"
    # g is specific to flask which store temporory object.
    # g.db = connect_db()
    #     cur = g.db.execute('select * from  posts')
    # posts = [dict(title=row[0], description=row[1]) \
    # for row in cur.fetchall()]
    # g.db.close()
    # Switching to the alchemy
    posts = []
    try:
        posts = db.session.query(BlogPost).all()
    except:
        flash("You have no datatbase")
    return render_template("index.html", posts=posts)


@app.route('/welcome')
@login_required
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid credentials, Please try again.'
        else:
            session['logged_in'] = True
            flash('You have just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have just logged out!')
    return redirect(url_for('welcome'))

# Commenting out the sqlite code will be migrating to the alchemy
# def connect_db():
#     """
#     Getting the sqlite3 DB connection
#     """
#     return sqlite3.connect(app.database)


if __name__ == '__main__':
    # app.run(debug=True)
    # Now we are switching to the main config file
    app.run()
