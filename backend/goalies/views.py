from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Goalie
from .serializers import GoalieSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def team_goalies(request, id):
    if request.method == 'GET':
        goalies = Goalie.objects.filter(team_id=id)
        serializer = GoalieSerializer(goalies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)