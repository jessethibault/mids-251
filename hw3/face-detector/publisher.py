import paho.mqtt.client as mqtt
import sys

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_capture"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

#publish the message
local_mqttclient.publish(LOCAL_MQTT_TOPIC,"Hello MQTT...")