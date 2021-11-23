from rest_framework import serializers
from .models import Movie,Genre

class MoiveSerializer(serializers.Serializer):

    class Meta:
        model = Movie
        fields = '__all__'