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
def clean_word(word):
    return re.sub("[^a-zA-Z]", "", word)
def write_special_words(filename, word_count):
    with open(filename, "w") as file:
        for word, count in word_count.items():
            clean_word = clean_word(word)
            if clean_word not in WORDS_TO_REMOVE and count > 2:
                file.write(f"{clean_word}\n")
def process_dimension(dimension, data_dir):
    """
    Processes word counts for a given dimension and writes special words to files.
    :param dimension: A tuple containing the two dimension types to be processed (e.g., ("I", "E")).
    :param data_dir: Directory where data files are stored.
    """
    wordcount_a = read_word_counts(os.path.join(data_dir, f"extreme_examples_{dimension[0]}.txt"))
    wordcount_b = read_word_counts(os.path.join(data_dir, f"extreme_examples_{dimension[1]}.txt"))
    all_words = set(wordcount_a) | set(wordcount_b)
    special_words_a = {}
    special_words_b = {}
    for word in all_words:
        count_a = wordcount_a.get(word, 0)
        count_b = wordcount_b.get(word, 0)
        if count_a > 0 and count_b == 0:
            special_words_a[word] = count_a
        elif count_b > 0 and count_a == 0:
            special_words_b[word] = count_b
        elif count_a > 0 and count_b > 0:
            diff = abs(count_a - count_b)
            if diff > 0:
                special_words_a[word] = diff
    write_special_words(os.path.join(data_dir, f"special_words_{dimension[0]}.txt"), special_words_a)
    write_special_words(os.path.join(data_dir, f"special_words_{dimension[1]}.txt"), special_words_b)
def process_dimensions(dimensions, data_dir):
    for dimension in dimensions:
        process_dimension(dimension, data_dir)
if __name__ == "__main__":
    process_dimensions(DIMENSIONS, DATA_DIR)