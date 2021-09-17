from flask import Flask, render_template, url_for, request
import popcorn_api

app = Flask (__name__)

@app.route('/')
def test():
    return popcorn_api.omdb_api_call("scream")

@app.route('/login')
def login():
    if request == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Failed Login'
        else:
            return redirect(url_for('login'))
    return render_template('content.html', error=error)
#Should just need to do "flask run" in cmd to get this to run on local host "127.0.0.1:5000"
