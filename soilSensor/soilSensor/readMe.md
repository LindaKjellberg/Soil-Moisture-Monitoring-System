
# Soil Moisture Monitoring System

## Overview
This project involves the creation of a soil moisture monitoring system using an Arduino sketch and a Python script. The Arduino sketch collects soil moisture data from a capacitive soil moisture sensor and displays it on an LCD screen. The Python script reads this data over serial communication and stores it in a local MySQL database table. Sensitive information is stored in a .env file.


<img scr="C:/Users/linda/Desktop/Examensarbete/Projekt/soilSensor/soilSensor/Images/sensorSetup.jpg" width="100">

![](C:/Users/linda/Desktop/Examensarbete/Projekt/soilSensor/soilSensor/Images/sensorSetup.jpg)

### Hardware Components

- Arduino Uno R3 board
- Capacitive Soil Moisture Sensor v1.2
- LCD display 16x2
- USB 2.0 Cable Type A/B
- Breadboard
- Jumper wires


## Usage

### 1. Arduino Sketch:

- Upload the `soilSensor.ino` file to your Arduino Uno R3 board using the Arduino IDE.
- Configure the setup of the `board type`, `COM port` and `baudrate` to match your environment.
- Connect the Capacitive Soil Moisture Sensor  and LCD display to the designated pins as specified in the sketch:

```cpp
// Setup pin connection to LCD 16x2 display
const int rs = 12;
const int vo = 6;
const int e = 11;
const int d4 = 5;
const int d5 = 4;
const int d6 = 3;
const int d7 = 2;

// Configure pin connection to the Capacitive Soil Sensor
int sensorValue = analogRead(A0);
```

IMAGE


### 2. Python Script:

- Install required Python packages: `serial`, `python-dotenv`, `mysql-connector-python`, `requests`.
- Configure the `COM port` and `baudrate` in the `.env` file to the same as the Arduino uses.
- Configure the `HUMIDITY_THRESHOLD` to desiresd value.
- Create a `.env` file with the following variables and their values:

```makefile
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_DATABASE=your_database_name
DISCORD_WEBHOOK_URL=your_discord_webhook_url
SERIAL_PORT=your_serial_port
BAUD_RATE=your_baud_rate
```


### 3. Configure Database:

- Set up a local MySQL database with the specified `user`, `password`, `host`, and `database name`.
- Update the `.env` file with your database configuration.

### 4. Configure Discord Webhook:

- Create a Discord webhook in your Discord server.
- Copy the webhook URL and update the `DISCORD_WEBHOOK_URL` in the `.env` file.

### 5. Run the Project:
- Upload and run the `soilSensor.ino` sketch to the Arduino board
- Run the Python script by executing the following command in the terminal:
```python script.py```

- The script will start reading data from the Arduino and storing it in the MySQL database.
- If the soil humidity falls below the specified threshold, a notification will be sent to the configured Discord channel.

## Notes

- Make sure to handle sensitive information securely and avoid sharing it publicly.
- Adjust the hardware connections based on your specific setup.
- Customize the database and Discord webhook configurations according to your environment.


## Troubleshooting Tips:

- Ensure that the Arduino is properly connected, and the `COM port` is selected correctly in both the Arduino IDE and the `.env` file.
- Check for any error messages in the Arduino IDE's serial monitor and the Python script's terminal.
- Note that while running the serial monitor can not be used in the Arduino IDE, as it is being used for communicating between the Arduino sketch and Python script. You can monitor the output in the Python script's terminal.
- Verify that the hardware connections match the pin configurations in the Arduino sketch.
- Make sure the MySQL database is running and accessible with the provided credentials.

Feel free to contribute, report issues, or suggest improvements!