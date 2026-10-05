import os
import numpy as np
from collections import Counter
NUM_WORDS_IN_DICT = 3000
TRAIN_DIR = 'train-mails'
TEST_DIR = 'test-mails'
def make_dictionary(train_dir):
    all_words = []
    for filename in os.listdir(train_dir):
        filepath = os.path.join(train_dir, filename)
        with open(filepath) as file:
            for i, line in enumerate(file):
                if i == 2:
                    words = line.split()
                    all_words.extend(words)
    word_counts = Counter(all_words)
    for word in list(word_counts):
        if not word.isalpha() or len(word) == 1:
            del word_counts[word]
    dictionary = word_counts.most_common(NUM_WORDS_IN_DICT)
    return dictionary
def extract_features(mail_dir, dictionary):
    features_matrix = np.zeros((len(os.listdir(mail_dir)), NUM_WORDS_IN_DICT))
    for doc_id, filename in enumerate(os.listdir(mail_dir)):
        filepath = os.path.join(mail_dir, filename)
        with open(filepath) as file:
            for i, line in enumerate(file):
                if i == 2:
                    words = line.split()
                    for word in words:
                        for idx, entry in enumerate(dictionary):
                            if entry[0] == word:
                                features_matrix[doc_id, idx] = words.count(word)
    return features_matrix
def get_filenames(mail_dir):
    filenames = [os.path.splitext(filename)[0] for filename in os.listdir(mail_dir)]
    return filenames
dictionary = make_dictionary(TRAIN_DIR)
train_matrix = extract_features(TRAIN_DIR, dictionary)
test_matrix = extract_features(TEST_DIR, dictionary)
with open('./training_matrix.arff', 'w') as filetraining:
    filetraining.write("% 1. Title: Spam Dataset training\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for idx, entry in enumerate(dictionary):
        attribute_name = "@ATTRIBUTE class_" if entry[0] == "class" else "@ATTRIBUTE " + entry[0]
        filetraining.write(attribute_name + " NUMERIC\n")
    filetraining.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    filename_list = get_filenames(TRAIN_DIR)
    for idx, row in enumerate(train_matrix):
        for n in row:
            filetraining.write(str(n) + ",")
        filetraining.write("spam\n" if filename_list[idx][:1] == 's' else "not-spam\n")
with open('./test_matrix.arff', 'w') as filetest:
    filetest.write("% 1. Title: Spam Dataset test\n%\n% 2. Sources: Hasil Feature Matrix\n%\n@RELATION spam\n")
    for idx, entry in enumerate(dictionary):
        attribute_name = "@ATTRIBUTE class_" if entry[0] == "class" else "@ATTRIBUTE " + entry[0]
        filetest.write(attribute_name + " NUMERIC\n")
    filetest.write("@ATTRIBUTE class {spam, not-spam}\n@DATA\n")
    filename_list = get_filenames(TEST_DIR)
    for idx, row in enumerate(test_matrix):
        for n in row:
            filetest.write(str(n) + ",")
        filetest.write("spam\n" if filename_list[idx][:1] == 's' else "not-spam\n")