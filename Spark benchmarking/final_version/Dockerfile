# syntax = docker/dockerfile:experimental
FROM python:3.8.11-buster

RUN apt update && apt install gettext python3-pip python3-dev -y
RUN apt-get install default-jre -y
WORKDIR /src
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .
CMD ["python", "a.py"]
