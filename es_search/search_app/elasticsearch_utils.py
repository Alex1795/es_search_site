from django.conf import settings
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from .elasticsearch_utils import search_products
from django.shortcuts import  render

# Connect to Elasticsearch
es = Elasticsearch(hosts=[settings.ELASTICSEARCH_URL])


def search_products(query):
    """
    Search for products in Elasticsearch based on the given query.
    """
    search = Search(using=es, index='products')

    if query:
        search = search.query('multi_match', query=query, fields=['name', 'description'])

    response = search.execute()
    return [hit.to_dict() for hit in response]


