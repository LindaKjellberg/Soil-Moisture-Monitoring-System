import serial  # Import for the serial module
import time  # Import for the time module
from dotenv import load_dotenv  # Import function to use .env variables
import os   # Import the os module
import mysql.connector  # Import MySQL connector module
import re  # Import the regular expression module
from datetime import datetime, timedelta    #Import datetime module
import requests # Import HTTP request library


# Load environment variables from .env file
load_dotenv()

# MySQL credentials configuration
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', '')
DB_DATABASE = os.getenv('DB_DATABASE', '')

# Discord webhook URL configuration
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')

# Serial port configuration
SERIAL_PORT = os.getenv('SERIAL_PORT', '')
BAUD_RATE = int(os.getenv('BAUD_RATE', '9600'))

# Humidity threshold for Discord notification
HUMIDITY_THRESHOLD = 22

# Time interval for Discord notifications (in seconds)
# NOTIFICATION_INTERVAL = 24 * 60 * 60  # Every 24 hours

# Time tracking for notifications
last_notification_time = datetime.now()

# Open serial port for communication 
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Connect to local MySQL database using credentials stored in .env file
try:
    print("Connecting to the database...")  # Print message to terminal when trying to establish connection
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    print("Connected to the database.") # Print message to terminal if connection is established

    # Create a cursor object to handle interaction with the MySQL database 
    cursor = connection.cursor()


    while True:
        # Read data from Arduino sketch
        line = ser.readline().decode('utf-8').strip()   # Using serial communication to read the data, UTF-8 encoding to convert the result, then removes any unwanted whitespace

        # Extract numeric value from the printed content
        humidity_match = re.search(r"Soil Humidity: (\d+)%", line)  # Searches for the specific expression with value in the Arduino sketch
        if humidity_match:
            humidity_value = int(humidity_match.group(1))

            # Insert humidity value into MySQL table
            insert_query = "INSERT INTO sensor_data (humidity) VALUES (%s)" # Configure the setup forr entering the data into the MySQL table
            cursor.execute(insert_query, (humidity_value,)) # Use cursor object to send the data
            connection.commit() # Enter the data into the table

            print(f"Inserted humidity value: {humidity_value}") 

            # Check if humidity is below the threshold
            if humidity_value <= HUMIDITY_THRESHOLD:    # If the humidity reaches the threshold or lower print a warning
                print(f"Alert: Soil humidity is below {HUMIDITY_THRESHOLD}% - Sending notification to Discord")
                    
                # Create an alert for webhook
                message_content = f"Alert: Soil humidity is below {HUMIDITY_THRESHOLD}%. Current humidity {humidity_value}%"

                # Send notification to Discord using webhook
                payload = {"content": message_content}  # Store the alert in a payload 
                requests.post(DISCORD_WEBHOOK_URL, json=payload)    # Use HTTP communication and the URL to send the alert to Discord channel

        # Set interval for sending the collected data from the Arduino sketch to the MySQL database
        time.sleep(60)  # Send data every 60 seconds

# Exception handling 
except KeyboardInterrupt:
    print("Script terminated by user")

# Exception handling
except Exception as e:
    print(f"Error: {e}")

finally:
    # Close serial port
    ser.close()
    # Close MySQL connection
    if connection.is_connected():
        cursor.close()
        connection.close()