import paho.mqtt.client as mqtt
import sys
import time
import os
import numpy as np
import csv
import keras
from keras.preprocessing import image

# Load trained model
model = keras.models.load_model('./models')

# Static data defining local host
LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_store"

files = list()

with open('labels.csv', newline='') as f:
  reader = csv.reader(f)
  labels = list(reader)[0]

# Run when connected to local MQTT broker
def on_connect_local(client, userdata, flags, rc):
  print(f"connected to local broker with rc: {rc}")
  client.subscribe(LOCAL_MQTT_TOPIC)

# Keep for debugging purposes
def write_to_file(payload):
  file_name = f"./data/images/{round(time.time() * 1000000)}.jpg"
  files.append(file_name)

  f = open(file_name, "wb")
  f.write(payload)
  f.close()

  if len(files) >= 10:
    make_prediction()

# Write payload to S3 using boto3
def make_prediction():
  image_dataset = image.image_dataset_from_directory('./data')

  most_common = np.argmax(model.predict(image_dataset), axis=-1)

  for file in files:
    os.remove(file)
 
  files.clear()

  print(labels[np.bincount(most_common).argmax()])

# Run whenever a new message arrives -- a new image
def on_message(client,userdata, msg):
  try:
    print('Received image')
    write_to_file(msg.payload)
  except:
    print(f"Unexpected error: {sys.exc_info()[0]} -- {sys.exc_info()[1]} -- {sys.exc_info()[2]}")


# Build up local MQTT client
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
