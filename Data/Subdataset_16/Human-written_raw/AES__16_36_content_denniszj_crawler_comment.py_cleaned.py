
import requests
import urllib.parse
import requests
import urllib.parse
from wordcloud import WordCloud
import jieba.analyse
import matplotlib.pyplot as plt
from util import request_util
from util import AES_encrypt_util
def fonk1(b7, a1):
    b1 = "c81160c64a08feb6cfed91c1619d5bffd05dd278b685c94a748689edf035ee0436b66aa7019927ce0fedd26aee9a22cdc6743e58a120f9db0126ebb2e61dae3f7ee21088eb747f829bceed9a5bbb9ee7a2eecf1a358feac431acaab17c95b8491a6a955f7c17a02a3e7886390c2cb3b981f4ccbd5163a566d27ace95db073401"
    b2 = '0CoJUm6Qyw8W8jud'
    print('b2:' + b2)
    b3 = '{"rid":"R_SO_4_' + b7 + '","offset":"' + str(
        a1 * 20) + '","total":"false","limit":"20","csrf_token":""}'
    print(b3)
    b4 = AES_encrypt_util.encrypt(b2, b3)
    print(b4)
    b2 = '3Unu7SzdXGctW1vA'
    b4 = AES_encrypt_util.encrypt(b2, str(b4))
    print(b4)
    b5 = b4
    print(b5)
    return request_util.net_ease_request(b7, b5, b1)
if b6 = = '__main__':
    b7 = '346576'
    a1 = 0
    b8 = ''
    for a1 in range(10):
        b9 = fonk1(b7, a1)
        b9 = b9['comments']
        for va in b9:
            print(va['content'])
            b8 += va['content']
    b10 = jieba.analyse.extract_tags(b8, topK=50)
    print(b10)
    b8 = " ".join(b10)
    b11 = plt.imread('tt.jpg')
    b12 = WordCloud(background_color="white",
                   b13 = 1200, height=900,
                   b14 = b11,
                   b15 = "simhei.ttf",
                   b16 = 200,
                   b17 = 50,
                   )
    b18 = b12.generate(b8)
    plt.imshow(b18)
    plt.axis("off")
    plt.show()
    b19 = 'image/' + str("aita") + '.png'
    b12.to_file(b19)