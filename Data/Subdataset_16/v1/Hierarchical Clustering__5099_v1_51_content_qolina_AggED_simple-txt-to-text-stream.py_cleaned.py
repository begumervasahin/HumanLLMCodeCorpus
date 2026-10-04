import codecs
from datetime import datetime, timedelta
import sys
import time
def fonk1(line):
    b1 = line.strip().split("\t")
    b2 = b1[6]
    b3 = b1[8]
    if len(b2) != 18:
        return ['', '', '', [], [], [], [], 0, 0]
    b4 = b1[9][:b1[9].find("2012") + 4]
    try:
        b5 = datetime.strptime(b4, "%I:%M %p - %d %b %Y")
        b5 += timedelta(b6 = 7)
        b7 = b5.strftime("%a %b %d %H:%M:%S %Y")
    except ValueError:
        return ['', '', '', [], [], [], [], 0, 0]
    b8 = []
    b9 = []
    b10 = []
    for word in b3.split():
        if word.startswith("@"):
            b9.append(word[1:])
        elif word.startswith("
            b8.append(word[1:])
        elif word.startswith("http"):
            b10.append(word)
    b11 = [None]
    a1 = 0
    a2 = 0
    return [b7, b2, b3, b8, b9, b10, b11, a1, a2]
def fonk2(b20, b21):
    b12 = {}
    with codecs.open(b20, 'r', 'utf-8') as file_in:
        for line in file_in:
            b13 = fonk1(line)
            if not b13[0]:
                continue
            try:
                b14 = b13[0]
                b15 = time.strptime(b14, '%a %b %d %H:%M:%S %Y')
                b16 = int(time.mktime(b15))
                b17 = str([b16] + b13)
                if b16 in b12:
                    b12[b16].append(b17)
                else:
                    b12[b16] = [b17]
            except Exception as e:
                print(f"Problem with b14: {b14}, line: {line.strip()}")
                print(e)
    with codecs.open(b21, 'w', 'utf-8') as file_out:
        for item in sorted(b12.items(), b18 = lambda a: a[0]):
            for sub_item in item[1]:
                file_out.write(sub_item + "\n")
if b19 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <b20> <b21>")
        sys.exit(1)
    b20 = sys.argv[1]
    b21 = sys.argv[2]
    fonk2(b20, b21)