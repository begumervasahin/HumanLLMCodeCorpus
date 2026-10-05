import os
import re
word_regex = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
def get_words(text):
    return list(word_regex.findall(text.lower()))
def get_words_sans_stopwords(text, stop_words):
    words = list(word_regex.findall(text.lower()))
    new_word_list = [word for word in words if word not in stop_words]
    return new_word_list
def get_mail_dictionary(path):
    messages = {}
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
            messages[file] = get_words(mail_file.read())
    return messages
def get_mail_dictionary_without_stopwords(path, stop_words):
    messages = {}
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
            messages[file] = get_words_sans_stopwords(mail_file.read(), stop_words)
    return messages
def read_stop_words(path):
    with open(path, encoding='utf-8', errors="ignore") as stop_file:
        stop_words = get_words(stop_file.read())
        return stop_words
def get_vocabulary(mail_dict):
    vocab = []
    for key, value in mail_dict.items():
        vocab.extend(value)
    return vocab