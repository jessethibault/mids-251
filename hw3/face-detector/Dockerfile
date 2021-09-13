FROM ubuntu:18.04
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip python3-opencv vim-tiny libopencv-dev
RUN pip3 install paho-mqtt
RUN pip3 install Cython
RUN pip3 install numpy
COPY face-detection.py face-detection.py
COPY haarcascade_frontalface_default.xml haarcascade_frontalface_default.xml
CMD python3 face-detection.py