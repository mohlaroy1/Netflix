from rest_framework import serializers

class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    gender = serializers.CharField()
    birthdate = serializers.DateField()
