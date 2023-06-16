#include <DHT.h>

#define DHTPIN 2          // Définition du pin de données connecté au capteur DHT22
#define DHTTYPE DHT22     // Définition du type de capteur
DHT dht(DHTPIN, DHTTYPE);  // Initialisation du capteur DHT22

String old_wd;  // Déclaration de la variable old_wd

const int anemometerPin = A2;  // Broche analogique pour lire la valeur de l'anémomètre
const float radius = 0.000711;  // Rayon de l'anémomètre en mètres
const unsigned long measurementDuration = 5000;  // Durée de la mesure en millisecondes

unsigned long startTime;  // Temps de début de la mesure
unsigned long elapsedTime;  // Temps écoulé depuis le début de la mesure
unsigned int pulseCount = 0;  // Compteur de pulsations

float windSpeed = 0;  // Vitesse du vent en m/s

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
 

  // CALCULE DE WIND DIRECTION
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
  // AFFICHAGE WIND DIRECTION
  
 // CALCUL DE windSpeedKmh
  startTime = millis();  // Début de la mesure
  elapsedTime = 0;  // Temps écoulé initialisé à 0
  pulseCount = 0;  // Compteur de pulsations initialisé à 0

  // Mesure pendant la durée spécifiée
    while (elapsedTime < measurementDuration) {
    // Si une pulsation est détectée, incrémenter le compteur
    if (digitalRead(anemometerPin) == HIGH) {
      pulseCount++;
    }
    
    // Mettre à jour le temps écoulé
    elapsedTime = millis() - startTime;
  }

  // Calcul de la vitesse du vent en m/s
  windSpeed = (3.14 * radius * pulseCount) / (measurementDuration / 1000.0);

  // Conversion en km/h
  float windSpeedKmh = windSpeed * 3.6;

  Serial.print(temperature);
  Serial.print(" ");
  Serial.print(humidity);
  Serial.print(" ");
  Serial.print(windSpeedKmh);
  Serial.print(" ");
  Serial.println(wd);

}