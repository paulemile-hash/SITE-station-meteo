#include <DHT.h>
#define DHTPIN 2          // Définition du pin de données du DHT22
#define DHTTYPE DHT22     // Définition du type de capteur
DHT dht(DHTPIN, DHTTYPE);  // Initialisation du capteur DHT22

String old_wd;  // Déclaration de la variable old_wd

const int anemometerPin = A2;  // Broche analogique de l'anémomètre
const float radius = 0.0711;  // Rayon de l'anémomètre en mètres
const unsigned long measurementDuration = 1000;  // Durée de la mesure en millisecondes

unsigned long startTime;  // Temps de début de la mesure
unsigned long elapsedTime;  // Temps depuis le début de la mesure
unsigned int pulseCount = 0;  // Compteur de pulsations

float windSpeed = 0;  // Vitesse du vent en m/s

  void setup() {
  Serial.begin(9600);     // Vitesse de communication de l'Arduino
  dht.begin();            // Initialisation du capteur DHT22
  analogRead(A1);         // Port analogique 
}

  void loop() {
  //delay(2000);            // Stabilisation du capteurs en 2s

  float temperature = dht.readTemperature();   // Lecture de la température en degrés Celsius
  float humidity = dht.readHumidity();         // Lecture de l'humidité relative en pourcentage
 
  // CALCULE DE WIND DIRECTION
  //delay(500);
  
  int sensorValue = analogRead(A1);
  float dirvent = sensorValue ;
  String wd = "other";
  
  if (dirvent > 90 && dirvent < 460) {
    wd = "E";
  }
  if (dirvent > 790 && dirvent < 890) {
    wd = "N";
  }
  if (dirvent > 400 && dirvent < 459) {
    wd = "N";
  }
  if (dirvent > 635 && dirvent < 790) {
    wd = "W";
  }   
  if (dirvent > 180 && dirvent < 635) {
    wd = "S";
  }

  if (wd == "other") {
    wd = old_wd;
  } else {
    old_wd = wd;
  }
  
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
  windSpeed = (3.14 * radius * pulseCount) / (measurementDuration);

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