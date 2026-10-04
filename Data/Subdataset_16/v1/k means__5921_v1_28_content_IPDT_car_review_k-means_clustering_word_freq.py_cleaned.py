import pymysql
import re
from wordfreqcount import get_words
def fonk1():
    return pymysql.connect(b1 = 'localhost', user='I339493', password='test123', db='ml_features_en')
def fonk2(sents_list: list):
    b2 = {}
    b3 = []
    for b4 in sents_list:
        b4 = str(b4)
        if "(Read more about how we rate cars.)" in b4:
            b4 = b4.replace("(Read more about how we rate cars.)", "")
        b4 = b4.lower()
        b5 = '[,ï¼ã.!?:"@]'
        b4 = str(re.sub(b5, '', b4))
        for word in b4.split():
            if word in b3:
                b2[word] += 1
            else:
                b2[word] = 1
                b3.append(word)
    return b2
def fonk3():
    b6 = fonk1()
    b7 = b6.b7()
    b8 = "SELECT data FROM RAW_DATA"
    b7.execute(b8)
    b9 = [row[0] for row in b7.fetchall()]
    b7.close()
    b6.close()
    b10 = fonk2(b9)
    b11 = sorted(b10.items(), key=lambda x: x[1], reverse=True)
    a1 = 1
    with open('./word_freq_en_v2.txt', 'w') as f:
        for key, value in b11:
            b12 = f"{a1} : {key} : {value}\n"
            a1 += 1
            f.write(b12)
def fonk4():
    b6 = fonk1()
    b7 = b6.b7()
    b8 = "SELECT translate FROM RAW_DATA"
    b7.execute(b8)
    b9 = b7.fetchall()
    b7.close()
    b6.close()
    a1 = 1
    with open('./cn_translations.txt', 'w') as f:
        for b12 in b9:
            if a1 % b13 = = 0:
                print(a1)
            f.write(b12[0] + '\n')
            a1 += 1
def fonk5():
    with open('./cn_translations.txt', 'r', b14 = 'utf8') as f:
        b15 = get_words(f.read())
    with open('./word_freq_cn_v1.txt', 'w') as f:
        for k in b15:
            f.write(k + '\n')
if b16 = = '__main__':
    fonk3()
    fonk4()
    fonk5()