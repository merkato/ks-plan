from flask import Flask, render_template, json, redirect, url_for, request
from models import db

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

#db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
    
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Try again'
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=49666)
