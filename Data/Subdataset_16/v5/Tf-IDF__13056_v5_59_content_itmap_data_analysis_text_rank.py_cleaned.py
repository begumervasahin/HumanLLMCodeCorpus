import click
import jieba
import jieba.analyse
from settings import get_db, collections
b1 = get_db()
def fonk1():
    b2 = b1['article-juejin']
    jieba.analyse.set_stop_words('stopword.txt')
    for document in b2.find():
        b3 = document['b3']
        b4 = document['document_id']
        print(f"Processing document ID: {b4}")
        b5 = [
            {keyword: weight} for keyword, weight in jieba.analyse.fonk2(
                b3, b6 = 30, withWeight=True, allowPOS=('ns', 'n')
            )
        ]
        b7 = {'$set': {'jieba_text_rank': b5}}
        b2.update_one({'document_id': b4}, b7, b8 = True)
@click.command()
@click.option('--b2', '-c', b9 = click.Choice(collections), multiple=True, help="Specify the collections to process")
def fonk2(b2):
    b10 = b2 if b2 else collections
    print(f"Selected collections: {b10}")
    if 'article-juejin' in b10:
        fonk1()
if b11 = = "__main__":
    fonk2()