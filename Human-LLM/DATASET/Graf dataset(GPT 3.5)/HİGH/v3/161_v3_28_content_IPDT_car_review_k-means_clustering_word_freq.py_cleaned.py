import pymysql
import re
def fonk1():
    return pymysql.connect(b1 = 'localhost', user='I339493', password='test123', db='ml_features_en')
def fonk2(query):
    try:
        b2 = fonk1()
        with b2.cursor() as cursor:
            cursor.execute(query)
            b3 = cursor.fetchall()
        return b3
    finally:
        b2.close()
def fonk3(b4):
    b4 = b4.lower()
    b5 = r'[,\ï¼ã.!?:"@]'
    b4 = re.sub(b5, '', b4)
    return b4.split()
def fonk4(sents_list):
    b6 = {}
    for b4 in sents_list:
        b7 = "(Read more about how we rate cars.)"
        if b7 in b4:
            b4 = b4.replace(b7, "")
        for word in fonk3(b4):
            b6[word] = b6.get(word, 0) + 1
    return b6
def fonk5(b6, filepath):
    b8 = sorted(b6.items(), key=lambda x: x[1], reverse=True)
    with open(filepath, 'w', b9 = 'utf-8') as file:
        for index, (word, frequency) in enumerate(b8, b10 = 1):
            file.write(f"{index} : {word} : {frequency}\n")
def fonk6():
    b11 = "SELECT data FROM RAW_DATA"
    b12 = fonk2(b11)
    b13 = [row[0] for row in b12]
    b14 = fonk4(b13)
    fonk5(b14, './word_freq_en_v2.txt')
def fonk7():
    pass
if b15 = = '__main__':
    fonk6()
