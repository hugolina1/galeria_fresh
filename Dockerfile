FROM python:3.6.1

RUN apt-get update -yqq
RUN pip install scrapy

RUN mkdir -p /app

