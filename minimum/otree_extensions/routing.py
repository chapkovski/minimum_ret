from channels.routing import route_class
from channels.generic.websockets import JsonWebsocketConsumer
import random
from minimum.models import Player


class TaskTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/tasktracker/(?P<player>[0-9]+)$')

    def connect(self, message, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        if not player.last_question:
            player.last_question = random.randint(1, 99)
            player.save()
        response = player.last_question
        self.send(response)

    def receive(self, text=None, bytes=None, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        print(text)
        response = random.randint(1, 99)
        self.send(response)


channel_routing = [
    route_class(TaskTracker, path=TaskTracker.url_pattern),
]
