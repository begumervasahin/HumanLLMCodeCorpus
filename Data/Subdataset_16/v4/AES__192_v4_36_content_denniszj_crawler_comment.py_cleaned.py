import requests
import urllib.parse
from b9 import WordCloud
import jieba.analyse
import matplotlib.pyplot as plt
from util import request_util, AES_encrypt_util
def fonk1(b16, page):
    b1 = (
        "c81160c64a08feb6cfed91c1619d5bffd05dd278b685c94a748689edf035ee0436b66aa7019927ce0fedd26aee9a22cdc6743e58a120f9db0126ebb2e61dae3f7ee21088eb747f829bceed9a5bbb9ee7a2eecf1a358feac431acaab17c95b8491a6a955f7c17a02a3e7886390c2cb3b981f4ccbd5163a566d27ace95db073401"
    )
    b2 = '0CoJUm6Qyw8W8jud'
    b3 = '3Unu7SzdXGctW1vA'
    b4 = (
        f'{{"rid":"R_SO_4_{b16}","offset":"{page * 20}","total":"false","limit":"20","csrf_token":""}}'
    )
    b5 = AES_encrypt_util.encrypt(b2, b4)
    print(f'Encrypted with initial key: {b5}')
    b5 = AES_encrypt_util.encrypt(b3, str(b5))
    print(f'Encrypted with final key: {b5}')
    return request_util.net_ease_request(b16, b5, b1)
def fonk2(text, background_image_path, output_image_path):
    b6 = jieba.analyse.extract_tags(text, topK=50)
    b7 = " ".join(b6)
    b8 = plt.imread(background_image_path)
    b9 = WordCloud(
        b10 = "white",
        b11 = 1200, height=900,
        b12 = b8,
        b13 = "simhei.ttf",
        b14 = 200,
        a1 = 50
    ).generate(b7)
    plt.imshow(b9, b15 = 'bilinear')
    plt.axis("off")
    plt.show()
    b9.to_file(output_image_path)
def fonk3():
    b16 = '346576'
    a2 = 10
    b17 = ''
    for page in range(a2):
        b18 = fonk1(b16, page)
        b19 = b18.get('b19', [])
        for comment in b19:
            print(comment['content'])
            b17 += comment['content']
    fonk2(b17, 'tt.jpg', 'image/aita.png')
if b20 = = '__main__':
    fonk3()