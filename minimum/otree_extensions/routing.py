from channels.routing import route_class
from channels.generic.websockets import JsonWebsocketConsumer
import random
from minimum.models import Player


class TaskTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/tasktracker/(?P<player>[0-9]+)$')

    def prepare_task(self, player):
        return {'task': player.last_question,
                'num_answered': player.num_answered,
                'num_correct': player.num_correct, }

    def connect(self, message, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        if not player.last_question:
            player.last_question = random.randint(1, 99)
            player.save()
        response = self.prepare_task(player)
        self.send(response)

    def receive(self, text=None, bytes=None, **kwargs):
        player = Player.objects.get(id=self.kwargs['player'])
        player.num_answered += 1
        if text == 100 - player.last_question:
            player.num_correct += 1
        player.last_question = random.randint(1, 99)
        player.save()
        response = self.prepare_task(player)
        self.send(response)


channel_routing = [
    route_class(TaskTracker, path=TaskTracker.url_pattern),
]
