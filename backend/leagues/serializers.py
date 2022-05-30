from rest_framework import serializers
from .models import League


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'name']
        

