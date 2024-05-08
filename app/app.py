from fastapi import FastAPI

from app.routes import health

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


app = FastAPI()

app.include_router(health.router)

FastAPIInstrumentor.instrument_app(app)
