from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
class DemoViewSet(APIView):
    
    #  权限限制
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response({"message": "Hello11 World"}, status=status.HTTP_200_OK)
