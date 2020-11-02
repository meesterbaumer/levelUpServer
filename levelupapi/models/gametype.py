"""Game type model module"""
from django.db import models


class GameType(models.Model):
    """Gametype database model"""
    label = models.CharField(max_length=25)
