FROM python:3.11-alpine

WORKDIR /api

COPY requirements.txt ./
COPY app ./app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD opentelemetry-instrument \
    --metrics_exporter console,otlp \
    uvicorn app.app:app \
    --port 8000 \
    --host 0.0.0.0