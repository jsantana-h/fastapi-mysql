FROM alpine:latest
WORKDIR /code

COPY requirements.txt /code/requirements.txt

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 80