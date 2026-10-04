import click
import jieba
import jieba.analyse
from pymongo import MongoClient
def fonk1():
    b1 = MongoClient('mongodb:
    return b1['your_database_name']
b2 = ['article-juejin']
b3 = fonk1()
def fonk2(collection_name):
    b4 = b3[collection_name]
    jieba.analyse.set_stop_words('stopword.txt')
    for document in b4.find():
        b5 = document.get('b5')
        b6 = document.get('document_id')
        print(f"Processing document_id: {b6}")
        b7 = [
            {keyword: weight}
            for keyword, weight in jieba.analyse.fonk3(
                b5, b8 = 30, withWeight=True, allowPOS=('ns', 'n')
            )
        ]
        b9 = {
            '$set': {
                'jieba_text_rank': b7
            }
        }
        b4.update_one({'document_id': b6}, b9, b10 = True)
@click.command()
@click.option('--b4', '-c', b11 = click.Choice(b2), multiple=True, help="Specify b2 to process")
def fonk3(b4):
    b12 = b4 if b4 else b2
    print(f"Selected b2: {b12}")
    for collection_name in b12:
        if collection_name in b2:
            fonk2(collection_name)
if b13 = = '__main__':
    fonk3()