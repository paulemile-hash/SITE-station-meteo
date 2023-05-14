import serial
import sqlite3
import time

# Paramètres de communication série
port = 'COM7'  # Remplacez par le port série de votre Arduino (ex: 'COM3' sous Windows)
baud_rate = 9600
name_db = "data/tast1.db"


# Établir la connexion série
ser = serial.Serial(port, baud_rate, timeout=1)  # Ajout du paramètre timeout pour éviter les blocages

# Attendre une seconde pour laisser le temps à la connexion de s'établir
ser.reset_input_buffer()
time.sleep(1)


db = sqlite3.connect(name_db)
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mesures(time INTEGER,temperature FLOAT, humidite FLOAT, force_vent FLOAT, direction_vent FLOAT)")



while True:
    if ser.in_waiting > 0:
        # Lire toutes les données disponibles dans le buffer de réception
        #data = ser.readline().decode('utf-8').rstrip()
        data = input("donne la ligne : ")


        x=data.split()# créer une liste dés qu'il y a un espace
        x.insert(0,time.time())            # ({x[0]},{x[1]},0,0) chaque élément = 1 colomnes et avec direction et force ({x[0]},{x[1]},{x[2]},{x[3]})
        cur.execute(f"""INSERT INTO mesures VALUES
                ({x[0]},{x[1]},{x[2]},0,0)  
        """) #transferer mes valeurs de data.txt dans la base de données
        # Faire quelque chose avec les données lues
        print(data)  # Afficher les données à la console
        db.commit()

# Fermer la connexion série lorsque vous avez terminé

db.close()
ser.close()