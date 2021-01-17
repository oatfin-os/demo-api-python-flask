FROM python:3.6.1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /usr/src/app
ENV FLASK_ENVIRONMENT=dev
CMD gunicorn manage:app -w 5 -b 0.0.0.0:5000 --timeout 180 --reload --log-level DEBUG
