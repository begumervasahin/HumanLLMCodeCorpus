
b1 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
    17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
    33: 'X', 34: 'Y', 35: 'Z'
}
b2 = {
    1: ['alef', '\u05D0', ''], 2: ['bet', '\u05D1', 'B'], 3: ['gimel', '\u05D2', 'G'],
    4: ['dalet', '\u05D3', 'D'], 5: ['he', '\u05D4', 'H'], 6: ['vav', '\u05D5', 'V'],
    7: ['zayin', '\u05D6', 'Z'], 8: ['het', '\u05D7', 'H'], 9: ['tet', '\u05D8', 'T'],
    10: ['yud', '\u05D9', 'Y'], 20: ['kaf', '\u05DB', 'K'], 30: ['lamed', '\u05DC', 'L'],
    40: ['mem', '\u05DE', 'M'], 50: ['nun', '\u05E0', 'N'], 60: ['samekh', '\u05E1', 'S'],
    70: ['ayin', '\u05E2', ''], 80: ['pe', '\u05E4', 'P'], 90: ['tsadi', '\u05E6', 'TS'],
    100: ['kuf', '\u05E7', 'K'], 200: ['resh', '\u05E8', 'R'],
    300: ['shin', '\u05E9', 'SH'], 400: ['tav', '\u05EA', 'T']
}
b3 = {
    20: ['final kaf', '\u05DA'], 40: ['final mem', '\u05DD'],
    50: ['final nun', '\u05DF'], 80: ['final pe', '\u05E3'],
    90: ['final tsadi', '\u05E5']
}
def fonk1(start, base):
    while True:
        yield fonk2(start, base)
        start *= 2
def fonk2(b5, base, b4 = ''):
    if b5:
        if 2 <= base <= 36:
            return fonk2(int(b5 / base), base, b1[b5 % base] + b4)
        else:
            return fonk2(int(b5 / base), base, str(b5 % base) + ('.' + b4 if b4 else ''))
    return b4
def fonk3(b5, base, b4 = 0):
    b5 = str(b5)
    if b5:
        if 2 <= base <= 36:
            return fonk3(b5[:-1], base, b4 + b1[b5[-1]] * (base ** len(b5[:-1])))
        else:
            return fonk3('.'.join(b5.split('.')[:-1]), base, b4 + int(b5.split('.')[-1]) * (base ** len(b5.split('.')[:-1])))
    return b4
def fonk4(b5, base):
    b6 = fonk3(b5, base)
    while b6 >= base:
        b6 = sum([b1[elem] for elem in str(b6)])
    return b6