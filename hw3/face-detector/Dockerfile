FROM ubuntu:18.04
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip
#RUN a command to intall the MQTT python client
RUN pip3 install paho-mqtt
# Copy your listener.py file into the container
COPY publisher.py ./
CMD python3 publisher.py