from elasticsearch import Elasticsearch
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

es = Elasticsearch(['es'])
consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
for message in consumer:
    product = json.loads((message.value).decode('utf-8'))
    es.index(index='listing_index', doc_type='listing', id=product['id'], body=product)
    es.indices.refresh(index='listing_index')
