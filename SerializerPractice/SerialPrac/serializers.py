from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 120)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length = 255)
