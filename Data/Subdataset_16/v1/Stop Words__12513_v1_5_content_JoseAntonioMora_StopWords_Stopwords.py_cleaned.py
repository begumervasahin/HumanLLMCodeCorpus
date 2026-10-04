import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def fonk1(b5):
    with codecs.open(b5, 'r', b1 = 'utf-8') as file:
        b2 = ""
        for line in file:
            b2 += " " + line.strip()
    return b2
def fonk2(b2):
    b3 = sent_tokenize(b2)
    b4 = [word_tokenize(sentence) for sentence in b3]
    return b3, b4
def fonk3():
    b5 = 'texto.txt'
    b2 = fonk1(b5)
    b3, b4 = fonk2(b2)
    b6 = len(b3)
    print("\nThe b2 contains {} b3.\nStarting from 0 to {}\n".format(b6, b6 - 1))
    try:
        b7 = int(input("Enter the sentence number: "))
    except ValueError:
        print("\n\nInvalid sentence number")
        return
    if 0 <= b7 < b6:
        print("\n[Sentence {}] -> {}\n".format(b7, b3[b7]))
        b8 = b4[b7]
        for i, token in enumerate(b8):
            print("Token {} -> {}".format(i, token))
        print("\nTotal word b8 in sentence {}: {} b8".format(b7, len(b8)))
        print("\nTotal b3: {}".format(b6 - 1))
    else:
        print("\n\nInvalid sentence number")
if b9 = = "__main__":
    fonk3()