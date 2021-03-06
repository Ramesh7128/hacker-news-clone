from django.contrib import admin
from .models import Story
from .models import User
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display=('title', 'sentiment_score')
    search_fields = ('title', 'sentiment_score', 'order_no')

admin.site.register(Story, StoryAdmin)
admin.site.register(User)