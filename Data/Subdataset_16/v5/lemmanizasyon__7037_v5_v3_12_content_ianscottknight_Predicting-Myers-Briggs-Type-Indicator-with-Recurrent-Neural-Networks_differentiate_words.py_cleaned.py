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
def fonk1(filepath):
    with open(filepath, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(filepath, word_count):
    b4 = re.compile("[^a-zA-Z]")
    with open(filepath, "w") as file:
        for word, count in word_count.items():
            b5 = b4.sub("", word)
            if b5 not in b3 and count > 2:
                file.write(b5 + "\n")
def fonk3(dimension):
    b6 = os.path.join(b1, f"extreme_examples_{dimension[0]}.txt")
    b7 = os.path.join(b1, f"extreme_examples_{dimension[1]}.txt")
    b8 = fonk1(b6)
    b9 = fonk1(b7)
    b10 = {key: b8[key] for key in b8 if key not in b9}
    b11 = {key: b9[key] for key in b9 if key not in b8}
    b12 = {
        key: abs(b8[key] - b9[key])
        for key in b8 if key in b9 and abs(b8[key] - b9[key]) > 0
    }
    b13 = {**b10, **b12}
    b14 = b11
    fonk2(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b13)
    fonk2(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b14)
for dimension in b2:
    fonk3(dimension)