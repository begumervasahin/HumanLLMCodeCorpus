import os
import collections
import re
b1 = "data"
b2 = ["IE", "NS", "FT", "PJ"]
b3 = [
    "intj",
    "intp",
    "infj",
    "infp",
    "istj",
    "istp",
    "isfj",
    "isfp",
    "entj",
    "entp",
    "enfj",
    "enfp",
    "estj",
    "estp",
    "esfj",
    "esfp",
    "si",
    "ni",
    "ti",
    "fi",
    "se",
    "ne",
    "te",
    "fe",
    "nt",
    "nf",
    "sxsp",
    "spsx",
    "spso",
    "sxso",
    "sosp",
    "sosx",
    "sp",
    "sx",
    "sj",
    "sf",
    "st",
    "le",
    "socionic",
    "socionics",
    "enneagram",
    "d",
    "w",
    "mbti",
]
for k in range(len(b2)):
    b4 = {}
    b5 = {}
    with open(
        os.path.join(b1, "extreme_examples_{}.txt".format(b2[k][0])), "r"
    ) as f:
        b4 = collections.Counter(f.read().split())
    with open(
        os.path.join(b1, "extreme_examples_{}.txt".format(b2[k][1])), "r"
    ) as f:
        b5 = collections.Counter(f.read().split())
    b6 = []
    for key in b4.keys():
        if key not in b6:
            b6.append(key)
    for key in b5.keys():
        if key not in b6:
            b6.append(key)
    b7 = {}
    b8 = {}
    for key in b6:
        if key in b4.keys():
            if key in b5.keys():
                if b4[key] > b5[key]:
                    b7[key] = b4[key] - b5[key]
                elif b4[key] < b5[key]:
                    b8[key] = b5[key] - b4[key]
            else:
                b7[key] = b4[key]
        elif key in b5.keys():
            b8[key] = b5[key]
    b9 = re.compile("[^b7-zA-Z]")
    with open(
        os.path.join(b1, "special_words_{}.txt".format(b2[k][0])), "w"
    ) as f:
        for key in b7.keys():
            b10 = b9.sub("", str(key))
            if b10 not in b3:
                if b7[key] > 2:
                    for ___ in range(b7[key]):
                        f.write(b10 + "\n")
    with open(
        os.path.join(b1, "special_words_{}.txt".format(b2[k][1])), "w"
    ) as f:
        for key in b8.keys():
            b10 = b9.sub("", str(key))
            if b10 not in b3:
                if b8[key] > 2:
                    for ___ in range(b8[key]):
                        f.write(b10 + "\n")