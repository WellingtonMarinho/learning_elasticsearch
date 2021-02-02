from elasticsearch_dsl import analyzer
from elasticsearch_dsl.connections import  connections
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document, fields
from .models import People

connections.create_connection(hosts=['localhost'])

html_strip = analyzer('html_strip',
                      tokenizer='standard',
                      filter=['lowercase', 'stop', 'snowball'],
                      char_filter=['html_strip'])

@registry.register_document
class PeoplesDocument(Document):
    name = fields.TextField()
    address = fields.TextField()
    birthdate = fields.DateField()

    class Index:
        name = 'people_data'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:

        model = People
