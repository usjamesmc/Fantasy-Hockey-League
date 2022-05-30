from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import TeamSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_team(request):
    if request.method == 'POST':
            serializer = TeamSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)