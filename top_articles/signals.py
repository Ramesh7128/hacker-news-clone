from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Story
from .search import StoryIndex

@receiver(post_save, sender=Story)
def index_story(sender, instance, **kwargs):
    instance.indexing()