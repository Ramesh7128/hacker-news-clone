from django.apps import AppConfig
from elasticsearch_dsl import connections
from django.conf import settings


class TopArticlesConfig(AppConfig):
    name = 'top_articles'

    def ready(self):
        import top_articles.signals
        try:
            connections.create_connection()
        except Exception as e:
            print(e)
