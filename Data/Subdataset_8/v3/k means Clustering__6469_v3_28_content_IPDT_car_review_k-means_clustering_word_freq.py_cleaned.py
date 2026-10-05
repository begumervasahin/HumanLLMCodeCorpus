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
    punctuation_pattern = r'[,\ï¼ã.!?:"@]'
    sentence = re.sub(punctuation_pattern, '', sentence)
    return sentence.split()
def calculate_word_frequency(sents_list):
    word_freq = {}
    for sentence in sents_list:
        phrase_to_remove = "(Read more about how we rate cars.)"
        if phrase_to_remove in sentence:
            sentence = sentence.replace(phrase_to_remove, "")
        for word in clean_and_split_sentence(sentence):
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq
def write_word_frequencies_to_file(word_freq, filepath):
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        for index, (word, frequency) in enumerate(sorted_word_freq, start=1):
            file.write(f"{index} : {word} : {frequency}\n")
def calculate_and_write_en_word_frequency():
    sql_query = "SELECT data FROM RAW_DATA"
    fetched_data = fetch_data_from_db(sql_query)
    sentences_list = [row[0] for row in fetched_data]
    word_frequency = calculate_word_frequency(sentences_list)
    write_word_frequencies_to_file(word_frequency, './word_freq_en_v2.txt')
def cn_freq_placeholder():
    pass
if __name__ == '__main__':
    calculate_and_write_en_word_frequency()
