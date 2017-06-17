from flask import Flask, render_template, json, redirect, url_for, request
from peewee import *
from models import *

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/wolne", methods=["GET","POST"])
def holiday():
	if request.method == 'POST':
		termin = request.form.get('inputTermin')
		opis = request.form.get('inputOpis')
		wariant = request.form.get('inputWariant')
		q = holidays.insert(termin = termin, opis = opis, wariant = wariant)
		q.execute()
		return redirect(url_for('holiday'))
	return render_template("holiday.html",wolne=list(holidays.select().order_by(holidays.termin.asc())))

@app.route("/pociagi", methods=["GET","POST"])
def trains():
	if request.method == 'POST':
		termin = request.form.get('inputTermin')
		opis = request.form.get('inputOpis')
		wariant = request.form.get('inputWariant')
		q = holidays.insert(termin = termin, opis = opis, wariant = wariant)
		q.execute()
		return redirect(url_for('pociagi'))
	return render_template("pociagi.html",wolne=list(holidays.select()))

@app.route("/sluzby", methods=["GET","POST"])
def shifts():
	if request.method == 'POST':
		termin = request.form.get('inputTermin')
		opis = request.form.get('inputOpis')
		wariant = request.form.get('inputWariant')
		q = holidays.insert(termin = termin, opis = opis, wariant = wariant)
		q.execute()
		return redirect(url_for('holiday'))
	return render_template("holiday.html",wolne=list(holidays.select()))

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

def login_required(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        if session.get('logged_in'):
            return fn(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return inner

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=49666)
