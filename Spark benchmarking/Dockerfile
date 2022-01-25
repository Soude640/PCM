# syntax = docker/dockerfile:experimental
FROM python:3.8.11-buster

WORKDIR /src
COPY ./requirements.txt .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip cache list
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt
COPY ./src .
CMD ["python", "a.py"]
