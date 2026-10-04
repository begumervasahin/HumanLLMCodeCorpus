import os
import collections
import re
b1 = "data"
b2 = ["IE", "NS", "FT", "PJ"]
b3 = [
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx",
    "sj", "sf", "st", "le", "socionic", "socionics", "enneagram",
    "d", "w", "mbti",
]
def fonk1(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(file_path, word_dict, b12):
    with open(file_path, "w") as file:
        for word, count in word_dict.items():
            b4 = b12.sub("", word)
            if count > 2:
                file.write(f"{b4}\n" * count)
def fonk3(dimension):
    b5 = os.path.join(b1, f"extreme_examples_{dimension[0]}.txt")
    b6 = os.path.join(b1, f"extreme_examples_{dimension[1]}.txt")
    b7 = fonk1(b5)
    b8 = fonk1(b6)
    b9 = set(b7.keys()).union(set(b8.keys()))
    b10 = {}
    b11 = {}
    b12 = re.compile("[^a-zA-Z]")
    for key in b9:
        if key not in b3:
            b13 = b7.get(key, 0)
            b14 = b8.get(key, 0)
            b15 = b13 - b14
            if b15 > 0:
                b10[key] = b15
            elif b15 < 0:
                b11[key] = -b15
    fonk2(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b10, b12)
    fonk2(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b11, b12)
def fonk4():
    for dimension in b2:
        fonk3(dimension)
if b16 = = "__main__":
    fonk4()