from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/api/$', consumers.APIConsumer.as_asgi()),
    # re_path(r'ws/api/(?P<id>\w+)/$', consumers.APIDetailsConsumer.as_asgi()),
]