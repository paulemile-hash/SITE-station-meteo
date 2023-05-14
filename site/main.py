from flask import Flask, render_template
import sqlite3

name_db = "data/test1.db"

db = sqlite3.connect(name_db, check_same_thread=False)
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mesures(time INTEGER,temperature FLOAT, humidite FLOAT, force_vent FLOAT, direction_vent FLOAT)") # création de la table si elle existe pas


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/humidite')
def humidity():
    data_humidite = cur.execute("SELECT time,humidite FROM mesures").fetchall()
    data = [[x[0], x[1]] for x in data_humidite]
    return render_template('humidite.html', data_humidite=data, title="Humidité")

@app.route('/temperature')
def temperature():
    data_temperature = cur.execute("SELECT time,temperature FROM mesures").fetchall()
    data = [[x[0], x[1]] for x in data_temperature]
    return render_template('temperature.html', data_temperature=data, title="Température")

@app.route('/vent')
def vent():
    data_vent = cur.execute("SELECT time,force_vent, direction_vent FROM mesures").fetchall()
    data = [[x[0], x[1], x[2]] for x in data_vent]
    return render_template('vent.html', data_vent=data, title="Vent")


app.run(debug=True)