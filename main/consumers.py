import openai
from channels.consumer import AsyncConsumer


class Consumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text_data['text']}
            ]
        )

        await self.send({
            "type": "websocket.send",
            "text": response['choices'][0]['message']['content']
        })

    async def websocket_disconnect(self, event):
        pass