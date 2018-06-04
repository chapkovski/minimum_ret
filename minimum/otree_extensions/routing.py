from channels.routing import route, route_class
from channels.generic.websockets import WebsocketConsumer
# from pggfg.models import Player TODO importing later
import json
import random


class TaskTracker(WebsocketConsumer):
    url_pattern = (r'^/tasktracker/$')

    def connect(self, message, **kwargs):
        response = random.randint(1, 99)
        self.send(response)

    def receive(self, text=None, bytes=None, **kwargs):
        response = random.randint(1, 99)
        self.send(response)

    def send(self, content):
        self.message.reply_channel.send({'text': json.dumps(content)})


channel_routing = [
    route_class(TaskTracker, path=TaskTracker.url_pattern),
]
