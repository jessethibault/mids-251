FROM alpine:3.13
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
ENV AWS_SHARED_CREDENTIALS_FILE=/.aws/credentials
ENV AWS_CONFIG_FILE=/.aws/config
WORKDIR /app
RUN apk update 
RUN apk add bash
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip
#RUN a command to intall the MQTT python client
RUN pip3 install paho-mqtt
RUN pip3 install boto3
# Copy your listener.py file into the container
COPY image_processor.py ./
CMD python3 image_processor.py