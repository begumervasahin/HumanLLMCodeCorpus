import click
import jieba
import jieba.analyse
from pymongo import MongoClient
def get_db():
    client = MongoClient('mongodb:
    return client['your_database_name']
collections = ['article-juejin']
db = get_db()
def process_text_rank_for_collection(collection_name):
    collection = db[collection_name]
    jieba.analyse.set_stop_words('stopword.txt')
    for document in collection.find():
        body = document.get('body')
        doc_id = document.get('document_id')
        print(f"Processing document_id: {doc_id}")
        ranks = [
            {keyword: weight}
            for keyword, weight in jieba.analyse.textrank(
                body, topK=30, withWeight=True, allowPOS=('ns', 'n')
            )
        ]
        update_data = {
            '$set': {
                'jieba_text_rank': ranks
            }
        }
        collection.update_one({'document_id': doc_id}, update_data, upsert=True)
@click.command()
@click.option('--collection', '-c', type=click.Choice(collections), multiple=True, help="Specify collections to process")
def textrank(collection):
    selected_collections = collection if collection else collections
    print(f"Selected collections: {selected_collections}")
    for collection_name in selected_collections:
        if collection_name in collections:
            process_text_rank_for_collection(collection_name)
if __name__ == '__main__':
    textrank()