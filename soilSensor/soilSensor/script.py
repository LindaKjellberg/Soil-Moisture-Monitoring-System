import serial  # Add this import for the serial module
import time  # Add this import for the time module
from dotenv import load_dotenv
import os
import mysql.connector
import re  # Import the regular expression module
from datetime import datetime, timedelta
import requests


# Load environment variables from .env file
load_dotenv()

# MySQL credentials
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', '')
DB_DATABASE = os.getenv('DB_DATABASE', '')

# Discord webhook URL
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')

# Serial port configuration
SERIAL_PORT = os.getenv('SERIAL_PORT', '')
BAUD_RATE = int(os.getenv('BAUD_RATE', '9600'))

# Humidity threshold for notification
HUMIDITY_THRESHOLD = 25

# Time interval for Discord notifications (in seconds)
# NOTIFICATION_INTERVAL = 24 * 60 * 60  # 24 hours

# Time tracking for notifications
last_notification_time = datetime.now()

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

            # Check if humidity is below the threshold
            if humidity_value <= HUMIDITY_THRESHOLD:
                print(f"Alert: Soil humidity is below {HUMIDITY_THRESHOLD}% - Sending notification to Discord")
                    
                # Create message content
                message_content = f"Alert: Soil humidity is below {HUMIDITY_THRESHOLD}%. Current humidity {humidity_value}%"

                # Send notification to Discord using webhook
                payload = {"content": message_content}
                requests.post(DISCORD_WEBHOOK_URL, json=payload)


        time.sleep(60)  # Send data every 60 seconds

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