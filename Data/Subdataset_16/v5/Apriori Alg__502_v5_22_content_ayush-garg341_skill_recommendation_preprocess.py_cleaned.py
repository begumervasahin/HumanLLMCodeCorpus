import re
import pandas as pd
def fonk1(frame):
    b1 = ['c
    b2 = []
    for _, b3 in frame.iteritems():
        b3 = b3.replace('>', '').replace('<', '').replace('...', '')
        b4 = b3.split(',')
        b5 = []
        b6 = re.compile(r'([a-z].*[0-9])')
        b7 = re.compile(r'([a-z].*[a-z])')
        for b9 in b4:
            b8 = b9.split(' ')
            if len(b8) <= 4:
                b9 = b9.lower().strip()
                if (b6.match(b9) or
                    b7.match(b9) or
                    b9 in b1):
                    b10 = fonk2(b9)
                    if b10 not in b5:
                        b5.append(b10)
        b2.append(b5)
    return b2
def fonk2(b9):
    b11 = {
        '?': '', '&amp;': '', '.': '', '&': '', '
    }
    for old, new in b11.items():
        b9 = b9.replace(old, new)
    if b9.startswith('.') and not b9.startswith('.net'):
        b9 = b9[1:]
    return b9
