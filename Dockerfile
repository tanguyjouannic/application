# syntax=docker/dockerfile:1
FROM python:3
COPY ./app/ /app/
CMD python3 /app/server.py