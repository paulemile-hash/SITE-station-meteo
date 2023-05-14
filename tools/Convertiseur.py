import serial

# Paramètres de communication série
port = 'COM7'  # Remplacez par le port série de votre Arduino (ex: 'COM3' sous Windows)
baud_rate = 9600

# Établir la connexion série
ser = serial.Serial(port, baud_rate, timeout=1)  # Ajout du paramètre timeout pour éviter les blocages

# Attendre une seconde pour laisser le temps à la connexion de s'établir
ser.reset_input_buffer()
time.sleep(1)

while True:
    if ser.in_waiting > 0:
        # Lire toutes les données disponibles dans le buffer de réception
        data = ser.readline().decode('utf-8').rstrip()

        # Faire quelque chose avec les données lues
        print(data)  # Afficher les données à la console

# Fermer la connexion série lorsque vous avez terminé
ser.close()