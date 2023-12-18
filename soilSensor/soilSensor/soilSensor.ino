
const int dry = 796; // Value for dry sensor
const int wet = 424; // Value for wet sensor

void setup() {
 Serial.begin(9600);
}

void loop() {
 int sensorValue = analogRead(A0);

 // Sensor has a range of 424 to 796
 // We want to translate this to a scale or 0% to 100%

 int percentageHumidity = map(sensorValue, wet, dry, 100, 0); // Using the map function to translate sensor value to humidity in percent

 Serial.print(percentageHumidity);
  Serial.println("%");

 delay(1000); // 1s delay in between reads for stability
}
