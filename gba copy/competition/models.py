from django.db import models

# Create your models here.
from django.db.models.fields import CharField


class Competition(models.Model):
    competition_name = CharField(max_length=20)

    def __str__(self):
        return self.competition_name
