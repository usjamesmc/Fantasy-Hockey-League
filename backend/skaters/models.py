from django.db import models
from teams.models import Team


class Skater(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    assists = models.IntegerField()
    plus_minus = models.IntegerField()
    power_play_points = models.IntegerField()
    shots = models.IntegerField()
    penalty_minutes = models.IntegerField()
    goals = models.IntegerField()