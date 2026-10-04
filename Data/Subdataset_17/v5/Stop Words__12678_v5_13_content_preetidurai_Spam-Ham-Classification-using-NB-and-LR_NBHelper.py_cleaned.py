import os
import re
WORD_REGEX = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def get_words(text):
    return WORD_REGEX.findall(text.lower())
def get_words_without_stopwords(text, stop_words):
    words = get_words(text)
    return [word for word in words if word not in stop_words]
def get_mail_dictionary(path):
    messages = {}
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, encoding='utf-8', errors='ignore') as mail_file:
                messages[file] = get_words(mail_file.read())
    return messages
def get_mail_dictionary_without_stopwords(path, stop_words):
    messages = {}
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, encoding='utf-8', errors='ignore') as mail_file:
                messages[file] = get_words_without_stopwords(mail_file.read(), stop_words)
    return messages
def read_stop_words(path):
    with open(path, encoding='utf-8', errors='ignore') as stop_file:
        return get_words(stop_file.read())
def get_vocabulary(mail_dict):
    vocab = []
    for words in mail_dict.values():
        vocab.extend(words)
    return vocab