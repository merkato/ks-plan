from flask import Flask, render_template, json, redirect, url_for, request
from peewee import * 
from models import *

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

@app.route("/")
def index():
    return render_template("index.html")

def login_required(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        if session.get('logged_in'):
            return fn(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return inner

@app.route('/login/', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next') or request.form.get('next')
    if request.method == 'POST' and request.form.get('password'):
        password = request.form.get('password')
        if password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            session.permanent = True  # Use cookie to store session.
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            flash('Incorrect password.', 'danger')
    return render_template('login.html', next_url=next_url)

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('login'))
    return render_template('logout.html')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/dodaj_wolne", methods=["GET","POST"])
def addholiday():
	if request.method == 'POST':
		termin_v = request.form.get('inputTermin')
		opis_v = request.form.get('inputOpis')
		wariant_v = request.form.get('inputWariant')
		holidays.insert(termin = termin_v, opis = opis_v, wariant = wariant_v)
		return redirect(url_for('wolne'))
	return render_template("holiday.html")

@app.route("/wolne")
def holiday():
	return render_template("holiday_list.html",wolne=list(holidays.select()))

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=49666)
