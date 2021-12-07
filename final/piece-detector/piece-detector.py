import paho.mqtt.client as mqtt
import cv2
import time

# Static data defining local host
LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_capture"

# Build up local MQTT client
def on_connect_local(client, userdata, flags, rc):
        print(f"connected to local broker with rc: {rc}")

# Run when connected to local MQTT broker
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# Initiate video capture
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resize to image size indentifier is expecting (and save tons of space)
    dim = (128, 128)
    resized = cv2.resize(frame, dim)

    # Encode and send
    rc,jpg = cv2.imencode('.jpg', resized)
    msg = jpg.tobytes()
    local_mqttclient.publish(LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)

    time.sleep(0.1)