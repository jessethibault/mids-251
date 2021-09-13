import paho.mqtt.client as mqtt
import sys

# Static data defining local host
LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_capture"

# Run when connected to local MQTT broker
def on_connect_local(client, userdata, flags, rc):
  print(f"connected to local broker with rc: {rc}")
  client.subscribe(LOCAL_MQTT_TOPIC)
	
# Run whenever a new message arrives -- a new image
def on_message(client,userdata, msg):
  try:
    print(f"New image received, size: {sys.getsizeof(msg.payload)} bytes")
  except:
    print(f"Unexpected error: {sys.exc_info()[0]}")

# Build up local MQTT client
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()