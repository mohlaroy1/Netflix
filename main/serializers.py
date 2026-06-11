from rest_framework import serializers

class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    gender = serializers.CharField()
    birthdate = serializers.DateField()


class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    price = serializers.FloatField()
    duration = serializers.DurationField()