import json
from channels.generic.websocket import AsyncWebsocketConsumer

class APIConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join channel group
        await self.channel_layer.group_add(
            'api',
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave channel group
        await self.channel_layer.group_discard(
            'api',
            self.channel_name
        )

    async def receive(self, text_data):
        print('Recieved here')
        text_data_json = json.loads(text_data)
        payload = text_data_json['payload']

        # Send message to channel group
        await self.channel_layer.group_send(
            'api',
            {
                'type': 'payload',
                'payload': payload,
            }
        )

    # Receive message from channel group
    async def payload(self, event):
        payload = event['payload']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'payload': payload,
        }))
    