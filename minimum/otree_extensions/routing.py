from channels.routing import route_class
from channels.generic.websockets import JsonWebsocketConsumer
import random


class TaskTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/tasktracker$')

    def connect(self, message, **kwargs):
        response = random.randint(1, 99)
        self.send(response)

    def receive(self, text=None, bytes=None, **kwargs):
        response = random.randint(1, 99)
        self.send(response)


channel_routing = [
    route_class(TaskTracker, path=TaskTracker.url_pattern),
]
