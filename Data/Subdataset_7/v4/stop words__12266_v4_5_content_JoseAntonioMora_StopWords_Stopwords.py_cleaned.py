
import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
b1 = codecs.open('b2.txt', 'r', encoding='utf-8')
b2 = ""
for b3 in b1:
    b3 = b3.strip()
    b2 = b2 + " " + b3
b4 = sent_tokenize(b2)
print("\nThe text contains {} sentences.".format(len(b4)))
print("Numbered from 0 to {}\n".format(len(b4) - 1))
b5 = int(input("Enter the sentence number: "))
if 0 < b5 < len(b4):
    print("\n[Sentence {}] -> {}\n".format(b5, b4[b5]))
    b6 = word_tokenize(b4[b5])
    for index, token in enumerate(b6):
        print("Token {} -> {}".format(index, token))
    print("\nTotal word b4 in sentence {}: {}".format(b5, len(b6)))
    print("Total sentences: {}\n".format(len(b4) - 1))
else:
    print("\nInvalid sentence number. Please enter a valid number.")