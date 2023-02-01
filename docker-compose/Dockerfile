# https://docs.docker.com/engine/reference/builder/

# Docker can build images automatically by reading the
# instructions from a Dockerfile. A Dockerfile is a text
# document that contains all the commands a user could
# call on the command line to assemble an image.

# syntax=docker/dockerfile:1
FROM python:3.7-alpine
LABEL maintainer=foroozf001
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
