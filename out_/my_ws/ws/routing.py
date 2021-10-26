from django.urls import path
from .consumers import WSConsumer

websocket_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi())
]
