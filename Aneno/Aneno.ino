const int anemometerPin = A2;  // Broche analogique pour lire la tension de l'anémomètre

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(anemometerPin);
  float voltage = sensorValue * (5.0 / 1023.0);  // Conversion de la valeur lue en tension (5V est la référence)

  Serial.print("Tension : ");
  Serial.print(voltage, 2);  // Affichage de la tension avec 2 décimales
  Serial.println(" V");
  delay(1000);
}