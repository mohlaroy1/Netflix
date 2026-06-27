from rest_framework import serializers

from .models import Movie, Actor, Comment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    price = serializers.FloatField()
    duration = serializers.DurationField()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSafeSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = Movie
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("user", "created_at")