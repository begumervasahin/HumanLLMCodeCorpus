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
b4 = re.compile("[^a-zA-Z]")
def fonk1(filepath):
    with open(filepath, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(word):
    return b4.sub("", word)
def fonk3(filepath, word_diff):
    with open(filepath, "w") as file:
        for word, count in word_diff.items():
            b5 = fonk2(word)
            if b5 not in b3 and count > 2:
                file.write(b5 + "\n")
def fonk4(dimension):
    b6 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[0]}.txt"))
    b7 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[1]}.txt"))
    b8 = set(b6.keys()).union(set(b7.keys()))
    b9 = {}
    b10 = {}
    for key in b8:
        if key in b6 and key not in b7:
            b9[key] = b6[key]
        elif key in b7 and key not in b6:
            b10[key] = b7[key]
        elif key in both b6 and b7:
            b11 = b6[key] - b7[key]
            if b11 > 0:
                b9[key] = b11
            elif b11 < 0:
                b10[key] = -b11
    fonk3(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b9)
    fonk3(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b10)
def fonk5():
    for dimension in b2:
        fonk4(dimension)
if b12 = = "__main__":
    fonk5()