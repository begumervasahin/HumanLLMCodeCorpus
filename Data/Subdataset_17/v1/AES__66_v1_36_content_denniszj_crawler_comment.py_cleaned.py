import requests
import urllib.parse
from wordcloud import WordCloud
import jieba.analyse
import matplotlib.pyplot as plt
from util import request_util
from util import AES_encrypt_util
def get_comment(song_id, page):
    encSecKey = "c81160c64a08feb6cfed91c1619d5bffd05dd278b685c94a748689edf035ee0436b66aa7019927ce0fedd26aee9a22cdc6743e58a120f9db0126ebb2e61dae3f7ee21088eb747f829bceed9a5bbb9ee7a2eecf1a358feac431acaab17c95b8491a6a955f7c17a02a3e7886390c2cb3b981f4ccbd5163a566d27ace95db073401"
    aes_key_initial = '0CoJUm6Qyw8W8jud'
    aes_key_final = '3Unu7SzdXGctW1vA'
    source_en = f'{{"rid":"R_SO_4_{song_id}","offset":"{page * 20}","total":"false","limit":"20","csrf_token":""}}'
    encrypt_en = AES_encrypt_util.encrypt(aes_key_initial, source_en)
    encrypt_en = AES_encrypt_util.encrypt(aes_key_final, str(encrypt_en))
    params = encrypt_en
    return request_util.net_ease_request(song_id, params, encSecKey)
def generate_wordcloud(text, background_image_path, output_image_path):
    ags = jieba.analyse.extract_tags(text, topK=50)
    text = " ".join(ags)
    background_image = plt.imread(background_image_path)
    wc = WordCloud(
        background_color="white",
        width=1200, height=900,
        mask=background_image,
        font_path="simhei.ttf",
        max_font_size=200,
        random_state=50
    )
    my_wordcloud = wc.generate(text)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    wc.to_file(output_image_path)
if __name__ == '__main__':
    song_id = '346576'
    pages_to_fetch = 10
    text = ''
    for page in range(pages_to_fetch):
        comment_data = get_comment(song_id, page)
        comments = comment_data['comments']
        for comment in comments:
            print(comment['content'])
            text += comment['content']
    generate_wordcloud(text, 'tt.jpg', 'image/aita.png')