from rest_framework import serializers
from .models import Team_Manager


class Team_ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Manager
        fields = ['id', 'first_name', 'last_name', 'email', 'user_id']
        
       