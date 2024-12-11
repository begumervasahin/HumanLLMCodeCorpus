import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
b2 = 'EN'
b3 = 'files/sample.txt'
b4 = 'stopwords/stop_words_%s.txt' % b2
b5 = 'out.txt'
def fonk1():
    b6 = fonk2()
    b7 = fonk3(b6)
    b8 = fonk4()
    b9 = fonk5()
    print 'Using %s as file and %s as stop word reference, printing to %s.' % (
        b9, b7, b8)
    print
    fonk6(b9, b7, b8)
def fonk2():
    b10 = "Select Language from the following (%s - default is %s): " % (
        ' '.join(b1), b2)
    b6 = raw_input(b10).upper()
    return b6 if b6 in b1 else b2
def fonk3(b6):
    return 'stopwords/stop_words_%s.txt' % b6 if b6 in b1 else b4
def fonk4():
    b11 = "Select name of output text file (default is %s): " % b5
    b12 = raw_input(b11)
    b12 = b12 if b12.endswith('.txt') else b12 + '.txt'
    return b12 if b12 else b5
def fonk5():
    return sys.argv[1] if len(sys.argv) > 1 else b3
def fonk6(b9, b7, b8):
    b13 = open(b9).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    b13 = [word.strip(string.punctuation) for word in b13]
    b14 = open(b7).read().decode("utf-8-sig").encode("utf-8").splitlines()
    b15 = [word for word in b13 if word not in b14]
    b16 = Counter(b15)
    b17 = sum(b16.values())
    b18 = b17 / len(b16)
    b19 = {key: value for key, value in b16.iteritems() if value >= b18}
    b20 = sorted(b19.items(), key=lambda x: x[0])
    with open(b8, 'w+') as output_file:
        for word, count in b20:
            output_file.write('%s: %s\n' % (word, count))
if b21 = = '__main__':
    fonk1()