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
for dimension in DIMENSIONS:
    wordcount_a = collections.Counter()
    wordcount_b = collections.Counter()
    with open(os.path.join(DATA_DIR, f"extreme_examples_{dimension[0]}.txt"), "r") as f:
        wordcount_a.update(f.read().split())
    with open(os.path.join(DATA_DIR, f"extreme_examples_{dimension[1]}.txt"), "r") as f:
        wordcount_b.update(f.read().split())
    common_keys = set(wordcount_a.keys()) | set(wordcount_b.keys())
    a = {}
    b = {}
    for key in common_keys:
        if key in wordcount_a and key not in wordcount_b:
            a[key] = wordcount_a[key]
        elif key in wordcount_b and key not in wordcount_a:
            b[key] = wordcount_b[key]
        elif key in wordcount_a and key in wordcount_b:
            diff = wordcount_a[key] - wordcount_b[key]
            if diff > 0:
                a[key] = diff
            elif diff < 0:
                b[key] = -diff
    regex = re.compile("[^a-zA-Z]")
    with open(os.path.join(DATA_DIR, f"special_words_{dimension[0]}.txt"), "w") as f:
        for key in a.keys():
            modified_key = regex.sub("", str(key))
            if modified_key not in WORDS_TO_REMOVE and a[key] > 2:
                f.write(modified_key + "\n")
    with open(os.path.join(DATA_DIR, f"special_words_{dimension[1]}.txt"), "w") as f:
        for key in b.keys():
            modified_key = regex.sub("", str(key))
            if modified_key not in WORDS_TO_REMOVE and b[key] > 2:
                f.write(modified_key + "\n")