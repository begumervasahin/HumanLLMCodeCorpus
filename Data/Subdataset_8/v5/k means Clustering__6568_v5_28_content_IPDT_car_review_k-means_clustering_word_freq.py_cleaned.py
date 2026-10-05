import pymysql
import re
from wordfreqcount import get_words
DB_HOST = 'localhost'
DB_USER = 'I339493'
DB_PASSWORD = 'test123'
DB_NAME = 'ml_features_en'
EN_FREQ_FILE_PATH = './word_freq_en_v2.txt'
CN_TRANSLATIONS_FILE_PATH = './cn_translations.txt'
WORD_FREQ_CN_FILE_PATH = './word_freq_cn_v1.txt'
PUNCTUATION_PATTERN = '[,ï¼ã.!?:"@'
REMOVE_PHRASE = "(Read more about how we rate cars.)"
def remove_unwanted_text(sentence: str) -> str:
    if REMOVE_PHRASE in sentence:
        sentence = sentence.replace(REMOVE_PHRASE, "")
    sentence = sentence.lower()
    return re.sub(PUNCTUATION_PATTERN, '', sentence)
def calculate_word_frequency(sents_list: list) -> dict:
    word_freq = {}
    for sentence in sents_list:
        sentence = remove_unwanted_text(str(sentence))
        for word in sentence.split():
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq
def fetch_data_and_process(sql_query: str, output_file: str, process_function):
    with pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
    processed_data = process_function(result)
    with open(output_file, 'w', encoding='utf8') as f:
        for data in processed_data:
            f.write(f"{data}\n")
def process_english_frequency():
    sql_query = "SELECT data FROM RAW_DATA"
    def process_function(results):
        word_freq_dict = calculate_word_frequency([x[0] for x in results])
        sorted_word_freq = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)
        return [f"{index + 1} : {key} : {value}" for index, (key, value) in enumerate(sorted_word_freq)]
    fetch_data_and_process(sql_query, EN_FREQ_FILE_PATH, process_function)
def process_chinese_frequency():
    with open(CN_TRANSLATIONS_FILE_PATH, 'r', encoding='utf8') as f:
        chinese_text = f.read()
    chinese_words = get_words(chinese_text)
    with open(WORD_FREQ_CN_FILE_PATH, 'w', encoding='utf8') as f:
        for word in chinese_words:
            f.write(f"{word}\n")
def main():
    process_english_frequency()
    process_chinese_frequency()
if __name__ == '__main__':
    main()