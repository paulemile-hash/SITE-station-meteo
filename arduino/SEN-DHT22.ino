#include <DHT.h>
#define DHTPIN 2          // Définition du pin de données connecté au capteur DHT22
#define DHTTYPE DHT22     // Définition du type de capteur
DHT dht(DHTPIN, DHTTYPE);  // Initialisation du capteur DHT22

void setup() {
  Serial.begin(9600);     // Configuration de la vitesse de communication série
  dht.begin();            // Initialisation du capteur DHT22
}
void loop() {
  delay(2000);            // Attente de 2 secondes pour que le capteur DHT22 se stabilise

  float temperature = dht.readTemperature();   // Lecture de la température en degrés Celsius
  float humidity = dht.readHumidity();         // Lecture de l'humidité relative en pourcentage

  // Affichage des données sur le moniteur série
  Serial.print(temperature);
  Serial.print(" ");
  Serial.println(humidity);
}
