from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Float, Integer, Completion, analyzer, tokenizer, token_filter
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# connections.create_connection()

my_analyzer = analyzer('my_analyzer',
                       tokenizer='standard',
                       filter=['lowercase', token_filter(
                           'edge_ngram_filter', type='edgeNGram',
                           min_gram=1, max_gram=20
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
