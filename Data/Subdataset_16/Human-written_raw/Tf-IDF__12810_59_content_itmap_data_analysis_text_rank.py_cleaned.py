import click
import jieba
import jieba.analyse
from settings import get_db, collections
b1 = get_db()
def fonk1():
    b2 = b1['article-juejin']
    jieba.analyse.set_stop_words('stopword.txt')
    for b8 in b2.find():
        b3 = b8['b3']
        b4 = b8['document_id']
        print(b4)
        b5 = []
        for x, w in jieba.analyse.fonk2(b3, b6 = 30,
            b7 = True, allowPOS=('ns', 'n')):
            b5.append({x: w})
        b8 = {
            '$set': {
                'jieba_text_rank': b5
            }
        }
        b2.update_one({'document_id': b4}, b8, b9 = True)
@click.command()
@click.option('--b2', '-c', b10 = click.Choice(collections), multiple=True)
def fonk2(b2):
    b11 = b2 if b2 else collections
    print(b11)
    if 'article-juejin' in b11:
        fonk1()