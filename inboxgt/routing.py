from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from shipping.consumers import NotificatorConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NotificatorConsumer)
    ])
})
