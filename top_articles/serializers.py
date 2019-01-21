from rest_framework import serializers
from top_articles.models import Story
from drf_haystack.serializers import HaystackSerializer
from top_articles.search_Indexes import StoryIndex

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Story
        fields = '__all__'

class StoryIndexSerializer(HaystackSerializer):
    class Meta:
        index_classes=[StoryIndex] 
        fields=['text', 'title']