FROM ubuntu:18.04
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip python3-opencv vim-tiny libopencv-dev
RUN pip3 install --upgrade pip
RUN pip3 install Cython
RUN pip3 install tensorflow -f https://tf.kmtea.eu/whl/stable.html
RUN pip3 install keras
COPY piece-identifier.py piece-identifier.py
COPY /models/ /usr/models/
CMD python3 piece-identifier.py