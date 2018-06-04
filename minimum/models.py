from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from django import forms
from django.forms.widgets import NumberInput
from django.db import models as djmodels
from django.db import models as djmodels
from django.db.models import F
import json

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
    ...