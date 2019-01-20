from rest_framework import serializers
from top_articles.models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Story
        fields = '__all__'