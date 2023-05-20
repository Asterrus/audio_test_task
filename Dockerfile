FROM python:3.11.1-alpine

WORKDIR /web

COPY requirements.txt .

RUN apk add --no-cache ffmpeg && pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000