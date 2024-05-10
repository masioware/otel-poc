# FROM python:3.11-alpine # don't have gcc and you can't install psutil
FROM python:3.11-slim

# if you're using alpine (install gcc)
# RUN apk update && \
#     apk add python3-dev \
#     gcc \
#     libc-dev \
#     libffi-dev

WORKDIR /api

COPY requirements.txt ./
COPY app ./app

RUN pip install -r requirements.txt

EXPOSE 8000

# CMD opentelemetry-instrument \
#     uvicorn app.app:app \
#     --host 0.0.0.0 \
#     --port 8000

CMD opentelemetry-instrument \
    python -m app __main__.py