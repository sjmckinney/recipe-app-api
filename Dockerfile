# Use python alpine image
FROM python:3.7-alpine

# Optional MAINTAINER information
MAINTAINER stevejmckinney@gmail.com

# Instruct python to run unbuffered in image
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt to image
# and use as basis for pip install
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Create app directory in image and copy
# contents of project app directory to it
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Add specific user for image to run under
RUN adduser -D user
USER user
