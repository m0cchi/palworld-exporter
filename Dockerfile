FROM python:3.10

ADD . /usr/local/app
WORKDIR /usr/local/app
RUN cd /usr/local/bin && curl -O https://raw.githubusercontent.com/m0cchi/wait_for_tcp/master/wait_for_http.py && chmod +x wait_for_http.py

RUN pip install -r requirements.txt


CMD bash bootstrap.sh

