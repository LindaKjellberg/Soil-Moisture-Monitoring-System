#include <LiquidCrystal.h>  // Include the Adafruit library for the LCD


// Setup values for Capacitive Soil Sensor, sensor has a range of 424 to 796
const int dry = 796;  // Value for dry sensor, the highest possible value the sensor can measure
const int wet = 424;  // Value for wet sensor, the lowest possible value the sensor can measure

// Setup pin connection to LCD 16x2 display
const int rs = 12;  // LCD pin rs connected to Arduino digital pin 12
const int vo = 6;   // LCD pin vo connected to Arduino digital pin 6
const int e = 11;   // LCD pin e connected to Arduino digital pin 11
const int d4 = 5;   // LCD pin d4 connected to Arduino digital pin 5
const int d5 = 4;   // LCD pin d5 connected to Arduino digital pin 4
const int d6 = 3;   // LCD pin d6 connected to Arduino digital pin 3
const int d7 = 2;   // LCD pin d7 connected to Arduino digital pin 2

// Configure LCD display connection to Arduino board
LiquidCrystal lcd(rs, vo, e, d4, d5, d6, d7);  // Instantiate LCD with the pins as arguments to setup the communication

// Setup that prepares and starts the program
void setup() {
  Serial.begin(9600);  // Initialize the Sketch with 9600 baud rate
  lcd.begin(16, 2);    // Setup the dimensions of number rows and columns on the LCD

  delay(2000);  // Two seconds delay to ensure the LCD is setup properly
}

// Loop through the functions and actions the program should perform
void loop() {
  // Configure pin connection to the Capacitive Soil Sensor
  int sensorValue = analogRead(A0);  // Get the measured sensor value as an integer from the analog pin A0

  // Translate the range of values to a scale of 0% to 100% for a more evident value representation
  int percentageHumidity = map(sensorValue, wet, dry, 100, 0);  // Mapping the sensor value to humidity in percent

  // Print to terminal
  Serial.print("Soil Humidity: ");   // Print the text message to the LCD
  Serial.print(percentageHumidity);  // Print the humidity value in percent to the terminal
  Serial.println("%");               // Add percentage symbol at the end of each value

  // Print to LCD Screen
  lcd.setCursor(1, 0);            // Moves the cursor to column 2 on the first row
  lcd.print("Soil Humidity: ");   // Print the text message to the LCD
  lcd.setCursor(6, 1);            // Moves the cursor to column 7 on the second row
  lcd.print(percentageHumidity);  // Print the humidity to LCD
  lcd.print("%");                 // Add percentage symbol at the end of each value

  delay(1000);  // One second delay in between each value reading for a clear representation
}