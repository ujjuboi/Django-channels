import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread, ChatMessage

class ChatConsumer(AsyncConsumer):
  async def websocket_connect(self, event): #async keyword makes the function communicate in asynchronous mode
    print("connected", event)

  async def websocket_recieve(self, event): 
    print("recieve", event)

  async def websocket_disconnect(self, event):
    print("disconnected", event)    