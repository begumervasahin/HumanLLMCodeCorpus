import os
import re
WORD_REGEX = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def get_words(text):
    return list(WORD_REGEX.findall(text.lower()))
def get_words_excluding_stop_words(text, stop_words):
    words = get_words(text)
    return [word for word in words if word not in stop_words]
def get_mail_dictionary(path):
    messages = {}
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for file in files:
        with open(os.path.join(path, file), encoding='utf-8', errors='ignore') as mail_file:
            messages[file] = get_words(mail_file.read())
    return messages
def get_mail_dictionary_without_stop_words(path, stop_words):
    messages = {}
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for file in files:
        with open(os.path.join(path, file), encoding='utf-8', errors='ignore') as mail_file:
            messages[file] = get_words_excluding_stop_words(mail_file.read(), stop_words)
    return messages
def read_stop_words(path):
    with open(path, encoding='utf-8', errors='ignore') as stop_file:
        return get_words(stop_file.read())
def get_vocabulary(mail_dict):
    vocab = []
    for words in mail_dict.values():
        vocab.extend(words)
    return vocab
if __name__ == "__main__":
    mail_dir = "path_to_mails"
    stop_words_file = "path_to_stopwords.txt"
    stop_words = read_stop_words(stop_words_file)
    mail_dict = get_mail_dictionary(mail_dir)
    mail_dict_without_stop_words = get_mail_dictionary_without_stop_words(mail_dir, stop_words)
    vocabulary = get_vocabulary(mail_dict)
    vocabulary_without_stop_words = get_vocabulary(mail_dict_without_stop_words)
    print("Mail Dictionary:", mail_dict)
    print("Mail Dictionary Without Stop Words:", mail_dict_without_stop_words)
    print("Vocabulary:", vocabulary)
    print("Vocabulary Without Stop Words:", vocabulary_without_stop_words)