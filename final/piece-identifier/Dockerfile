FROM ubuntu:18.04
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip python3-opencv vim-tiny libopencv-dev
RUN pip3 install --upgrade pip
RUN pip3 install Cython
RUN pip3 install paho-mqtt
RUN pip3 install tensorflow
RUN pip3 install keras
RUN mkdir data
RUN mkdir data/images
COPY piece-identifier.py piece-identifier.py
COPY labels.csv labels.csv
ADD models/ models
CMD python3 piece-identifier.py