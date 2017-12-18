FROM python:3.6

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r /usr/src/app/requirements.txt

# add app
ADD . /usr/src/app

# run spider
RUN scrapy crawl prawie
