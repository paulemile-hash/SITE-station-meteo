import serial
import sqlite3
import time
import serial

port = 'COM7'
baud_rate = 9600
output_file = 'data/data.txt'

try:
    ser = serial.Serial(port, baud_rate)
except serial.SerialException as e:
    print(f"Erreur lors de l'ouverture du port série : {e}")
    exit(1)

try:
    with open(output_file, 'w') as file:
        while True:
            try:
                if ser.in_waiting > 0:
                    # Lire les données disponibles dans le buffer de réception
                    data = ser.read(ser.in_waiting).decode('utf-8')
                    
                    # Écrire les données dans le fichier de sortie
                    file.write(data.strip())
                    
                    # Afficher les données à la console
                    print(data, end='')
            except serial.SerialException as e:
                print(f"Erreur lors de la lecture du port série : {e}")
                break
except IOError as e:
    print(f"Erreur lors de l'ouverture du fichier de sortie : {e}")
    exit(1)

ser.close()



name_db = "data/test1.db"
db = sqlite3.connect(name_db)
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mesures(time FLOAT,temperature FLOAT, humidite FLOAT, force_vent FLOAT, direction_vent FLOAT)") # création de la table si elle existe pas



def lecture (txt):
    fichier=open(txt,"r")
    for row in fichier:
        x=row.split()# créer une liste dés qu'il y a un espace
        x.insert(0, time.time())
        cur.execute(f"""INSERT INTO mesures VALUES
        ({x[0]},{x[1]},{x[2]},{x[3]},{x[4]})  
        """)
         #transferer mes valeurs de data.txt dans la base de données
    fichier.close()



lecture("data.txt")
db.commit()
db.close()

