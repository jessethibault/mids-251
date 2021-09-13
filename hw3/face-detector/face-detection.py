import paho.mqtt.client as mqtt
import numpy as np
import cv2

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

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initiate video capture
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to gray image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Capture face data from frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # For each face, encode as .png file and fire off to the MQTT broker
    for (x,y,w,h) in faces:
        face = gray[y:y+h, x:x+w]
        rc,png = cv2.imencode('.png', face)
        msg = png.tobytes()
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)