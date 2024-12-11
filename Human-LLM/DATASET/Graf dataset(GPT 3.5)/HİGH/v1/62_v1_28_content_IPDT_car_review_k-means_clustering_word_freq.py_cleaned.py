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
def fonk4(b10):
    b6 = {}
    for b4 in b10:
        if "(Read more about how we rate cars.)" in b4:
            b4 = b4.replace("(Read more about how we rate cars.)", "")
        for word in fonk3(b4):
            if word not in b6:
                b6[word] = 0
            b6[word] += 1
    return b6
def fonk5(b6, filepath):
    b7 = sorted(b6.items(), key=lambda x: x[1], reverse=True)
    with open(filepath, 'w', b8 = 'utf-8') as f:
        for index, (key, value) in enumerate(b7, 1):
            f.write(f"{index} : {key} : {value}\n")
def fonk6():
    b9 = "SELECT data FROM RAW_DATA"
    b3 = fonk2(b9)
    b10 = [row[0] for row in b3]
    b6 = fonk4(b10)
    fonk5(b6, './word_freq_en_v2.txt')
def fonk7():
    pass
if b11 = = '__main__':
    fonk6()
