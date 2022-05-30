from django.db import models
from team_managers.models import Team_Manager
from leagues.models import League


class Team(models.Model):
    team_manager = models.ForeignKey(Team_Manager, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    ranking = models.IntegerField()
    