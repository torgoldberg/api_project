FROM python:3.9-slim

WORKDIR /usr/src/api_tests

COPY ./admin_console_tests/requirements.txt ./
RUN pip install -U pytest
RUN pip install -r requirements.txt

ENV MACHINE=local
ENV DB_HOSTS=test
ENV DB_USER=root
ENV DB_PASSWORD=4401

COPY . .

WORKDIR /usr/src/api_tests/admin_console_tests
CMD pytest -m sanity