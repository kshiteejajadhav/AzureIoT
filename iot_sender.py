import warnings
import time
import random
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message

# Get connection string and device ID from environment variables
CONNECTION_STRING = "YOUR_CONNECTION_STRING" # Add your connection string here
DEVICE_ID = 'YOUR DEVICE_ID' # Add your device ID here

if not CONNECTION_STRING or not DEVICE_ID:
    raise ValueError("Please set IOT_HUB_CONNECTION_STRING and DEVICE_ID in your .env file")

# Create the device client and connect
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
client.connect()

print("Sending telemetry data...")
while True:
    # Simulate sensor data
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(30.0, 50.0)
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    telemetry = {
        "deviceId": DEVICE_ID,
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2),
        "timestamp": current_time
    }
    # Create and send a message
    message = Message(str(telemetry))
    client.send_message(message)
    print("Message sent:", telemetry)
    time.sleep(5)  # Send a message every 5 seconds
