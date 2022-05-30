from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Goalie
from .serializers import GoalieSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_goalie(request):
    if request.method == 'POST':
        serializer = GoalieSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

@api_view(['PUT', 'GET'])
@permission_classes([IsAuthenticated])
def chosen_goalies(request, id):
    goalie = get_object_or_404(Goalie, pk = id)
    if request.method == 'PUT':
       serializer = GoalieSerializer(goalie, data = request.data) 
       serializer.is_valid(raise_exception = True)
       serializer.save()
       return Response(serializer.data)
    elif request.method == 'GET':
        goalies = Goalie.objects.filter(team_id=id)
        serializer = GoalieSerializer(goalies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    