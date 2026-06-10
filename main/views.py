from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import *
from .serializers import *

class ActorsAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

class ActorCreateAPIView(APIView):
    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            Actor.objects.create(
                name=serializer.validated_data.get('name'),
                gender=serializer.validated_data.get('gender'),
                country=serializer.validated_data.get('country'),
                birthdate=serializer.validated_data.get('birthdate'),
            )
            response = {
                "message": "Actor created successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ActorRetrieveAPIView(APIView):
    def get(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)