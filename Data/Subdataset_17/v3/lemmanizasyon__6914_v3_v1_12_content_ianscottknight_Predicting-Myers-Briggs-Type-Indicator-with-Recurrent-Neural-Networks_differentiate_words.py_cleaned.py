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
REGEX = re.compile("[^a-zA-Z]")
def read_word_counts(filepath):
    with open(filepath, "r") as file:
        return collections.Counter(file.read().split())
def clean_word(word):
    return REGEX.sub("", word)
def write_special_words(filepath, word_diff):
    with open(filepath, "w") as file:
        for word, count in word_diff.items():
            cleaned_word = clean_word(word)
            if cleaned_word not in WORDS_TO_REMOVE and count > 2:
                file.write(cleaned_word + "\n")
def process_dimension(dimension):
    wordcount_a = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt"))
    wordcount_b = read_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt"))
    combined_keys = set(wordcount_a.keys()).union(set(wordcount_b.keys()))
    a_diff = {}
    b_diff = {}
    for key in combined_keys:
        if key in wordcount_a and key not in wordcount_b:
            a_diff[key] = wordcount_a[key]
        elif key in wordcount_b and key not in wordcount_a:
            b_diff[key] = wordcount_b[key]
        elif key in both wordcount_a and wordcount_b:
            diff = wordcount_a[key] - wordcount_b[key]
            if diff > 0:
                a_diff[key] = diff
            elif diff < 0:
                b_diff[key] = -diff
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), a_diff)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), b_diff)
def main():
    for dimension in DIMENSIONS:
        process_dimension(dimension)
if __name__ == "__main__":
    main()