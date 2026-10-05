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
def read_word_counts(filename):
    with open(filename, "r") as file:
        return collections.Counter(file.read().split())
def write_special_words(filename, word_count):
    regex = re.compile("[^a-zA-Z]")
    with open(filename, "w") as file:
        for key, count in word_count.items():
            modified_key = regex.sub("", str(key))
            if modified_key not in WORDS_TO_REMOVE and count > 2:
                file.write(modified_key + "\n")
for dimension in DIMENSIONS:
    wordcount_a = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt"))
    wordcount_b = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt"))
    common_keys = set(wordcount_a) | set(wordcount_b)
    a = {}
    b = {}
    for key in common_keys:
        if key in wordcount_a and key not in wordcount_b:
            a[key] = wordcount_a[key]
        elif key in wordcount_b and key not in wordcount_a:
            b[key] = wordcount_b[key]
        elif key in wordcount_a and key in wordcount_b:
            diff = abs(wordcount_a[key] - wordcount_b[key])
            if diff > 0:
                a[key] = diff
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), a)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), b)