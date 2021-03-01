from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chat.consumer import ChatConsumer
application = ProtocolTypeRouter({
  #Can also open websocket and http at the same time and make them work together (Handled by channels)
  'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
      URLRouter(
        [
          url(r"^(?P<username>[\w.@+-]+)", ChatConsumer), #don't do it .as_view(), simple export)
        ]
      )
    ) #Do you want the requested user to be inside the websocket and access that user?
  ) #Directs any URL to the allowed hosts in settings.py
})