from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'release_date', 'duration', 'rating','genre','image']