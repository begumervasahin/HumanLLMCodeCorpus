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
b4 = re.compile("[^a-zA-Z]")
def fonk1(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(b12, b13):
    b5 = {}
    b6 = {}
    b7 = set(b12.keys()) | set(b13.keys())
    for key in b7:
        if key not in b3:
            b8 = b12.get(key, 0)
            b9 = b13.get(key, 0)
            b10 = b8 - b9
            if b10 > 0:
                b5[key] = b10
            elif b10 < 0:
                b6[key] = -b10
    return b5, b6
def fonk3(filename, word_counts):
    with open(filename, "w") as output_file:
        for word, count in word_counts.items():
            b11 = b4.sub("", word)
            if count > 2:
                output_file.write((b11 + "\n") * count)
def fonk4(dimension):
    b12 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[0]}.txt"))
    b13 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[1]}.txt"))
    b5, b6 = fonk2(b12, b13)
    fonk3(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b5)
    fonk3(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b6)
for dimension in b2:
    fonk4(dimension)