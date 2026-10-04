import click
import jieba
import jieba.analyse
from settings import get_db, collections
db = get_db()
def process_text_rank_for_article_juejin():
    collection = db['article-juejin']
    jieba.analyse.set_stop_words('stopword.txt')
    for document in collection.find():
        body = document['body']
        doc_id = document['document_id']
        print(f"Processing document ID: {doc_id}")
        ranks = [
            {keyword: weight} for keyword, weight in jieba.analyse.textrank(
                body, topK=30, withWeight=True, allowPOS=('ns', 'n')
            )
        ]
        update_data = {'$set': {'jieba_text_rank': ranks}}
        collection.update_one({'document_id': doc_id}, update_data, upsert=True)
@click.command()
@click.option('--collection', '-c', type=click.Choice(collections), multiple=True, help="Specify the collections to process")
def textrank(collection):
    selected_collections = collection if collection else collections
    print(f"Selected collections: {selected_collections}")
    if 'article-juejin' in selected_collections:
        process_text_rank_for_article_juejin()
if __name__ == "__main__":
    textrank()