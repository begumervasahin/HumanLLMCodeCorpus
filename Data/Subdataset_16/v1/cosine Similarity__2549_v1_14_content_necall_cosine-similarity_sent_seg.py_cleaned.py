import nltk
import os
def fonk1(content):
    return ''.join([c for c in content if 32 <= ord(c) <= 126])
def fonk2(b7, b8):
    print(f"Number of lines: {len(b7)}")
    b1 = []
    for i, content in enumerate(b7):
        if (i + 1) % b2 = = 0:
            print(f"Progress: {float(i + 1) / len(b7):.2%}")
        b3 = fonk1(content).replace("Mr .", "Mr")
        b4 = b8.tokenize(b3)
        b1.extend(b4)
    return b1
def fonk3():
    b5 = "/Users/ken77921/Desktop/TA/2004,7-05_nyt_tok"
    b6 = "/Users/ken77921/Desktop/TA/2004,7-05_nyt_sent"
    with open(b5, 'r') as doc:
        b7 = doc.readlines()
    b8 = nltk.data.load('tokenizers/punkt/english.pickle')
    b1 = fonk2(b7, b8)
    with open(b6, "w") as f_out:
        for sent in b1:
            f_out.write(sent + "\n")
if b9 = = "__main__":
    fonk3()