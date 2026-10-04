import re
import random
import numpy as np
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
CLASS1_FILE = "raw_data_sport.txt"
CLASS2_FILE = "raw_data_politics.txt"
important_words_class1 = {}
important_words_class2 = {}
def random_partitioner(text, percent):
    words = text.split()
    partition_length = len(words)
    second_partition_length = int(partition_length * percent)
    second_partition = []
    for _ in range(second_partition_length):
        r = random.randint(0, partition_length - 1)
        second_partition.append(words[r])
        del words[r]
        partition_length -= 1
    first_partition = ' '.join(words)
    second_partition = ' '.join(second_partition)
    return first_partition, second_partition
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.replace("\n", " ")
    text = text.replace("-", "")
    stop_words = set(stopwords.words('english'))
    stop_words.add("subject")
    for word in stop_words:
        text = text.replace(" " + word + " ", " ")
    return text
def normal_pdf(x, mean, std_dev):
    return (1 / (2 * np.pi * std_dev**2)**0.5) * np.exp(-1 * (x - mean)**2 / (2 * std_dev**2))
def calculate_probability(text, pclass1, pclass2, count_all_word1, count_all_word2, count_dist_words1, count_dist_words2, class1_words, class2_words):
    text = clean_text(text)
    words = re.split(r"[,\n :?\"â]+", text)
    p_word_in_class1 = pclass1
    p_word_in_class2 = pclass2
    pmax1 = 0
    pmax2 = 0
    imp_word1 = ""
    imp_word2 = ""
    for word in words:
        if len(word) < 3:
            continue
        p = normal_pdf(word, count_all_word1, count_dist_words1, class1_words)
        if p > pmax1:
            pmax1 = p
            imp_word1 = word
        p = normal_pdf(word, count_all_word2, count_dist_words2, class2_words)
        if p > pmax2:
            pmax2 = p
            imp_word2 = word
        p_word_in_class1 += normal_pdf(word, count_all_word1, count_dist_words1, class1_words)
        p_word_in_class2 += normal_pdf(word, count_all_word2, count_dist_words2, class2_words)
    if p_word_in_class1 > p_word_in_class2:
        important_words_class1[imp_word1] = pmax1
        return 1
    else:
        important_words_class2[imp_word2] = pmax2
        return 2
def count_words(train1, train2):
    words1 = re.split(r"[,\n.:?\"â]+", train1)
    words2 = re.split(r"[,\n.:?\"â]+", train2)
    counter1 = OrderedDict(Counter(words1))
    counter2 = OrderedDict(Counter(words2))
    return counter1, counter2
def stringify_every_50_words(arr):
    length = len(arr)
    result = [' '.join(arr[i*50:(i+1)*50]) for i in range(length)]
    if len(arr) % 50:
        result.append(' '.join(arr[length*50:]))
    return result
def classifier():
    with open(CLASS1_FILE, 'r', encoding="utf-8") as f:
        class1 = clean_text(f.read())
    with open(CLASS2_FILE, 'r', encoding="utf-8") as f:
        class2 = clean_text(f.read())
    train1, test1 = random_partitioner(class1, 0.10)
    train2, test2 = random_partitioner(class2, 0.10)
    count_sentence1 = sum(Counter(re.split(r"[.\n\r?!:]+", train1)).values())
    count_sentence2 = sum(Counter(re.split(r"[.\n\r?!:]+", train2)).values())
    class1_words, class2_words = count_words(train1, train2)
    count_all_word1 = sum(class1_words.values())
    count_all_word2 = sum(class2_words.values())
    count_dist_words1 = len(class1_words.keys())
    count_dist_words2 = len(class2_words.keys())
    pclass1 = count_sentence1 / (count_sentence1 + count_sentence2)
    pclass2 = count_sentence2 / (count_sentence1 + count_sentence2)
    test_sentences1 = stringify_every_50_words(re.split(r"[.\n\r?!: ]+", test1))
    test_sentences2 = stringify_every_50_words(re.split(r"[.\n\r?!: ]+", test2))
    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for sentence in test_sentences1:
        c = calculate_probability(sentence, pclass1, pclass2, count_all_word1, count_all_word2, count_dist_words1, count_dist_words2, class1_words, class2_words)
        if c == 1:
            tp += 1
        else:
            fn += 1
    for sentence in test_sentences2:
        c = calculate_probability(sentence, pclass1, pclass2, count_all_word1, count_all_word2, count_dist_words1, count_dist_words2, class1_words, class2_words)
        if c == 2:
            tn += 1
        else:
            fp += 1
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    print("False Positives:", fp)
    print("True Positives:", tp)
    print("False Negatives:", fn)
    print("True Negatives:", tn)
    print("Precision:", precision)
    print("Recall:", recall)
    print("Important words in class 1 (sports):", OrderedDict(important_words_class1))
    print("Important words in class 2 (politics):", OrderedDict(important_words_class2))
if __name__ == "__main__":
    classifier()