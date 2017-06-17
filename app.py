# utf-8
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

# Zakladka pociagi, edycja danych i wyswietlanie informacji o odcinkach obslugiwanych
@app.route("/pociagi", methods=["GET","POST"])
def trains():
    if request.method == 'POST':
        plan = request.form.get('inputPlan')
        obieg = request.form.get('inputObieg')
        nr_poc = request.form.get('inputPociag')
        termin = request.form.get('inputTermin')
        wyklucz = request.form.get('inputWyklucz')
        dolacz = request.form.get('inputDolacz')
        wariant = request.form.get('inputWariant')
        st_pocz = request.form.get('inputSPocz')
        st_konc = request.form.get('inputSKonc')
        godz_pocz = request.form.get('inputGPocz')
        godz_konc = request.form.get('inputGKonc')
        tabor = request.form.get('inputTabor')
        q = pociagi.insert(plan = obieg, obieg = obieg, nr_poc = nr_poc, termin = termin, wyklucz = wariant, dolacz = dolacz, wariant = wariant, st_pocz = st_pocz, st_konc = st_konc, godz_pocz = godz_pocz, godz_konc = godz_konc, tabor = tabor)
        q.execute()
        return redirect(url_for('pociagi'))
    return render_template("pociagi.html",wolne=list(pociagi.select().order_by(pociagi.nr_poc.asc()))

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
