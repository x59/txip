FROM python:3-alpine

MAINTAINER Yehuda Deutsch <yeh@uda.co.il>

WORKDIR /var/www/txip
RUN apk add --update alpine-sdk
RUN pip install pipenv && pipenv install klein

VOLUME ["/var/www/txip"]
CMD ["pipenv", "run", "python", "app.py"]
