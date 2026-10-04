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
    with open(file_path, "r") as f:
        return collections.Counter(f.read().split())
def fonk2(file_path, word_dict, b11):
    with open(file_path, "w") as f:
        for key, value in word_dict.items():
            b4 = b11.sub("", key)
            if value > 2:
                f.write(f"{b4}\n" * value)
for dimension in b2:
    b5 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[0]}.txt"))
    b6 = fonk1(os.path.join(b1, f"extreme_examples_{dimension[1]}.txt"))
    b7 = set(b5.keys()) | set(b6.keys())
    b8 = {}
    b9 = {}
    for key in b7:
        if key not in b3:
            if key in b5 and key in b6:
                b10 = b5[key] - b6[key]
                if b10 > 0:
                    b8[key] = b10
                elif b10 < 0:
                    b9[key] = -b10
            elif key in b5:
                b8[key] = b5[key]
            elif key in b6:
                b9[key] = b6[key]
    b11 = re.compile("[^a-zA-Z]")
    fonk2(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b8, b11)
    fonk2(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b9, b11)