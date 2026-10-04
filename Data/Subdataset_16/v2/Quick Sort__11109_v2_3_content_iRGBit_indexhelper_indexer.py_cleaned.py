import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
b2 = 'EN'
b3 = 'files/sample.txt'
b4 = 'out.txt'
def fonk1(language):
    return f'b11/stop_words_{language}.txt'
def fonk2():
    b5 = input(f"Select language from the following: {', '.join(b1)} (default is {b2}): ").upper()
    if b5 in b1:
        b6 = fonk1(b5)
        print(f"Parsing your text with the {b5} b11.")
    else:
        b6 = fonk1(b2)
        print("Invalid language. Assuming English...")
    b7 = input(f"Select name of output text file (default is {b4}): ")
    if not b7:
        b7 = b4
    elif not b7.endswith('.txt'):
        b7 += '.txt'
    print(f"Printing your results to {b7}.")
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given, {b3} and {b6} will be used as default files.\n")
        sys.exit()
    elif len(sys.argv) == 2:
        b8 = sys.argv[1]
    else:
        b8 = b3
    print(f'Using {b8} as file and {b6} as stop word reference, printing to {b7}.\n')
    fonk3(b8, b6, b7)
def fonk3(b8, b6, b7):
    with open(b8, 'r', b9 = 'utf-8') as file:
        b10 = file.read().lower().split()
        b10 = [word.strip(string.punctuation) for word in b10]
    with open(b6, 'r', b9 = 'utf-8') as file:
        b11 = file.read().splitlines()
    b12 = [word for word in b10 if word not in b11]
    b13 = Counter(b12)
    b14 = sum(b13.values())
    b15 = b14 / len(b13)
    b16 = {word: count for word, count in b13.items() if count >= b15}
    b17 = sorted(b16.items())
    with open(b7, 'w') as file:
        for word, count in b17:
            file.write(f'{word}: {count}\n')
if b18 = = '__main__':
    fonk2()