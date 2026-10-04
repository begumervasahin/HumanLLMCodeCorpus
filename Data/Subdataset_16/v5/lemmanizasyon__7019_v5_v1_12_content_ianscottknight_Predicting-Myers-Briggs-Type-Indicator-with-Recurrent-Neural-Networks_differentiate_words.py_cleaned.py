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
def fonk1(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(b12, b13):
    b5 = set(b12.keys()).union(set(b13.keys()))
    b6 = {}
    b7 = {}
    for word in b5:
        if word in b12 and word not in b13:
            b6[word] = b12[word]
        elif word in b13 and word not in b12:
            b7[word] = b13[word]
        elif word in b12 and word in b13:
            b8 = b12[word] - b13[word]
            if b8 > 0:
                b6[word] = b8
            elif b8 < 0:
                b7[word] = -b8
    return b6, b7
def fonk3(filename, word_dict):
    with open(os.path.join(b1, filename), "w") as file:
        for word, count in word_dict.items():
            b9 = b4.sub("", word)
            if b9 not in b3 and count > 2:
                file.write(b9 + "\n")
for dimension in b2:
    b10 = os.path.join(b1, f"extreme_examples_{dimension[0]}.txt")
    b11 = os.path.join(b1, f"extreme_examples_{dimension[1]}.txt")
    b12 = fonk1(b10)
    b13 = fonk1(b11)
    b6, b7 = fonk2(b12, b13)
    fonk3(f"special_words_{dimension[0]}.txt", b6)
    fonk3(f"special_words_{dimension[1]}.txt", b7)