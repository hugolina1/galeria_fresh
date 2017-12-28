FROM python:3.6
RUN apt-get update

ADD . /home/galeria

RUN pip install -r /home/galeria/requirements.txt

COPY start_crawl.py /cmd/start_crawl.py

ENTRYPOINT python /cmd/start_crawl.py
