from flask import Flask, render_template
import sqlite3

# Connexion à la base de données
name_db = "data/test1.db"

db = sqlite3.connect(name_db, check_same_thread=False)
cur = db.cursor()
#si la mesures exiqye pas on crée une table 
cur.execute("CREATE TABLE IF NOT EXISTS mesures(time INTEGER,temperature FLOAT, humidite FLOAT, force_vent FLOAT, direction_vent FLOAT)") # création de la table si elle existe pas

# Création de l'application Flask
app = Flask(__name__)

# Définition des routes
#lier bases de données au sites 
#AVG = moyenne
@app.route('/')
def index():
    moyenne_humidite = cur.execute("SELECT AVG(humidite) FROM mesures").fetchone()[0]
    moyenne_temperature = cur.execute("SELECT AVG(temperature) FROM mesures").fetchone()[0]
    moyenne_force_vent = cur.execute("SELECT AVG(force_vent) FROM mesures").fetchone()[0]
    return render_template('main.html',moyenne_humidite=round(moyenne_humidite,1),moyenne_temperature=round(moyenne_temperature,1),moyenne_force_vent=round(moyenne_force_vent,1))

# Route /humidite
@app.route('/humidite')
def humidity():
    # Récupération des données d'humidité de la base de données
    data_humidite = cur.execute("SELECT time,humidite FROM mesures").fetchall()
    data = [[x[0], x[1]] for x in data_humidite]
    # Calcul de la moyenne d'humidité
    moyenne_humidite = cur.execute("SELECT AVG(humidite) FROM mesures").fetchone()[0]
    # Renvoie du template humidite.html avec les données
    return render_template('humidite.html', data=data, moyenne_humidite=moyenne_humidite, title="Humidité")

@app.route('/temperature')
def temperature():
    # Récupération des données de température de la base de données
    data_temperature = cur.execute("SELECT time,temperature FROM mesures").fetchall()
    data = [[x[0], x[1]] for x in data_temperature]
    # Calcul de la moyenne de température
    moyenne_temperature = cur.execute("SELECT AVG(temperature) FROM mesures").fetchone()[0]
    # Renvoie du template temperature.html avec les données
    return render_template('temperature.html', data=data, moyenne_temperature=moyenne_temperature, title="Température")

@app.route('/vent')
def vent():
    # Récupération des données de vent de la base de données
    data_vent = cur.execute("SELECT time,force_vent, direction_vent FROM mesures").fetchall()
    data = [[x[0], x[1], x[2]] for x in data_vent]
    # Calcul de la moyenne de force et direction du vent
    moyenne_force_vent = cur.execute("SELECT AVG(force_vent) FROM mesures").fetchone()[0]
    # Renvoie du template vent.html avec les données
    return render_template('vent.html', data=data, moyenne_force_vent=moyenne_force_vent,title="Vent")


app.run(debug=True)