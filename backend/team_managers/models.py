from django.db import models
from authentication.models import User
from leagues.models import League


class Team_Manager(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
