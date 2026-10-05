import pymysql
import re
def connect_to_database():
    return pymysql.connect(host='localhost', user='I339493', password='test123', db='ml_features_en')
def fetch_data_from_db(query):
    try:
        conn = connect_to_database()
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    finally:
        conn.close()
def clean_and_split_sentence(sentence):
    sentence = sentence.lower()
    punctuation = r'[,\ï¼ã.!?:"@]'
    sentence = re.sub(punctuation, '', sentence)
    return sentence.split()
def calculate_word_frequency(sents_list):
    word_freq = {}
    for sentence in sents_list:
        if "(Read more about how we rate cars.)" in sentence:
            sentence = sentence.replace("(Read more about how we rate cars.)", "")
        for word in clean_and_split_sentence(sentence):
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1
    return word_freq
def write_word_frequencies_to_file(word_freq, filepath):
    word_freq_sort = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        for index, (key, value) in enumerate(word_freq_sort, 1):
            f.write(f"{index} : {key} : {value}\n")
def en_freq():
    sql = "SELECT data FROM RAW_DATA"
    result = fetch_data_from_db(sql)
    sents_list = [row[0] for row in result]
    word_freq = calculate_word_frequency(sents_list)
    write_word_frequencies_to_file(word_freq, './word_freq_en_v2.txt')
def cn_freq_placeholder():
    pass
if __name__ == '__main__':
    en_freq()
