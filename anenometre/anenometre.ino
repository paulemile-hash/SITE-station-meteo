const int anemometerPin = 2;  // Broche de l'anémomètre
volatile unsigned int pulseCount = 0;  // Compteur d'impulsions
unsigned long lastTime = 0;  // Dernier moment de lecture des impulsions
float windSpeed = 0.0;  // Vitesse du vent en m/s

void setup() {
  pinMode(anemometerPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(anemometerPin), countPulse, FALLING);
  Serial.begin(9600);
}

void loop() {
  unsigned long currentTime = millis();

  if (currentTime - lastTime >= 1000) {
    detachInterrupt(digitalPinToInterrupt(anemometerPin));
    windSpeed = calculateWindSpeed();
    pulseCount = 0;
    attachInterrupt(digitalPinToInterrupt(anemometerPin), countPulse, FALLING);
    lastTime = currentTime;
  }

  // Autres actions à réaliser pendant la boucle
  // ...

  Serial.print("Vitesse du vent : ");
  Serial.print(windSpeed);
  Serial.println(" m/s");
  delay(1000);
}

void countPulse() {
  pulseCount++;
}

float calculateWindSpeed() {
  const float calibrationFactor = 2.4;  // Facteur de calibration pour la conversion en m/s
  float windSpeed = pulseCount * calibrationFactor;
  return windSpeed;
}