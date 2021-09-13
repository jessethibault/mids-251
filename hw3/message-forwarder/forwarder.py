import paho.mqtt.client as mqtt
import sys

# Static data defining local host
LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_capture"

# Static data defining remote host
REMOTE_MQTT_HOST="18.118.218.53"
REMOTE_MQTT_PORT=32000
REMOTE_MQTT_TOPIC="image_store"

# Run when connected to local MQTT broker
def on_connect_local(client, userdata, flags, rc):
        print(f"connected to local broker with rc: {rc}")
        client.subscribe(LOCAL_MQTT_TOPIC)
	
# Run when connected to remote MQTT broker
def on_connect_remote(client, userdata, flags, rc):
        print(f"connected to remote broker with rc: {rc}")

# Run whenever a new message arrives -- a new image
def on_message(client,userdata, msg):
  try:
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print(f"Unexpected error:{sys.exc_info()[0]}")

# Build up local MQTT client
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# Build up remote MQTT client
remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

# go into a loop
local_mqttclient.loop_forever()