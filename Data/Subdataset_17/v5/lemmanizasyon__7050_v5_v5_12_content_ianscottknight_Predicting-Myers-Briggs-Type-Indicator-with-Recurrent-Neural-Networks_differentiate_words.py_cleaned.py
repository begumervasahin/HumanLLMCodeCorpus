import os
import collections
import re
DATA_DIR = "data"
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
WORDS_TO_REMOVE = set([
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx",
    "sj", "sf", "st", "le", "socionic", "socionics", "enneagram",
    "d", "w", "mbti"
])
def read_word_counts(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def write_special_words(file_path, word_dict, regex):
    with open(file_path, "w") as file:
        for word, count in word_dict.items():
            cleaned_word = regex.sub("", word)
            if count > 2:
                file.write(f"{cleaned_word}\n" * count)
def process_word_counts(dimension):
    """
    Processes word counts for each dimension, calculates differences, and writes special words to output files.
    :param dimension: A string representing a dimension (e.g., "IE").
    """
    word_counts_a = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt"))
    word_counts_b = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt"))
    all_words = set(word_counts_a.keys()) | set(word_counts_b.keys())
    special_words_a = {}
    special_words_b = {}
    regex = re.compile("[^a-zA-Z]")
    for word in all_words:
        if word not in WORDS_TO_REMOVE:
            count_a = word_counts_a.get(word, 0)
            count_b = word_counts_b.get(word, 0)
            diff = count_a - count_b
            if diff > 0:
                special_words_a[word] = diff
            elif diff < 0:
                special_words_b[word] = -diff
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), special_words_a, regex)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), special_words_b, regex)
for dimension in DIMENSIONS:
    process_word_counts(dimension)