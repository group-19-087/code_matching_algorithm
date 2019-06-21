FROM python:slim

RUN	mkdir -p usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app

RUN apt-get update -y
RUN apt-get install ffmpeg -y
RUN apt-get install tesseract-ocr -y
RUN apt-get install libsm6 libxrender1 libfontconfig1
RUN pip install opencv-contrib-python
RUN	pip install --trusted-host pypi.python.org -r requirements.txt





