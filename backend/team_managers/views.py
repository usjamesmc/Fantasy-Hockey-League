from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import Team_ManagerSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_manager(request):
    if request.method == 'POST':
            serializer = Team_ManagerSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)