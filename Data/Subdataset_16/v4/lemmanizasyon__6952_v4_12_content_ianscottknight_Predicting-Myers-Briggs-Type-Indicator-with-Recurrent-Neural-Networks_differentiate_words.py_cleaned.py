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
for dimension in b2:
    b4 = {}
    b5 = {}
    with open(os.path.join(b1, f"extreme_examples_{dimension[0]}.txt"), "r") as f:
        b4 = collections.Counter(f.read().split())
    with open(os.path.join(b1, f"extreme_examples_{dimension[1]}.txt"), "r") as f:
        b5 = collections.Counter(f.read().split())
    b6 = list(set(b4.keys()) | set(b5.keys()))
    b7 = {}
    b8 = {}
    for key in b6:
        if key in b4 and key not in b3:
            if key in b5:
                b9 = b4[key] - b5[key]
                if b9 > 0:
                    b7[key] = b9
                elif b9 < 0:
                    b8[key] = -b9
            else:
                b7[key] = b4[key]
        elif key in b5 and key not in b3:
            b8[key] = b5[key]
    b10 = re.compile("[^b7-zA-Z]")
    with open(os.path.join(b1, f"special_words_{dimension[0]}.txt"), "w") as f:
        for key, value in b7.items():
            b11 = b10.sub("", str(key))
            if value > 2:
                f.write(f"{b11}\n" * value)
    with open(os.path.join(b1, f"special_words_{dimension[1]}.txt"), "w") as f:
        for key, value in b8.items():
            b11 = b10.sub("", str(key))
            if value > 2:
                f.write(f"{b11}\n" * value)