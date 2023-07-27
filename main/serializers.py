from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    image1 = serializers.ImageField()
    image2 = serializers.ImageField()
    percentage = serializers.IntegerField()

    