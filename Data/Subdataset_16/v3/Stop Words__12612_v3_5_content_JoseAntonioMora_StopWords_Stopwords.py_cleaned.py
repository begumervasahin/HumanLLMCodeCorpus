import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def fonk1(b7):
    with codecs.open(b7, 'r', b1 = 'utf-8') as file:
        b2 = " ".join(line.strip() for line in file)
    return b2
def fonk2(b2):
    b3 = sent_tokenize(b2)
    b4 = [word_tokenize(b5) for b5 in b3]
    return b3, b4
def fonk3(b3, b4, b9):
    b5 = b3[b9]
    b6 = b4[b9]
    print(f"\n[Sentence {b9}] -> {b5}\n")
    for i, token in enumerate(b6):
        print(f"Token {i} -> {token}")
    print(f"\nTotal word b6 in b5 {b9}: {len(b6)} b6")
    print(f"\nTotal b3: {len(b3) - 1}")
def fonk4():
    b7 = 'texto.txt'
    b2 = fonk1(b7)
    b3, b4 = fonk2(b2)
    b8 = len(b3)
    print(f"\nThe b2 contains {b8} b3.\nStarting from 0 to {b8 - 1}\n")
    try:
        b9 = int(input("Enter the b5 number: "))
    except ValueError:
        print("\n\nInvalid b5 number")
        return
    if 0 <= b9 < b8:
        fonk3(b3, b4, b9)
    else:
        print("\n\nInvalid b5 number")
if b10 = = "__main__":
    fonk4()