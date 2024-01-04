
# Soil Moisture Monitoring System

## Overview
This project involves the creation of a soil moisture monitoring system using an Arduino sketch and a Python script. The Arduino sketch collects soil moisture data from a capacitive soil moisture sensor and displays it on an LCD screen. The Python script reads this data over serial communication and stores it in a local MySQL database table. Sensitive information is stored in a .env file.

IMAGE
![Arduino sensor and LCD upp and running]("C:\Users\linda\Desktop\Examensarbete\Projekt\soilSensor\soilSensor\sensorSetup.jpg")

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
- Connect the Capacitive Soil Moisture Sensor and LCD display to the designated pins as specified in the sketch:

```cpp
// Setup pin connection to LCD 16x2 display
const int rs = 12;
const int vo = 6;
const int e = 11;
const int d4 = 5;
const int d5 = 4;
const int d6 = 3;
const int d7 = 2;
```

IMAGE


### 1. Python Script:

- Install required Python packages: `serial`, `python-dotenv`, `mysql-connector-python`, `requests`.
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
- Run the script.py script using Python.
