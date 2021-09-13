from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
class MusicViewSet(APIView):
    def get(self, request, format=None):
        print(request.query_params)
        return Response({"message": "From music"}, status=status.HTTP_200_OK)



@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request):
    return Response({"message": "somessss"}, status=status.HTTP_200_OK)