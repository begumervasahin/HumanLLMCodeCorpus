import re
from nltk.corpus import opinion_lexicon
def fonk1():
    b1 = {}
    b2 = opinion_lexicon.b5()
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
    b3 = open(test_file_path, 'r', encoding='ISO-8859-1')
    b4 = open(out_file_path, 'w')
    a2 = 1
    for tweet in b3:
        b5 = tweet.split()
        a3 = 0
        a4 = 0
        for word in b5:
            b6 = word.lower()
            if b6 in b1:
                if b1[b6] == 1:
                    a4 += 1
                elif b1[b6] == 0:
                    a3 += 1
        if a4 > a3:
            b4.write(str(a2) + " positive\n")
        elif a4 < a3:
            b4.write(str(a2) + " negative\n")
        else:
            b4.write(str(a2) + " neutral\n")
        a2 += 1
    b3.close()
    b4.close()
if b7 = = "__main__":
    b1 = fonk1()
    fonk2("test.list", "baseline_out.txt", b1)