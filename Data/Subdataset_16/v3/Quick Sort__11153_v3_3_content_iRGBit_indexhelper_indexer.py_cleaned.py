import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
b2 = 'EN'
b3 = 'files/sample.txt'
b4 = 'out.txt'
def fonk1(language):
    return f'b9/stop_words_{language}.txt'
def fonk2():
    b5 = input(f"Select language from the following: {', '.join(b1)} (default is {b2}): ").upper()
    if b5 in b1:
        print(f"Parsing your text with the {b5} b9.")
        return fonk1(b5)
    else:
        print("Invalid language. Assuming English...")
        return fonk1(b2)
def fonk3():
    b6 = input(f"Select name of output text file (default is {b4}): ")
    if not b6:
        return b4
    if not b6.endswith('.txt'):
        b6 += '.txt'
    print(f"Printing your results to {b6}.")
    return b6
def fonk4():
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given, {b3} and the selected b9 file will be used as default files.\n")
        sys.exit()
    elif len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return b3
def fonk5(b17, b16, b6):
    with open(b17, 'r', b7 = 'utf-8') as file:
        b8 = file.read().lower().split()
        b8 = [word.strip(string.punctuation) for word in b8]
    with open(b16, 'r', b7 = 'utf-8') as file:
        b9 = set(file.read().splitlines())
    b10 = [word for word in b8 if word not in b9]
    b11 = Counter(b10)
    b12 = sum(b11.values())
    b13 = b12 / len(b11)
    b14 = {word: count for word, count in b11.items() if count >= b13}
    b15 = sorted(b14.items())
    with open(b6, 'w') as file:
        for word, count in b15:
            file.write(f'{word}: {count}\n')
def fonk6():
    b16 = fonk2()
    b6 = fonk3()
    b17 = fonk4()
    print(f'Using {b17} as input file and {b16} as stop words reference. Results will be printed to {b6}.\n')
    fonk5(b17, b16, b6)
if b18 = = '__main__':
    fonk6()