import os
import collections
import re
DATA_DIR = "data"
DIMENSIONS = ["IE", "NS", "FT", "PJ"]
WORDS_TO_REMOVE = {
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx",
    "sj", "sf", "st", "le", "socionic", "socionics", "enneagram",
    "d", "w", "mbti"
}
def get_word_counts(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def write_special_words(file_path, word_dict, regex):
    with open(file_path, "w") as file:
        for word, count in word_dict.items():
            cleaned_word = regex.sub("", word)
            if count > 2:
                file.write(f"{cleaned_word}\n" * count)
def calculate_word_differences(wordcount_a, wordcount_b):
    combined_keys = set(wordcount_a) | set(wordcount_b)
    diff_a = {}
    diff_b = {}
    for key in combined_keys:
        if key not in WORDS_TO_REMOVE:
            if key in wordcount_a and key in wordcount_b:
                diff = wordcount_a[key] - wordcount_b[key]
                if diff > 0:
                    diff_a[key] = diff
                elif diff < 0:
                    diff_b[key] = -diff
            elif key in wordcount_a:
                diff_a[key] = wordcount_a[key]
            elif key in wordcount_b:
                diff_b[key] = wordcount_b[key]
    return diff_a, diff_b
def process_dimension(dimension):
    file_a = os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt")
    file_b = os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt")
    wordcount_a = get_word_counts(file_a)
    wordcount_b = get_word_counts(file_b)
    diff_a, diff_b = calculate_word_differences(wordcount_a, wordcount_b)
    regex = re.compile("[^a-zA-Z]")
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), diff_a, regex)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), diff_b, regex)
if __name__ == "__main__":
    for dimension in DIMENSIONS:
        process_dimension(dimension)