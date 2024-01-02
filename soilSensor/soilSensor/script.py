import serial
import time
from dotenv import load_dotenv
import os
import mysql.connector
import re  # Import the regular expression module

# Load environment variables from .env file
load_dotenv()

# MySQL credentials
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', '')
DB_DATABASE = os.getenv('DB_DATABASE', '')

# Serial port configuration
SERIAL_PORT = os.getenv('SERIAL_PORT', '')
BAUD_RATE = int(os.getenv('BAUD_RATE', '9600'))

# Open serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Connect to MySQL
try:
    print("Connecting to the database...")
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    print("Connected to the database.")

    cursor = connection.cursor()

    while True:
        # Read data from Arduino Uno
        line = ser.readline().decode('utf-8').strip()
        
        # Extract numeric value from the printed content
        humidity_match = re.search(r"Soil Humidity: (\d+)%", line)
        if humidity_match:
            humidity_value = int(humidity_match.group(1))

            # Insert humidity value into MySQL table
            insert_query = "INSERT INTO sensor_data (humidity) VALUES (%s)"
            cursor.execute(insert_query, (humidity_value,))
            connection.commit()

            print(f"Inserted humidity value: {humidity_value}")

        time.sleep(60)  # Send data every 60 second

except KeyboardInterrupt:
    print("Script terminated by user")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close serial port
    ser.close()
    # Close MySQL connection
    if connection.is_connected():
        cursor.close()
        connection.close()

