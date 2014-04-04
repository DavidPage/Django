#from django.contrib.localflavor.generic.forms import DateTimeField
from django.db.models.fields import CharField
from django.db import models
from competition.models import Competition
from market.models import Market
from team.models import Team


class Trade(models.Model):
    homeTeam = models.ForeignKey(Team, related_name="home")
    awayTeam = models.ForeignKey(Team, related_name="away")
    competition = models.ForeignKey(Competition, related_name="competition")
    market = models.ForeignKey(Market, related_name="market")

    invested = CharField(max_length=20)
    profitLoss = CharField(max_length=20)
    #dateTrade = models.DateTimeField()

    def __str__(self):
        return self.invested

    def divide(self):
        return (int(self.profitLoss) * 100) / int(self.invested)