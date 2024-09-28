from rest_framework import serializers

class UserDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=15)
    email = serializers.EmailField()
