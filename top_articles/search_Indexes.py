from haystack import indexes
from top_articles.models import Story
import datetime

class StoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        use_template=True,
        template_name='/home/ramesh/wealthScore/hackerNewsClone/top_articles/templates/search/indexes/top_articles/story_text.txt'
    )
    title = indexes.CharField(model_attr='title')
    
    def get_model(self):
        return Story

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

