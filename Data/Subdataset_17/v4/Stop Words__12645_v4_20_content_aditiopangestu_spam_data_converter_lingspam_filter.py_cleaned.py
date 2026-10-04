
from __future__ import print_function
import os
import numpy as np
from collections import Counter
np.set_printoptions(threshold=np.inf)
NUMBER_WORDS_IN_DICT = 3000
TRAIN_DIR = 'train-mails'
TEST_DIR = 'test-mails'
def make_dictionary(mail_dir):
    emails = [os.path.join(mail_dir, f) for f in os.listdir(mail_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i, line in enumerate(m):
                if i == 2:
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    list_to_remove = list(dictionary.keys())
    for item in list_to_remove:
        if not item.isalpha() or len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(NUMBER_WORDS_IN_DICT)
    return dictionary
def extract_features(mail_dir, dictionary):
    files = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files), NUMBER_WORDS_IN_DICT))
    for doc_id, fil in enumerate(files):
        with open(fil) as fi:
            for i, line in enumerate(fi):
                if i == 2:
                    words = line.split()
                    for word in words:
                        for word_id, d in enumerate(dictionary):
                            if d[0] == word:
                                features_matrix[doc_id, word_id] = words.count(word)
    return features_matrix
def get_all_filenames(mail_dir):
    emails = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    filenames = [os.path.splitext(os.path.basename(mail))[0] for mail in emails]
    return filenames
def save_arff(file_path, relation, dictionary, matrix, filenames):
    with open(file_path, 'w') as file:
        file.write(f"% 1. Title: Spam Dataset {relation}\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
        for word, _ in dictionary:
            attribute = "class_" if word == "class" else word
            file.write(f"@ATTRIBUTE {attribute} NUMERIC\n")
        file.write("@ATTRIBUTE class {spam, not-spam}\n")
        file.write("@DATA\n")
        for i, features in enumerate(matrix):
            feature_str = ",".join(map(str, features))
            label = "spam" if filenames[i].startswith('s') else "not-spam"
            file.write(f"{feature_str},{label}\n")
dictionary = make_dictionary(TRAIN_DIR)
train_matrix = extract_features(TRAIN_DIR, dictionary)
test_matrix = extract_features(TEST_DIR, dictionary)
train_filenames = get_all_filenames(TRAIN_DIR)
test_filenames = get_all_filenames(TEST_DIR)
save_arff('./training_matrix.arff', 'training', dictionary, train_matrix, train_filenames)
save_arff('./test_matrix.arff', 'test', dictionary, test_matrix, test_filenames)