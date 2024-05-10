### Safe utilization

https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/security-best-practices.md#safeguards-against-denial-of-service-attacks

### Metrics Endpint (inside docker network)

http://otel-collector:8889/metrics

### Considerations about Dockerfile

`FROM python:3.11-alpine` don't have gcc and you can't install psutil, use `FROM python:3.11-slim` instead

```Dockerfile
# if you're using alpine (install gcc)
RUN apk update && \
apk add python3-dev \
gcc \
libc-dev \
libffi-dev
```
