from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Float, Integer, Completion, analyzer, tokenizer, token_filter
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# connections.create_connection()

my_analyzer = analyzer('my_analyzer',
                       tokenizer='standard',
                       filter=['lowercase', token_filter(
                           'edge_ngram_filter', type='edgeNGram',
                           min_gram=3, max_gram=20
                       )]
                       )


class StoryIndex(DocType):
    id = Integer()
    title = Text(
        analyzer=my_analyzer,
        search_analyzer='standard')
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
