FROM python:3.7-alpine

ADD . /
RUN pip install -r /requirements.txt

WORKDIR /app
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:80", "service.main:app"]
