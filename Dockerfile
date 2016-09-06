FROM python:2.7-alpine

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN set -ex \
    && pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=webdrop/webdrop.py
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]
