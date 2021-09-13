import paho.mqtt.client as mqtt
import sys

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_capture"

REMOTE_MQTT_HOST="18.118.218.53"
REMOTE_MQTT_PORT=31801
REMOTE_MQTT_TOPIC="image_store"

def on_connect_local(client, userdata, flags, rc):
        print(f"connected to local broker with rc: {rc}")
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_connect_remote(client, userdata, flags, rc):
        print(f"connected to remote broker with rc: {rc}")

def on_message(client,userdata, msg):
  try:
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print(f"Unexpected error:{sys.exc_info()[0]}")

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

# go into a loop
local_mqttclient.loop_forever()