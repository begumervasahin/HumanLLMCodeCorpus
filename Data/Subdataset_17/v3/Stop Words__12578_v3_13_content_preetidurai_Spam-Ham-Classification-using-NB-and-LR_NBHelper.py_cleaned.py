import os
import re
WORD_REGEX = re.compile(r"[a-zA-Z']+(?:-[a-zA-Z']+)?")
def extract_words(text):
    return list(WORD_REGEX.findall(text.lower()))
def extract_words_excluding_stop_words(text, stop_words):
    words = extract_words(text)
    return [word for word in words if word not in stop_words]
def create_mail_dictionary(directory):
    messages = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8', errors='ignore') as mail_file:
                messages[file] = extract_words(mail_file.read())
    return messages
def create_mail_dictionary_without_stop_words(directory, stop_words):
    messages = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8', errors='ignore') as mail_file:
                messages[file] = extract_words_excluding_stop_words(mail_file.read(), stop_words)
    return messages
def load_stop_words(file_path):
    with open(file_path, encoding='utf-8', errors='ignore') as stop_file:
        return extract_words(stop_file.read())
def extract_vocabulary(mail_dict):
    vocab = []
    for words in mail_dict.values():
        vocab.extend(words)
    return vocab
if __name__ == "__main__":
    mail_dir = "path_to_mails"
    stop_words_file = "path_to_stopwords.txt"
    stop_words = load_stop_words(stop_words_file)
    mail_dict = create_mail_dictionary(mail_dir)
    mail_dict_without_stop_words = create_mail_dictionary_without_stop_words(mail_dir, stop_words)
    vocabulary = extract_vocabulary(mail_dict)
    vocabulary_without_stop_words = extract_vocabulary(mail_dict_without_stop_words)
    print("Mail Dictionary:", mail_dict)
    print("Mail Dictionary Without Stop Words:", mail_dict_without_stop_words)
    print("Vocabulary:", vocabulary)
    print("Vocabulary Without Stop Words:", vocabulary_without_stop_words)