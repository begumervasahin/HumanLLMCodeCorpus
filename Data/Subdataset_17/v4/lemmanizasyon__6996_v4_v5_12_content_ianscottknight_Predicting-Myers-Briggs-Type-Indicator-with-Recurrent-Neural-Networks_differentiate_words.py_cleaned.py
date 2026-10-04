import os
import collections
import re
DATA_DIR = "data"
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
WORDS_TO_REMOVE = [
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx",
    "sj", "sf", "st", "le", "socionic", "socionics", "enneagram",
    "d", "w", "mbti",
]
def read_word_counts(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def write_special_words(file_path, word_dict, regex):
    with open(file_path, "w") as file:
        for word, count in word_dict.items():
            cleaned_word = regex.sub("", word)
            if count > 2:
                file.write(f"{cleaned_word}\n" * count)
def process_dimension_files(dimension):
    """
    Processes word counts for each dimension, calculates differences, and writes special words to output files.
    :param dimension: A string representing a dimension (e.g., "IE").
    """
    wordcount_a = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt"))
    wordcount_b = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt"))
    common_keys = set(wordcount_a.keys()) | set(wordcount_b.keys())
    special_words_a = {}
    special_words_b = {}
    regex = re.compile("[^a-zA-Z]")
    for word in common_keys:
        if word in wordcount_a and word not in WORDS_TO_REMOVE:
            if word in wordcount_b:
                diff = wordcount_a[word] - wordcount_b[word]
                if diff > 0:
                    special_words_a[word] = diff
                elif diff < 0:
                    special_words_b[word] = -diff
            else:
                special_words_a[word] = wordcount_a[word]
        elif word in wordcount_b and word not in WORDS_TO_REMOVE:
            special_words_b[word] = wordcount_b[word]
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), special_words_a, regex)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), special_words_b, regex)
for dimension in DIMENSIONS:
    process_dimension_files(dimension)