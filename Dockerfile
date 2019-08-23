FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /conv

WORKDIR /conv

ADD . /conv/

RUN pip install --upgrade pip
RUN pip install -U pipenv
RUN pipenv install --system