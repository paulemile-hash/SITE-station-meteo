#include <DHT.h>

#define DHTPIN 2          // Définition du pin de données connecté au capteur DHT22
#define DHTTYPE DHT22     // Définition du type de capteur
DHT dht(DHTPIN, DHTTYPE);  // Initialisation du capteur DHT22

String old_wd;  // Déclaration de la variable old_wd

void setup() {
  Serial.begin(9600);     // Configuration de la vitesse de communication série
  dht.begin();            // Initialisation du capteur DHT22
  analogRead(A1);
}

void loop() {
  delay(2000);            // Attente de 2 secondes pour que le capteur DHT22 se stabilise

  float temperature = dht.readTemperature();   // Lecture de la température en degrés Celsius
  float humidity = dht.readHumidity();         // Lecture de l'humidité relative en pourcentage

  // Affichage des données du capteur DHT22 sur le moniteur série
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print("°C\t");
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println("%");

  delay(500);
  
  int sensorValue = analogRead(A1);
  float dirvent = sensorValue / 3.3 ;
  String wd = "other";
  
  if (dirvent > 8 && dirvent < 14) {
    wd = "W";
  }
  if (dirvent > 17 && dirvent < 23) {
    wd = "NW";
  }
  if (dirvent > 28 && dirvent < 35) {
    wd = "N";
  }
  if (dirvent > 56 && dirvent < 62) {
    wd = "SW";
  }
  if (dirvent > 91 && dirvent < 99) {
    wd = "NE";
  }
  if (dirvent > 124 && dirvent < 154) {
    wd = "S";
  }
  if (dirvent > 188 && dirvent < 201) {
    wd = "SE";
  }
  if (dirvent > 224 && dirvent < 240) {
    wd = "E";
  }    

  if (wd == "other") {
    wd = old_wd;
  } else {
    old_wd = wd;
  }
  
  Serial.print("Wind Direction: ");
  Serial.println(wd);
}