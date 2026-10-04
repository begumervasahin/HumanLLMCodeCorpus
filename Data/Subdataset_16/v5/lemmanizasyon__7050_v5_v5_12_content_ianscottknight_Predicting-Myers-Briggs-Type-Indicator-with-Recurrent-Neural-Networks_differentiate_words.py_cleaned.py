import os
import collections
import re
b1 = "data"
b2 = ["IE", "NS", "FT", "PJ"]
b3 = set([
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx",
    "sj", "sf", "st", "le", "socionic", "socionics", "enneagram",
    "d", "w", "mbti"
])
def fonk1(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(file_path, word_dict, b10):
    with open(file_path, "w") as file:
        for word, count in word_dict.items():
            b4 = b10.sub("", word)
            if count > 2:
                file.write(f"{b4}\n" * count)
def fonk3(dimension):
    """
    Processes word counts for each dimension, calculates differences, and writes special words to output files.
    :param dimension: A string representing a dimension (e.g., "IE").
    """
    b5 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[0]}.txt"))
    b6 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[1]}.txt"))
    b7 = set(b5.keys()) | set(b6.keys())
    b8 = {}
    b9 = {}
    b10 = re.compile("[^a-zA-Z]")
    for word in b7:
        if word not in b3:
            b11 = b5.get(word, 0)
            b12 = b6.get(word, 0)
            b13 = b11 - b12
            if b13 > 0:
                b8[word] = b13
            elif b13 < 0:
                b9[word] = -b13
    fonk2(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b8, b10)
    fonk2(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b9, b10)
for dimension in b2:
    fonk3(dimension)