from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Float, Completion, analyzer, tokenizer
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# connections.create_connection()

my_analyzer = analyzer('my_analyzer',
                       tokenizer=tokenizer(
                           'trigram', 'edge_ngram', min_gram=1, max_gram=20),
                       filter=['lowercase']
                       )


class StoryIndex(DocType):
    title = Text(analyzer=my_analyzer)
    author = Text()
    score = Float()
    link = Text()
    timestamp = Text()
    created_at = Date()
    sentiment_score = Float()


# def bulk_indexing():
#     StoryIndex.init(index='story-index')
#     es = Elasticsearch()
#     es.indices.delete(index='story-index')
#     bulk(client=es, actions=(b.indexing()
#                              for b in models.Story.objects.all().iterator()))
