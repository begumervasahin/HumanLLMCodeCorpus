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
NON_ALPHABET_REGEX = re.compile("[^a-zA-Z]")
def read_word_counts(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def filter_and_diff_word_counts(wordcount_a, wordcount_b):
    filtered_wordcount_a = {}
    filtered_wordcount_b = {}
    combined_keys = set(wordcount_a.keys()) | set(wordcount_b.keys())
    for key in combined_keys:
        if key not in WORDS_TO_REMOVE:
            count_a = wordcount_a.get(key, 0)
            count_b = wordcount_b.get(key, 0)
            difference = count_a - count_b
            if difference > 0:
                filtered_wordcount_a[key] = difference
            elif difference < 0:
                filtered_wordcount_b[key] = -difference
    return filtered_wordcount_a, filtered_wordcount_b
def write_filtered_words(filename, word_counts):
    with open(filename, "w") as output_file:
        for word, count in word_counts.items():
            cleaned_word = NON_ALPHABET_REGEX.sub("", word)
            if count > 2:
                output_file.write((cleaned_word + "\n") * count)
def process_dimension_pair(dimension):
    wordcount_a = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt"))
    wordcount_b = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt"))
    filtered_wordcount_a, filtered_wordcount_b = filter_and_diff_word_counts(wordcount_a, wordcount_b)
    write_filtered_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), filtered_wordcount_a)
    write_filtered_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), filtered_wordcount_b)
for dimension in DIMENSIONS:
    process_dimension_pair(dimension)