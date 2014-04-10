from django.db.models.fields import CharField
from django.db import models
from team.models import Team
from competition.models import Competition

# Create your models here.

class Match(models.Model):
    competition = models.ForeignKey(Competition, related_name="competition")
    homeTeam = models.ForeignKey(Team, related_name="home")
    awayTeam = models.ForeignKey(Team, related_name="away")