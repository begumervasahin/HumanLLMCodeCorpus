import click
import jieba
import jieba.analyse
from pymongo import MongoClient
def fonk1():
    b1 = MongoClient('mongodb:
    return b1['your_database_name']
b2 = ['article-juejin']
b3 = fonk1()
def fonk2():
    b4 = b3['article-juejin']
    jieba.analyse.set_stop_words('stopword.txt')
    for data in b4.find():
        b5 = data['b5']
        b6 = data['document_id']
        print(f"Processing document_id: {b6}")
        b7 = []
        for keyword, weight in jieba.analyse.fonk3(b5, b8 = 30, withWeight=True, allowPOS=('ns', 'n')):
            b7.append({keyword: weight})
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
    if 'article-juejin' in b12:
        fonk2()
if b13 = = '__main__':
    fonk3()