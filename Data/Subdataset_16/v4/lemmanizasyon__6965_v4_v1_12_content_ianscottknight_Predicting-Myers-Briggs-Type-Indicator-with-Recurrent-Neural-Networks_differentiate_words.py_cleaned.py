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
for dimension in b2:
    b5 = collections.Counter()
    b6 = collections.Counter()
    with open(os.path.join(b1, f"extreme_examples_{dimension[0]}.txt"), "r") as file_a:
        b5.update(file_a.read().split())
    with open(os.path.join(b1, f"extreme_examples_{dimension[1]}.txt"), "r") as file_b:
        b6.update(file_b.read().split())
    b7 = set(b5.keys()).union(set(b6.keys()))
    b8 = {}
    b9 = {}
    for word in b7:
        if word in b5 and word not in b6:
            b8[word] = b5[word]
        elif word in b6 and word not in b5:
            b9[word] = b6[word]
        elif word in b5 and word in b6:
            b10 = b5[word] - b6[word]
            if b10 > 0:
                b8[word] = b10
            elif b10 < 0:
                b9[word] = -b10
    def fonk1(filename, word_dict):
        with open(os.path.join(b1, filename), "w") as file:
            for word, count in word_dict.items():
                b11 = b4.sub("", word)
                if b11 not in b3 and count > 2:
                    file.write(b11 + "\n")
    fonk1(f"special_words_{dimension[0]}.txt", b8)
    fonk1(f"special_words_{dimension[1]}.txt", b9)