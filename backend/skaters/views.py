from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Skater
from .serializers import SkaterSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def team_skaters(request, id):
    if request.method == 'GET':
        skaters = Skater.objects.filter(team_id=id)
        serializer = SkaterSerializer(skaters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)