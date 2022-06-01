from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import Team_ManagerSerializer
from django.shortcuts import get_object_or_404
from .models import Team_Manager

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_manager(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = Team_ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def chosen_team_manager(request, pk):
    team_manager = get_object_or_404(Team_Manager, pk = pk)
    if request.method == 'PUT':
       serializer = Team_ManagerSerializer(team_manager, data = request.data) 
       serializer.is_valid(raise_exception = True)
       serializer.save()
       return Response(serializer.data)
