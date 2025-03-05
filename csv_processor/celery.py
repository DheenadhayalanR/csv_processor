from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_processor.settings')

app = Celery('csv_processor')

# Load task modules from all registered Django apps
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from installed Django apps
app.autodiscover_tasks()
