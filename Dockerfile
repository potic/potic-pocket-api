FROM python:2-onbuild

EXPOSE 5000
ENV ENVIRONMENT_NAME test
CMD [ "python", "potic-pocket-api.py" ]
