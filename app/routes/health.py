from fastapi import APIRouter

from os import getenv

router = APIRouter()


@router.get('/')
def health_check():
    print(getenv('OTEL_EXPORTER_OTLP_ENDPOINT'))
    return {'status': 'OK'}
