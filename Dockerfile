# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR app/
COPY . .
RUN mkdir -p /app/app/files

CMD ["python", "app/main.py"]
