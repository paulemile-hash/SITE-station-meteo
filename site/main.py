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
    moyenne_humidite = cur.execute("SELECT AVG(humidite) FROM mesures").fetchone()[0]
    return render_template('humidite.html', data=data, moyenne_humidite=moyenne_humidite, title="Humidité")

@app.route('/temperature')
def temperature():
    data_temperature = cur.execute("SELECT time,temperature FROM mesures").fetchall()
    data = [[x[0], x[1]] for x in data_temperature]
    moyenne_temperature = cur.execute("SELECT AVG(temperature) FROM mesures").fetchone()[0]
    return render_template('temperature.html', data=data, moyenne_temperature=moyenne_temperature, title="Température")

@app.route('/vent')
def vent():
    data_vent = cur.execute("SELECT time,force_vent, direction_vent FROM mesures").fetchall()
    data = [[x[0], x[1], x[2]] for x in data_vent]
    moyenne_force_vent = cur.execute("SELECT AVG(force_vent) FROM mesures").fetchone()[0]
    moyenne_direction_vent = cur.execute("SELECT AVG(direction_vent) FROM mesures").fetchone()[0]
    return render_template('vent.html', data=data, moyenne_force_vent=moyenne_force_vent, moyenne_direction_vent=moyenne_direction_vent, title="Vent")


app.run(debug=True)