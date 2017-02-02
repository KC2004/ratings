"""Movie Ratings."""

from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, jsonify, render_template, redirect, request, flash, session
from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    # a = jsonify([1,3])
    # return a
    return render_template("homepage.html")


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route('/login')
def login():
    """Login page shows login form"""

    return render_template("login_form.html")


@app.route('/login', methods=["POST"])
def login_form():
    """Handle submission of login form"""

    email = request.form.get('email')
    password = request.form.get('pwd')
    print email, password
    # login page gets email and pwd, then redirects to home page?
        # if user doesnt exist, go to /register route, and add them to the db?

    # check to see if user exists
    user_rec = User.query.filter_by(email=email).first()
    print user_rec
    # TODO: check to see if submitted password matches user_rec.pass in db

    if not user_rec:
        # call other post and add to db?
        # if pwd doessnt match, reload form with alert try again
        return render_template("register_form.html")
        # return render_template("register_form.html", email=email,password=password )
    else:
        # TODO: add username and email to flask session to set alert
        return redirect("/")


@app.route('/register')
def register_form():
    """Registration page"""

    return render_template("register_form.html")


@app.route('/register', methods=["POST"])
def register_process():
    """Registration page"""

    # if user does not exist, add to db
    Users.add_new_user(email, password)

    return redirect("/")

    # return render_template("register_form.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5000, host='0.0.0.0')
