// Include the Adafruit library for the LCD
#include <LiquidCrystal.h>


// Setup values for Capacitive Soil Sensor, this particular sensor has a range of 424 to 796
const int dry = 796; // Value for dry sensor, the highest possible value the sensor can measure
const int wet = 424; // Value for wet sensor, the lowest possible value the sensor can measure

// Setup pin connection to LCD 16x2 display
const int rs = 12; // LCD pin rs connected to Arduino digital pin 12
const int vo = 6; // LCD pin vo connected to Arduino digital pin 6
const int e = 11; // LCD pin e connected to Arduino digital pin 11
const int d4 = 5; // LCD pin d4 connected to Arduino digital pin 5
const int d5 = 4; // LCD pin d5 connected to Arduino digital pin 4
const int d6 = 3; // LCD pin d6 connected to Arduino digital pin 3
const int d7 = 2; // LCD pin d7 connected to Arduino digital pin 2

// Instantiate LiquidCrystal class (from library) with name lcd
LiquidCrystal lcd(rs, vo, e, d4, d5, d6, d7); // Instantiate LCD using the pins as arguments to setup the communication between the LCD display and the Arduino Uno board

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
