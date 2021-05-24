# Dockerfile for a Python App
FROM python:latest
WORKDIR /app
COPY . .
Run pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python","app.py"]