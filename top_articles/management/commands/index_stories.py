from django.core.management.base import BaseCommand

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Index, connections
from top_articles.models import Story
from top_articles.search import StoryIndex
from top_articles import models


class Command(BaseCommand):
    help = 'indexes stories from hackernews'

    def handle(self, *args, **kwargs):
        try:
            es = Elasticsearch()
            es.indices.close(index="story-index")
            es.indices.delete(index="story-index")
        except Exception as error:
            pass
        StoryIndex.init(index='story-index')
        bulk(client=es, actions=(b.indexing()
                                 for b in models.Story.objects.all().iterator()))
