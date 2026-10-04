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
def fonk2(filename, word_count):
    b4 = re.compile("[^b9-zA-Z]")
    with open(filename, "w") as file:
        for key, count in word_count.items():
            b5 = b4.sub("", str(key))
            if b5 not in b3 and count > 2:
                file.write(b5 + "\n")
for dimension in b2:
    b6 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[0]}.txt"))
    b7 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[1]}.txt"))
    b8 = set(b6) | set(b7)
    b9 = {}
    b10 = {}
    for key in b8:
        if key in b6 and key not in b7:
            b9[key] = b6[key]
        elif key in b7 and key not in b6:
            b10[key] = b7[key]
        elif key in b6 and key in b7:
            b11 = abs(b6[key] - b7[key])
            if b11 > 0:
                b9[key] = b11
    fonk2(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b9)
    fonk2(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b10)