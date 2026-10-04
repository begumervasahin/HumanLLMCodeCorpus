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
def get_word_counts(file_path):
    with open(file_path, "r") as f:
        return collections.Counter(f.read().split())
def write_special_words(file_path, word_dict, regex):
    with open(file_path, "w") as f:
        for key, value in word_dict.items():
            cleaned_key = regex.sub("", key)
            if value > 2:
                f.write(f"{cleaned_key}\n" * value)
for dimension in DIMENSIONS:
    wordcount_a = get_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt"))
    wordcount_b = get_word_counts(os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt"))
    combined_keys = set(wordcount_a.keys()) | set(wordcount_b.keys())
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
    regex = re.compile("[^a-zA-Z]")
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), diff_a, regex)
    write_special_words(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), diff_b, regex)