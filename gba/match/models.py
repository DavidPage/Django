from django.db.models.fields import CharField
from django.db import models

# Create your models here.

class Match(models.Model):
    competition_name = CharField(max_length=20)