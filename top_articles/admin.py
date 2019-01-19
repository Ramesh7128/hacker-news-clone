from django.contrib import admin
from .models import Story
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display=('title', 'sentiment_score')
    search_fields = ('title', 'sentiment_score')

admin.site.register(Story, StoryAdmin)