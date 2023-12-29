
// Setup values for Capacitive Soil Sensor, this particular sensor has a range of 424 to 796
const int dry = 796; // Value for dry sensor, the highest possible value the sensor can measure
const int wet = 424; // Value for wet sensor, the lowest possible value the sensor can measure

// Setup prepares and starts the program
void setup() {
 Serial.begin(9600); // Initialize the Sketch with 9600 baud rate
}

// Loop through the functions and actions the program should perform
void loop() {
 int sensorValue = analogRead(A0); // Get the measured sensor value as an integer from the analog pin A0

 
 // Translate the range of values to a scale of 0% to 100%
 int percentageHumidity = map(sensorValue, wet, dry, 100, 0); // Using the map function to translate sensor value to humidity in percent

 Serial.print(percentageHumidity); // Print the humidity value in percent to the terminal without a line break
  Serial.println("%"); // Add percentage symbol at the end of each value and then a line break

 delay(1000); // One second delay in between each value reading for a clear representation
}
