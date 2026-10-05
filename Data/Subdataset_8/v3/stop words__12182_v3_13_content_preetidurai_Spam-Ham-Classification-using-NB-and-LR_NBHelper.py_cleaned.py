import os
import re
WORD_REGEX = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
def extract_words(text):
    return WORD_REGEX.findall(text.lower())
def extract_words_without_stopwords(text, stop_words):
    words = extract_words(text)
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words
def create_mail_dictionary(directory_path):
    messages = {}
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
            messages[file_name] = extract_words(mail_file.read())
    return messages
def create_mail_dictionary_without_stopwords(directory_path, stop_words):
    messages = {}
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
            messages[file_name] = extract_words_without_stopwords(mail_file.read(), stop_words)
    return messages
def read_stop_words(file_path):
    with open(file_path, encoding='utf-8', errors="ignore") as stop_file:
        stop_words = extract_words(stop_file.read())
        return stop_words
def create_vocabulary(mail_dict):
    vocabulary = set()
    for message in mail_dict.values():
        vocabulary.update(message)
    return list(vocabulary)
STOP_WORDS_PATH = "stopwords.txt"
MAIL_DIRECTORY_PATH = "mails"
stop_words = read_stop_words(STOP_WORDS_PATH)
mail_dict_with_stopwords = create_mail_dictionary(MAIL_DIRECTORY_PATH)
mail_dict_without_stopwords = create_mail_dictionary_without_stopwords(MAIL_DIRECTORY_PATH, stop_words)
vocabulary = create_vocabulary(mail_dict_with_stopwords)
print("Stop words:", stop_words)
print("\nMail dictionary with stop words:", mail_dict_with_stopwords)
print("\nMail dictionary without stop words:", mail_dict_without_stopwords)
print("\nVocabulary:", vocabulary)