from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    image1 = serializers.CharField()
    image2 = serializers.CharField()
    percentage = serializers.IntegerField()

    