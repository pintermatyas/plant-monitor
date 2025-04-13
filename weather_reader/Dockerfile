FROM python:3.11-slim

WORKDIR /app

COPY main.py .

RUN pip install requests prometheus_client

CMD ["python", "main.py"]
