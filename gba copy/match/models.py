from django.db import models
from team.models import Team
from competition.models import Competition

# Create your models here.

class Match(models.Model):
    competition = models.ForeignKey(Competition, related_name="competition")
    homeTeam = models.ForeignKey(Team, related_name="home")
    awayTeam = models.ForeignKey(Team, related_name="away")

    def __str__(self):
        return self.homeTeam.team_name + ' vs ' + self.awayTeam.team_name