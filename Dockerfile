# Use python alpine image
FROM python:3.7-alpine

# Optional MAINTAINER information
MAINTAINER stevejmckinney@gmail.com

# Instruct python to run unbuffered in image
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt to image
# and use as basis for pip install
# Use apk (Alpine Package Manager)
# to install db client
# --no-cache directs Docker not to
# store package registry index on
# Docker image to keep size to minimum
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache postgresql-client --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Create app directory in image and copy
# contents of project app directory to it
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Add specific user for image to run under
RUN adduser -D user
USER user
