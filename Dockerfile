# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY /requirements/_base.txt /code/
COPY /requirements/dev.txt /code/
RUN pip3 install --no-cache-dir -r _base.txt 
RUN pip3 install --no-cache-dir -r dev.txt
COPY . /code/
