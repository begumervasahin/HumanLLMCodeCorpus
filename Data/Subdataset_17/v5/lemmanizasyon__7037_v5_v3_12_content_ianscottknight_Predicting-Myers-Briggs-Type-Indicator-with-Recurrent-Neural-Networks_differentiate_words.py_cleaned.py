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
def read_word_counts(filepath):
    with open(filepath, "r") as file:
        return collections.Counter(file.read().split())
def write_special_words(filepath, word_count):
    regex = re.compile("[^a-zA-Z]")
    with open(filepath, "w") as file:
        for word, count in word_count.items():
            cleaned_word = regex.sub("", word)
            if cleaned_word not in WORDS_TO_REMOVE and count > 2:
                file.write(cleaned_word + "\n")
def process_dimension(dimension):
    filepath_a = os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt")
    filepath_b = os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt")
    wordcount_a = read_word_counts(filepath_a)
    wordcount_b = read_word_counts(filepath_b)
    unique_to_a = {key: wordcount_a[key] for key in wordcount_a if key not in wordcount_b}
    unique_to_b = {key: wordcount_b[key] for key in wordcount_b if key not in wordcount_a}
    differences = {
        key: abs(wordcount_a[key] - wordcount_b[key])
        for key in wordcount_a if key in wordcount_b and abs(wordcount_a[key] - wordcount_b[key]) > 0
    }
    output_a = {**unique_to_a, **differences}
    output_b = unique_to_b
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), output_a)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), output_b)
for dimension in DIMENSIONS:
    process_dimension(dimension)