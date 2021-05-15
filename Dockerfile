FROM python:3.7-slim-buster

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /tmp/outputs
RUN mkdir /tmp/inputs
RUN mkdir /tmp/config

COPY src/ /src
WORKDIR /src

ENTRYPOINT ["python","main.py"]