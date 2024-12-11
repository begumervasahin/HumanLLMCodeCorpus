import re
from nltk.corpus import opinion_lexicon
def fonk1():
    b1 = {}
    b2 = opinion_lexicon.b4()
    a1 = 0
    for word in b2:
        if a1 = = 0:
            b1[word] = a1
            if re.search("zombie", word):
                a1 = 1
        else:
            b1[word] = a1
    return b1
def fonk2(test_file_path, out_file_path, b1):
    with open(test_file_path, 'r', b3 = 'ISO-8859-1') as test_file, open(out_file_path, 'w') as out_file:
        a2 = 1
        for tweet in test_file:
            b4 = tweet.split()
            a3 = 0
            a4 = 0
            for word in b4:
                b5 = word.lower()
                if b5 in b1:
                    if b1[b5] == 1:
                        a4 += 1
                    elif b1[b5] == 0:
                        a3 += 1
            if a4 > a3:
                out_file.write(f"{a2} positive\n")
            elif a4 < a3:
                out_file.write(f"{a2} negative\n")
            else:
                out_file.write(f"{a2} neutral\n")
            a2 += 1
if b6 = = "__main__":
    b1 = fonk1()
    fonk2("test.list", "baseline_out.txt", b1)