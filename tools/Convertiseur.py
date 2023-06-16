import serial
import sqlite3
import time

# Paramètres de communication série
# Remplacez par le port série de votre Arduino (ex: 'COM3' sous Windows)
port = 'COM7'
baud_rate = 9600
name_db = "data/test1.db"


# Établir la connexion série
# Ajout du paramètre timeout pour éviter les blocages
ser = serial.Serial(port, baud_rate, timeout=1)

# Attendre une seconde pour laisser le temps à la connexion de s'établir
ser.reset_input_buffer()
time.sleep(1)


db = sqlite3.connect(name_db)
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mesures(time FLOAT,temperature FLOAT, humidite FLOAT, force_vent FLOAT, direction_vent)") # création de la table si elle existe pas


while True:
    if ser.in_waiting > 0:
        # Lire toutes les données disponibles dans le buffer de réception
        data = ser.readline().decode('utf-8').rstrip()

        x = data.split()  # créer une liste dés qu'il y a un espace
        # ({x[0]},{x[1]},0,0) chaque élément = 1 colomnes et avec direction et force ({x[0]},{x[1]},{x[2]},{x[3]})
        x.insert(0, time.time())
        cur.execute(f"""INSERT INTO mesures VALUES
                ({x[0]},{x[1]},{x[2]},0,0)  
        """)  # transferer mes valeurs dans la base de données
       
        print(data)  # Afficher les données à la console
        db.commit()

# Fermer la connexion série lorsque vous avez terminé

db.close()
ser.close()
