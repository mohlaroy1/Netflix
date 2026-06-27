from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

#class ActorsAPIView(APIView):
    #def get(self, request):
        #actors = Actor.objects.all()
        #serializer = ActorSerializer(actors, many=True)
        #return Response(serializer.data)

#class ActorCreateAPIView(APIView):
    #def post(self, request):
        #serializer = ActorSerializer(data=request.data)
        #if serializer.is_valid():
            #Actor.objects.create(
                #name=serializer.validated_data.get('name'),
                #gender=serializer.validated_data.get('gender'),
                #country=serializer.validated_data.get('country'),
                #birthdate=serializer.validated_data.get('birthdate'),
            #)
            #response = {
                #"message": "Actor created successfully",
                #"data": serializer.data
            #}
            #return Response(response, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#class ActorRetrieveAPIView(APIView):
    #def get(self, request, pk):
        #actor = get_object_or_404(Actor, pk=pk)
        #serializer = ActorSerializer(actor)
        #return Response(serializer.data)


#class ActorUpdateAPIView(APIView):
    #def put(self, request, pk):
        #actor = get_object_or_404(Actor, pk=pk)
        #serializer = ActorSerializer(data=request.data, instance=actor)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(
                #{
                    #"message": "Actor updated successfully",
                    #"data": serializer.data
                #},
                #status=status.HTTP_200_OK
            #)
        #return Response(
            #{
                #"success": False,
                #"errors": serializer.errors
            #},
            #status=status.HTTP_400_BAD_REQUEST
        #)


#class ActorDeleteAPIView(APIView):
    #def delete(self, request, pk):
        #actor = get_object_or_404(Actor, pk=pk)
        #actor.delete()
        #return Response({"message": "Actor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


#class SubscriptionAPIView(APIView):
    #def get(self, request):
        #subscriptions = Subscription.objects.all()
        #serializer = SubscriptionSerializer(subscriptions, many=True)
        #return Response(serializer.data)


#class SubscriptionCreateAPIView(APIView):
    #def post(self, request):
        #serializer = SubscriptionSerializer(data=request.data)
        #if serializer.is_valid():
            #Subscription.objects.create(
                #name=serializer.validated_data.get('name'),
                #price=serializer.validated_data.get('price'),
                #duration=serializer.validated_data.get('duration'),
            #)
            #response = {
                #"message": "Subscription created successfully",
                #"data": serializer.data
            #}
            #return Response(response, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class SubscriptionRetrieveAPIView(APIView):
    #def get(self, request, pk):
        #subscription = get_object_or_404(Subscription, pk=pk)
        #serializer = SubscriptionSerializer(subscription)
        #return Response(serializer.data)


#class MoviesAPIView(APIView):
    #def get(self, request):
        #movies = Movie.objects.all()
        #serializer = MovieSerializer(movies, many=True)
        #return Response(serializer.data)

    #def post(self, request):
        #serializer = MovieSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['get'])
    def actors(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='add-actor')
    def add_actor(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        instance = serializer.instance
        movie.actors.add(instance)
        return Response(
            {
                "message": f"Actor added successfully. (Movie: {movie.id})",
                "actor_data": serializer.data
            }
        )
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return MovieSafeSerializer
        return MovieSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.user != self.request.user:
            return Response(
                {"message": "You can't delete this comment"},
                status=status.HTTP_403_FORBIDDEN
            )
        comment.delete()
        return Response("Comment deleted successfully")



















