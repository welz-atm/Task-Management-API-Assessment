from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
import tasks.consumers as consumers

websocket_urlpatterns = [
    re_path(r'ws/tasks/$', consumers.TaskConsumer.as_asgi()),
]


