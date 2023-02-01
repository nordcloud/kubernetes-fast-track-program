# https://docs.docker.com/engine/reference/builder/

# Docker can build images automatically by reading the
# instructions from a Dockerfile. A Dockerfile is a text
# document that contains all the commands a user could
# call on the command line to assemble an image.

# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
LABEL maintainer=foroozf001
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
