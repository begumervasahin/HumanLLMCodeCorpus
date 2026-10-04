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
    hashtags, users, b8 = [], [], []
    for word in b3.split():
        if word.startswith("@"):
            users.append(word[1:])
        elif word.startswith("
            hashtags.append(word[1:])
        elif word.startswith("http"):
            b8.append(word)
    b9 = [None]
    nfollowers, b10 = 0, 0
    return [b7, b2, b3, hashtags, users, b8, b9, nfollowers, b10]
def fonk2(b18, b19):
    b11 = {}
    with codecs.open(b18, 'r', 'utf-8') as file_in:
        for line in file_in:
            b12 = fonk1(line)
            if not b12[0]:
                continue
            b13 = b12[0]
            try:
                b14 = time.strptime(b13, '%a %b %d %H:%M:%S %Y')
                b15 = int(time.mktime(b14))
            except Exception as e:
                print(f"Error parsing time: {b13} | Line: {line.strip()}\n{e}")
                continue
            b16 = str([b15] + b12)
            if b15 in b11:
                b11[b15].append(b16)
            else:
                b11[b15] = [b16]
    with codecs.open(b19, 'w', 'utf-8') as file_out:
        for timestamp, tweet_list in sorted(b11.items()):
            for tweet in tweet_list:
                file_out.write(tweet + "\n")
if b17 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <b18> <b19>")
        sys.exit(1)
    b18 = sys.argv[1]
    b19 = sys.argv[2]
    fonk2(b18, b19)