import os
import collections
import re
b1 = "data"
b2 = ["IE", "NS", "FT", "PJ"]
b3 = {
    "intj", "intp", "infj", "infp", "istj", "istp", "isfj", "isfp",
    "entj", "entp", "enfj", "enfp", "estj", "estp", "esfj", "esfp",
    "si", "ni", "ti", "fi", "se", "ne", "te", "fe", "nt", "nf",
    "sxsp", "spsx", "spso", "sxso", "sosp", "sosx", "sp", "sx",
    "sj", "sf", "st", "le", "socionic", "socionics", "enneagram",
    "d", "w", "mbti"
}
def fonk1(file_path):
    with open(file_path, "r") as file:
        return collections.Counter(file.read().split())
def fonk2(file_path, word_dict, b13):
    with open(file_path, "w") as file:
        for word, count in word_dict.items():
            b4 = b13.sub("", word)
            if count > 2:
                file.write(f"{b4}\n" * count)
def fonk3(b11, b12):
    b5 = set(b11) | set(b12)
    b6 = {}
    b7 = {}
    for key in b5:
        if key not in b3:
            if key in b11 and key in b12:
                b8 = b11[key] - b12[key]
                if b8 > 0:
                    b6[key] = b8
                elif b8 < 0:
                    b7[key] = -b8
            elif key in b11:
                b6[key] = b11[key]
            elif key in b12:
                b7[key] = b12[key]
    return b6, b7
def fonk4(dimension):
    b9 = os.path.join(b1, f"extreme_examples_{dimension[0]}.txt")
    b10 = os.path.join(b1, f"extreme_examples_{dimension[1]}.txt")
    b11 = fonk1(b9)
    b12 = fonk1(b10)
    b6, b7 = fonk3(b11, b12)
    b13 = re.compile("[^a-zA-Z]")
    fonk2(os.path.join(b1, f"special_words_{dimension[0]}.txt"), b6, b13)
    fonk2(os.path.join(b1, f"special_words_{dimension[1]}.txt"), b7, b13)
if b14 = = "__main__":
    for dimension in b2:
        fonk4(dimension)