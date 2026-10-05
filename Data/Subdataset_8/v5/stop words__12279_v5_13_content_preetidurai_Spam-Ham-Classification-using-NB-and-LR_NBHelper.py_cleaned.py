import os
import re
word_regex = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def extract_words(text):
    return word_regex.findall(text.lower())
def extract_words_without_stopwords(text, stop_words):
    words = extract_words(text)
    return [word for word in words if word not in stop_words]
def create_mail_dictionary(path):
    messages = {}
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
            messages[file_name] = extract_words(mail_file.read())
    return messages
def create_mail_dictionary_without_stopwords(path, stop_words):
    messages = {}
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
            messages[file_name] = extract_words_without_stopwords(mail_file.read(), stop_words)
    return messages
def read_stop_words(path):
    with open(path, encoding='utf-8', errors="ignore") as stop_file:
        return extract_words(stop_file.read())
def get_vocabulary(mail_dict):
    return [word for words in mail_dict.values() for word in words]