void setup() {
pinMode(13, OUTPUT);
pinMode(A2, INPUT);
}
// Boucle principale:
void loop() {
int BP = digitalRead(A2); // Lecture du capteur
if (BP == LOW) {
digitalWrite(13, HIGH); // Allume la Led
}
else {
digitalWrite(13, LOW); // Eteind la Led
}
} 