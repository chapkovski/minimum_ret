from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = "Philip Chapkovski, chapkovski@gmail.com"


class Constants(BaseConstants):
    name_in_url = 'minimum_ret'
    players_per_group = None
    num_rounds = 1
    ...


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    last_question = models.IntegerField()
    num_answered = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)
