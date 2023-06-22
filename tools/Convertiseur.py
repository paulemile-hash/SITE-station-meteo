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
                    file.write(data)
                    
                    # Afficher les données à la console
                    print(data, end='')
            except serial.SerialException as e:
                print(f"Erreur lors de la lecture du port série : {e}")
                break
except IOError as e:
    print(f"Erreur lors de l'ouverture du fichier de sortie : {e}")
    exit(1)

ser.close()