import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop', backend='amqp', broker='amqp://')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# celery -A myshop worker -l info
# sudo systemctl start rabbitmq-server
