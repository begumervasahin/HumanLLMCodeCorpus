import codecs
from datetime import datetime, timedelta
import sys
import time
def fonk1(line):
    b1 = line.strip().split("\t")
    if len(b1) <= 9 or len(b1[6]) != 18:
        return ['', '', '', [], [], [], [], 0, 0]
    b2 = b1[6]
    b3 = b1[8]
    b4 = b1[9][:b1[9].find("2012") + 4]
    try:
        b5 = datetime.strptime(b4, "%I:%M %p - %d %b %Y")
        b6 = b5 + timedelta(hours=7)
        b7 = b6.strftime("%a %b %d %H:%M:%S %Y")
    except ValueError:
        return ['', '', '', [], [], [], [], 0, 0]
    b11, b12, b8 = fonk2(b3)
    b9 = [None]
    nfollowers, b10 = 0, 0
    return [b7, b2, b3, b11, b12, b8, b9, nfollowers, b10]
def fonk2(b3):
    b11 = []
    b12 = []
    b8 = []
    for word in b3.split():
        if word.startswith("@"):
            b12.append(word[1:])
        elif word.startswith("
            b11.append(word[1:])
        elif word.startswith("http"):
            b8.append(word)
    return b11, b12, b8
def fonk3(b19, b20):
    b13 = {}
    with codecs.open(b19, 'r', 'utf-8') as file_in:
        for line in file_in:
            b14 = fonk1(line)
            if not b14[0]:
                continue
            try:
                b15 = fonk4(b14[0])
            except Exception as e:
                print(f"Error parsing time: {b14[0]} | Line: {line.strip()}\n{e}")
                continue
            b16 = str([b15] + b14)
            if b15 in b13:
                b13[b15].append(b16)
            else:
                b13[b15] = [b16]
    fonk5(b13, b20)
def fonk4(tweet_gmttime):
    b17 = time.strptime(tweet_gmttime, '%a %b %d %H:%M:%S %Y')
    return int(time.mktime(b17))
def fonk5(b13, b20):
    with codecs.open(b20, 'w', 'utf-8') as file_out:
        for timestamp, tweet_list in sorted(b13.items()):
            for tweet in tweet_list:
                file_out.write(tweet + "\n")
if b18 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <b19> <b20>")
        sys.exit(1)
    b19 = sys.argv[1]
    b20 = sys.argv[2]
    fonk3(b19, b20)