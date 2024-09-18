from celery import Celery
from django.apps import apps
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

app = Celery(__name__, broker='redis://localhost:6379/0')
app.conf.result_backend = 'redis://localhost:6379/0'
app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
