from rest_framework import serializers
from .models import Goalie


class GoalieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goalie
        fields = ['id', 'first_name', 'last_name', 'team', 'shutouts', 'save_percentage', 'goals_against_average', 'wins']
