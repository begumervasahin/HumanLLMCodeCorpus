import pymysql
import re
from wordfreqcount import get_words
db_config = {
    'host': 'localhost',
    'user': 'I339493',
    'password': 'test123',
    'db': 'ml_features_en'
}
def get_db_connection(config):
    return pymysql.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        db=config['db']
    )
def word_freq(sentences):
    word_freq_dict = {}
    encountered_words = set()
    for sentence in sentences:
        sentence = str(sentence)
        if "(Read more about how we rate cars.)" in sentence:
            sentence = sentence.replace("(Read more about how we rate cars.)", "")
        sentence = sentence.lower()
        punctuation = r'[,ï¼ã.!?:"@]'
        sentence = re.sub(punctuation, '', sentence)
        for word in sentence.split():
            if word in encountered_words:
                word_freq_dict[word] += 1
            else:
                word_freq_dict[word] = 1
                encountered_words.add(word)
    return word_freq_dict
def en_freq():
    conn = get_db_connection(db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM RAW_DATA")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    sentences = [result[0] for result in results]
    word_freq_dict = word_freq(sentences)
    sorted_word_freq = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)
    with open('./word_freq_en_v2.txt', 'w') as f:
        for index, (word, freq) in enumerate(sorted_word_freq, start=1):
            f.write(f"{index} : {word} : {freq}\n")
def cn_freq():
    conn = get_db_connection(db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT translate FROM RAW_DATA")
    results = cursor.fetchall()
    with open('./cn_translations.txt', 'w') as f:
        for index, (translation,) in enumerate(results, start=1):
            if index % 10000 == 0:
                print(index)
            f.write(translation + '\n')
    cursor.close()
    conn.close()
if __name__ == '__main__':
    en_freq()
    with open('./cn_translations.txt', 'r', encoding='utf8') as f:
        word_list = get_words(f.read())
    with open('./word_freq_cn_v1.txt', 'w') as f:
        for word in word_list:
            f.write(word + '\n')