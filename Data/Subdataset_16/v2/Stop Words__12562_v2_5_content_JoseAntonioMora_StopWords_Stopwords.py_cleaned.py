import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def fonk1(b6):
    with codecs.open(b6, 'r', b1 = 'utf-8') as file:
        b2 = ""
        for line in file:
            b2 += " " + line.strip()
    return b2
def fonk2(b2):
    b3 = sent_tokenize(b2)
    b4 = [word_tokenize(sentence) for sentence in b3]
    return b3, b4
def fonk3(b3, b4, b8):
    print("\n[Sentence {}] -> {}\n".format(b8, b3[b8]))
    b5 = b4[b8]
    for i, token in enumerate(b5):
        print("Token {} -> {}".format(i, token))
    print("\nTotal word b5 in sentence {}: {} b5".format(b8, len(b5)))
    print("\nTotal b3: {}".format(len(b3) - 1))
def fonk4():
    b6 = 'texto.txt'
    b2 = fonk1(b6)
    b3, b4 = fonk2(b2)
    b7 = len(b3)
    print("\nThe b2 contains {} b3.\nStarting from 0 to {}\n".format(b7, b7 - 1))
    try:
        b8 = int(input("Enter the sentence number: "))
    except ValueError:
        print("\n\nInvalid sentence number")
        return
    if 0 <= b8 < b7:
        fonk3(b3, b4, b8)
    else:
        print("\n\nInvalid sentence number")
if b9 = = "__main__":
    fonk4()