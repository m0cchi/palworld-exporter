FROM python:3.10

ADD . /usr/local/app
WORKDIR /usr/local/app

RUN pip install -r requirements.txt

CMD python exporter.py

