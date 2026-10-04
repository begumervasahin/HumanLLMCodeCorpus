import os
import collections
import re
b1 = "data"
b2 = ["IE", "NS", "FT", "PJ"]
b3 = [
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx", "sj", "sf", "st",
    "le", "socionic", "socionics", "enneagram", "d", "w", "mbti",
]
def fonk1(filename):
    with open(filename, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(word):
    return re.sub("[^a-zA-Z]", "", word)
def fonk3(filename, word_count):
    with open(filename, "w") as file:
        for word, count in word_count.items():
            b4 = fonk2(word)
            if b4 not in b3 and count > 2:
                file.write(f"{b4}\n")
def fonk4(dimension, data_dir):
    """
    Processes word counts for a given dimension and writes special words to files.
    :param dimension: A tuple containing the two dimension types to be processed (e.g., ("I", "E")).
    :param data_dir: Directory where data files are stored.
    """
    b5 = fonk1(os.path.join(data_dir, f"extreme_examples_{dimension[0]}.txt"))
    b6 = fonk1(os.path.join(data_dir, f"extreme_examples_{dimension[1]}.txt"))
    b7 = set(b5) | set(b6)
    b8 = {}
    b9 = {}
    for word in b7:
        b10 = b5.get(word, 0)
        b11 = b6.get(word, 0)
        if b10 > 0 and b11 = = 0:
            b8[word] = b10
        elif b11 > 0 and b10 = = 0:
            b9[word] = b11
        elif b10 > 0 and b11 > 0:
            b12 = abs(b10 - b11)
            if b12 > 0:
                b8[word] = b12
    fonk3(os.path.join(data_dir, f"special_words_{dimension[0]}.txt"), b8)
    fonk3(os.path.join(data_dir, f"special_words_{dimension[1]}.txt"), b9)
def fonk5(dimensions, data_dir):
    for dimension in dimensions:
        fonk4(dimension, data_dir)
if b13 = = "__main__":
    fonk5(b2, b1)