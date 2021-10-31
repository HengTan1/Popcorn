from enum import unique
from flask import Flask, render_template, url_for, request
from flask import session
from flask import redirect
from werkzeug.utils import html
import popcorn_api
#from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_manager
from sqlalchemy import create_engine
from flask import g
import sqlite3

app = Flask (__name__)
app.secret_key = 'secretkey'

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

#Test users for now. Will need to add DB code here. Check before insert.
users = []
users.append(User(id=1, username='Test1', password='password1'))
users.append(User(id=2, username='Test2', password='password2'))
users.append(User(id=3, username='Test3', password='password3'))
users.append(User(id=4, username='Test4', password='password4'))

@app.route('/')
def home():
    return render_template('index.html')

#Flask function that runs before each request.
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        #Need to add a DB search here for user ID.
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#Checking if username is in list. Need to check for unique when user is created.
@app.route('/login', methods=['GET', 'POST'])
def login():
    from Database.Users import users
    r = ""
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("Database/users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
        r = c.fetchall()
        for i in r:
            if (username == i[0] and password == i[1]):
                session["loggedin"] = True
                session["username"] = username
                return redirect(url_for("test"))
            else:
                errorMsg = "Username or password is incorrect."
            
    return render_template('login.html')

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    from Database.Users import users
    session.pop('user_id', None)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #Would add user to DB here. create_user is a test user.
        
        # Using Users method
        user = users.insert(username, password)
        
        # DB code
        # conn = sqlite3.connect("users.db")
        # c = conn.cursor()
        # c.execute("SELECT * FROM users WHERE username = '" + username + "'")
        # if(c.fetchone()):
        #     print("User already exists")
        #     conn.close()
        # else:
        #     c.execute("INSERT INTO users VALUES ('" + username + "', '" + password + "')")
        #     print("Username " + username + " added")
        #     conn.commit()
        #     conn.close()
        
        # create_user = User(id=4, username=username, password=password)
        # session['user.id'] = create_user.id
        return (redirect(url_for('login')))
    return render_template('signup.html')

@app.route('/topten', methods=['GET', 'POST'])
def topten():
    if request.method == 'GET':
        return popcorn_api.top_movies_imdb()


app.run()

#Should just need to do "flask run" in cmd to get this to run on local host "127.0.0.1:5000"
