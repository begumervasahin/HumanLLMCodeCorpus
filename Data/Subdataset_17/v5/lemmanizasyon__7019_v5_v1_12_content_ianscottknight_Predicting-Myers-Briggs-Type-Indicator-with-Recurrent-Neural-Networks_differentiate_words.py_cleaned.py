import os
import collections
import re
DATA_DIR = "data"
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
WORDS_TO_REMOVE = [
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx", "sj", "sf", "st",
    "le", "socionic", "socionics", "enneagram", "d", "w", "mbti",
]
NON_ALPHA_REGEX = re.compile("[^a-zA-Z]")
def count_words(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def calculate_word_differences(wordcount_a, wordcount_b):
    all_words = set(wordcount_a.keys()).union(set(wordcount_b.keys()))
    unique_words_a = {}
    unique_words_b = {}
    for word in all_words:
        if word in wordcount_a and word not in wordcount_b:
            unique_words_a[word] = wordcount_a[word]
        elif word in wordcount_b and word not in wordcount_a:
            unique_words_b[word] = wordcount_b[word]
        elif word in wordcount_a and word in wordcount_b:
            difference = wordcount_a[word] - wordcount_b[word]
            if difference > 0:
                unique_words_a[word] = difference
            elif difference < 0:
                unique_words_b[word] = -difference
    return unique_words_a, unique_words_b
def write_special_words(filename, word_dict):
    with open(os.path.join(DATA_DIR, filename), "w") as file:
        for word, count in word_dict.items():
            cleaned_word = NON_ALPHA_REGEX.sub("", word)
            if cleaned_word not in WORDS_TO_REMOVE and count > 2:
                file.write(cleaned_word + "\n")
for dimension in DIMENSIONS:
    file_path_a = os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt")
    file_path_b = os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt")
    wordcount_a = count_words(file_path_a)
    wordcount_b = count_words(file_path_b)
    unique_words_a, unique_words_b = calculate_word_differences(wordcount_a, wordcount_b)
    write_special_words(f"special_words_{dimension[0]}.txt", unique_words_a)
    write_special_words(f"special_words_{dimension[1]}.txt", unique_words_b)