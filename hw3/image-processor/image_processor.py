import paho.mqtt.client as mqtt
import sys
import time
import boto3

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="image_store"

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
  print('write_to_s3 start')
  resp = boto_client.put_object(ACL='public-read', Body=payload, Bucket='hw3-faces', Key=f"{round(time.time() * 1000000)}.png")
  if resp['ResponseMetadata']['HTTPStatusCode'] != 200:
    print(f"Error pushing file: {resp}")
  print('write_to_s3 end')

def on_message(client,userdata, msg):
  try:
    print('on_message start')
    write_to_s3(msg.payload)
    print('on_message end')
  except:
    print(f"Unexpected error: {sys.exc_info()[0]} -- {sys.exc_info()[1]} -- {sys.exc_info()[2]}")

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message
boto_client = boto3.client('s3')
print('startup even working?')
# go into a loop
local_mqttclient.loop_forever()
