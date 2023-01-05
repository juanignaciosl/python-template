FROM python:3.10-alpine

RUN apk add build-base

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/app"]
WORKDIR /app
