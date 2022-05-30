from rest_framework import serializers
from .models import Skater


class SkaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skater
        fields = ['id', 'first_name', 'last_name', 'team', 'position', 'shots', 'goals', 'plus_minus', 'power_play_points', 'penalty_minutes', 'assists']
      