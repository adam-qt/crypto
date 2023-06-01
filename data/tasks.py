from celery import app
from .utils import parse_data_from_api


@app.shared_task
def update_db():
    parse_data_from_api()
