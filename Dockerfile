FROM python:2-onbuild

RUN mkdir /data
VOLUME /data

CMD [ "python", "articles_fetch_web_server.py" ]
