import sqlite3
def lecture (txt):
    fichier=open(txt,"r")
    for row in fichier:
        x=row.split()# créer une liste dés qu'il y a un espace
                    # ({x[0]},{x[1]},0,0) chaque élément = 1 colomnes et avec direction et force ({x[0]},{x[1]},{x[2]},{x[3]})
        cur.execute(f"""INSERT INTO mesures VALUES
                ({x[0]},{x[1]},0,0)  
        """) #transferer mes valeurs de data.txt dans la base de données
    fichier.close()
def create():
    cur.execute("CREATE TABLE mesures(temperature FLOAT, humidite FLOAT, force_vent FLOAT, direction_vent FLOAT)")
db = sqlite3.connect("test1.db")
cur = db.cursor()

lecture("data.txt")
db.commit()
db.close()
#coucou
