FROM python:3.6

# set working directory
RUN mkdir -p /app
WORKDIR /app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /app/requirements.txt

# install requirements
RUN pip install -r /app/requirements.txt

# add app
ADD . /app

# run spider
RUN scrapy crawl prawie

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
