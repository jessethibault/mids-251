import paho.mqtt.client as mqtt
import sys
import time
import boto3

# Static data defining local host
LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_store"

# Run when connected to local MQTT broker
def on_connect_local(client, userdata, flags, rc):
  print(f"connected to local broker with rc: {rc}")
  client.subscribe(LOCAL_MQTT_TOPIC)

# Keep for debugging purposes
def write_to_file(payload):
  f = open(f"{round(time.time() * 1000000)}.png", "wb")
  f.write(payload)
  f.close()

# Write payload to S3 using boto3
def write_to_s3(payload):
  resp = boto_client.put_object(ACL='public-read', Body=payload, Bucket='hw3-faces', Key=f"{round(time.time() * 1000000)}.png")
  if resp['ResponseMetadata']['HTTPStatusCode'] != 200:
    print(f"Error pushing file: {resp}")

# Run whenever a new message arrives -- a new image
def on_message(client,userdata, msg):
  try:
    write_to_s3(msg.payload)
  except:
    print(f"Unexpected error: {sys.exc_info()[0]} -- {sys.exc_info()[1]} -- {sys.exc_info()[2]}")

# Build up local MQTT client
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# Boto3 client for S3 access
boto_client = boto3.client('s3')

# go into a loop
local_mqttclient.loop_forever()
