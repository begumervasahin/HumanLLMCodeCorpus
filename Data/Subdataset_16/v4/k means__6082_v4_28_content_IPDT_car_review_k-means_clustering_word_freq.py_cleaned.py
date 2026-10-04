import pymysql
import re
from wordfreqcount import get_words
b1 = {
    'b2': 'localhost',
    'b3': 'I339493',
    'b4': 'test123',
    'b5': 'ml_features_en'
}
def fonk1(config):
    return pymysql.connect(
        b2 = config['b2'],
        b3 = config['b3'],
        b4 = config['b4'],
        b5 = config['b5']
    )
def fonk2(b13):
    b6 = {}
    b7 = set()
    for b8 in b13:
        b8 = str(b8)
        if "(Read more about how we rate cars.)" in b8:
            b8 = b8.replace("(Read more about how we rate cars.)", "")
        b8 = b8.lower()
        b9 = r'[,ï¼ã.!?:"@]'
        b8 = re.sub(b9, '', b8)
        for word in b8.split():
            if word in b7:
                b6[word] += 1
            else:
                b6[word] = 1
                b7.add(word)
    return b6
def fonk3():
    b10 = fonk1(b1)
    b11 = b10.b11()
    b11.execute("SELECT data FROM RAW_DATA")
    b12 = b11.fetchall()
    b11.close()
    b10.close()
    b13 = [result[0] for result in b12]
    b6 = fonk2(b13)
    b14 = sorted(b6.items(), key=lambda x: x[1], reverse=True)
    with open('./word_freq_en_v2.txt', 'w') as f:
        for index, (word, freq) in enumerate(b14, b15 = 1):
            f.write(f"{index} : {word} : {freq}\n")
def fonk4():
    b10 = fonk1(b1)
    b11 = b10.b11()
    b11.execute("SELECT translate FROM RAW_DATA")
    b12 = b11.fetchall()
    with open('./cn_translations.txt', 'w') as f:
        for index, (translation,) in enumerate(b12, b15 = 1):
            if index % b16 = = 0:
                print(index)
            f.write(translation + '\n')
    b11.close()
    b10.close()
if b17 = = '__main__':
    fonk3()
    with open('./cn_translations.txt', 'r', b18 = 'utf8') as f:
        b19 = get_words(f.read())
    with open('./word_freq_cn_v1.txt', 'w') as f:
        for word in b19:
            f.write(word + '\n')