import pymysql
import re
from wordfreqcount import get_words
b1 = pymysql.connect(host='localhost', user='I339493', password='test123', db='ml_features_en')
b2 = b1.b2()
def fonk1(sents_list: list):
    b3 = {}
    b4 = []
    for b5 in sents_list:
        b5 = str(b5)
        if "(Read more about how we rate cars.)" in b5:
            b5 = b5.replace("(Read more about how we rate cars.)", "")
        b5 = b5.lower()
        b6 = '[,ï¼ã.!?:"@
        b5 = str(re.sub(b6, '', b5))
        for word in b5.split(" "):
            if word in b4:
                b3[word] += 1
            else:
                b3[word] = 1
                b4.append(word)
    return b3
def fonk2():
    b7 = "select data from RAW_DATA"
    b2.execute(b7)
    b8 = list(b2.fetchall())
    b2.close()
    b1.close()
    b9 = fonk1(b8)
    b10 = sorted(b9.items(), key=lambda x: x[1], reverse=True)
    a1 = 1
    with open('./word_freq_en_v2.txt', 'w') as f:
        for (key, value) in b10:
            b11 = str(a1) + " : " + key + " : " + str(value) + "\n"
            a1 += 1
            f.write(b11)
def fonk3():
    b7 = "select translate from RAW_DATA"
    b2.execute(b7)
    b8 = b2.fetchall()
    a1 = 1
    with open('./cn_translations.txt', 'w') as f:
        for b11 in b8:
            if a1 % b12 = = 0:
                print(a1)
            f.write(b11[0] + '\n')
            a1 += 1
    b2.close()
    b1.close()
if b13 = = '__main__':
    with open('./cn_translations.txt', 'r', b14 = 'utf8') as f:
        b15 = get_words(f.read())
    with open('./word_freq_cn_v1.txt', 'w') as f:
        for k in b15:
            f.write(k + '\n')