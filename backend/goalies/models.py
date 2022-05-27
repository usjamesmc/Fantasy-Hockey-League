from django.db import models
from teams.models import Team


class Goalie(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shutouts = models.IntegerField()
    save_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    goals_against_average = models.DecimalField(max_digits=3, decimal_places=1)
    wins = models.IntegerField()