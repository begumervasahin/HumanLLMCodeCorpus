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
def process_dimension(dimension):
    type_a_file = os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt")
    type_b_file = os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt")
    wordcount_a = read_word_counts(type_a_file)
    wordcount_b = read_word_counts(type_b_file)
    common_keys = set(wordcount_a.keys()).union(set(wordcount_b.keys()))
    a_words = {}
    b_words = {}
    regex = re.compile("[^a-zA-Z]")
    for key in common_keys:
        if key not in WORDS_TO_REMOVE:
            count_a = wordcount_a.get(key, 0)
            count_b = wordcount_b.get(key, 0)
            diff = count_a - count_b
            if diff > 0:
                a_words[key] = diff
            elif diff < 0:
                b_words[key] = -diff
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), a_words, regex)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), b_words, regex)
def main():
    for dimension in DIMENSIONS:
        process_dimension(dimension)
if __name__ == "__main__":
    main()