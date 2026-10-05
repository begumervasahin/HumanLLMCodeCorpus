import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def fonk1(b7):
    with codecs.open(b7, 'r', b1 = 'utf-8') as file:
        return ' '.join(line.strip() for line in file)
def fonk2(b8):
    b2 = sent_tokenize(b8)
    b3 = [word_tokenize(sentence) for sentence in b2]
    return b2, b3
def fonk3(b2):
    b4 = len(b2)
    print(f"\nThe b8 contains {b4} b2.")
    print(f"Numbered from 0 to {b4 - 1}\n")
def fonk4(b9, b2, b3):
    b5 = b2[b9]
    print(f"\n[Sentence {b9}] -> {b5}\n")
    b6 = b3[b9]
    for index, token in enumerate(b6):
        print(f"Token {index} -> {token}")
    print(f"\nTotal word b6 in sentence {b9}: {len(b6)}")
def fonk5():
    b7 = 'texto.txt'
    b8 = fonk1(b7)
    b2, b3 = fonk2(b8)
    fonk3(b2)
    b9 = int(input("Enter the sentence number: "))
    if 0 < b9 < len(b2):
        fonk4(b9, b2, b3)
        print(f"Total b2: {len(b2)}\n")
    else:
        print("\nInvalid sentence number. Please enter a valid number.")
if b10 = = "__main__":
    fonk5()