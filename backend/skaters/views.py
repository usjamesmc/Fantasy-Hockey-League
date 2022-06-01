from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Skater
from .serializers import SkaterSerializer

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def any_skaters(request):
    if request.method == 'POST':
        serializer = SkaterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    elif request.method == 'GET':
        skaters = Skater.objects.all()
        serializer = SkaterSerializer(skaters, many=True)
        return Response(serializer.data)
    

@api_view(['PUT', 'GET'])
@permission_classes([IsAuthenticated])
def chosen_skaters(request, id):
    skater = get_object_or_404(Skater, pk = id)
    if request.method == 'PUT':
       serializer = SkaterSerializer(skater, data = request.data) 
       serializer.is_valid(raise_exception = True)
       serializer.save()
       return Response(serializer.data)
    elif request.method == 'GET':
        skaters = Skater.objects.filter(team_id=id)
        serializer = SkaterSerializer(skaters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
