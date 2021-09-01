FROM python:3.9.6-alpine
LABEL Author="Archana Sharma"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# apk - is the alpine application package manager
#  update is update the registry of the postgres-client
# no--cache means dont store the registry in the docker file--keep it lightweight
RUN apk add --update --no-cache postgresql-client
# install dependencies 
RUN apk add --update --no-cache --virtual .tmp-build-deps \
         gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

