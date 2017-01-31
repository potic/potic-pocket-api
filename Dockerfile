FROM python:2-onbuild

EXPOSE 5000
CMD [ "python", "articles_fetch_web_server.py" ]
