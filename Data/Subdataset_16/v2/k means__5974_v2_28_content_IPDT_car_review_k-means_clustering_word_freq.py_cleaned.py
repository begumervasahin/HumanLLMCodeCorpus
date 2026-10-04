import pymysql
import re
from wordfreqcount import get_words
def fonk1():
    return pymysql.connect(
        b1 = 'localhost',
        b2 = 'I339493',
        b3 = 'test123',
        b4 = 'ml_features_en'
    )
def fonk2(sents_list):
    b5 = {}
    b6 = set()
    for b7 in sents_list:
        b7 = str(b7)
        if "(Read more about how we rate cars.)" in b7:
            b7 = b7.replace("(Read more about how we rate cars.)", "")
        b7 = b7.lower()
        b8 = '[,ï¼ã.!?:"@]'
        b7 = re.sub(b8, '', b7)
        for word in b7.split():
            if word in b6:
                b5[word] += 1
            else:
                b5[word] = 1
                b6.add(word)
    return b5
def fonk3():
    b9 = fonk1()
    b10 = b9.b10()
    b11 = "SELECT data FROM RAW_DATA"
    b10.execute(b11)
    b12 = [row[0] for row in b10.fetchall()]
    b10.close()
    b9.close()
    b13 = fonk2(b12)
    b14 = sorted(b13.items(), key=lambda x: x[1], reverse=True)
    with open('./word_freq_en_v2.txt', 'w') as f:
        for index, (key, value) in enumerate(b14, b15 = 1):
            f.write(f"{index} : {key} : {value}\n")
def fonk4():
    b9 = fonk1()
    b10 = b9.b10()
    b11 = "SELECT translate FROM RAW_DATA"
    b10.execute(b11)
    b12 = b10.fetchall()
    b10.close()
    b9.close()
    with open('./cn_translations.txt', 'w') as f:
        for index, line in enumerate(b12, b15 = 1):
            if index % b16 = = 0:
                print(index)
            f.write(line[0] + '\n')
def fonk5():
    with open('./cn_translations.txt', 'r', b17 = 'utf8') as f:
        b18 = get_words(f.read())
    with open('./word_freq_cn_v1.txt', 'w') as f:
        for k in b18:
            f.write(k + '\n')
if b19 = = '__main__':
    fonk3()
    fonk4()
    fonk5()