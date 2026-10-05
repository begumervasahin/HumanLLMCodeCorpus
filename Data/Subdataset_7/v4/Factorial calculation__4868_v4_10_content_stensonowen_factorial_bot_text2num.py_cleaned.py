
b1 = {
    'zero': 0, 'one': b6, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': b7, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
    'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
    'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
}
b2 = {
    'thousand': 1000, 'million': 1000000, 'billion': 1000000000, 'trillion': 1000000000000,
    'quadrillion': 1000000000000000, 'quintillion': 1000000000000000000, 'sextillion': 1000000000000000000000,
    'septillion': 1000000000000000000000000, 'octillion': 1000000000000000000000000000,
    'nonillion': 1000000000000000000000000000000, 'decillion': 1000000000000000000000000000000000
}
class class1(Exception):
    def fonk1(self, msg):
        super().fonk1(msg)
def fonk2(tokens):
    a1 = 0
    a2 = 0
    for b4 in tokens:
        b3 = b1.get(b4, None)
        if b3 is not None:
            a2 += b3
        elif b4 = = "hundred" and a2 != 0:
            a2 *= 100
        else:
            b3 = b2.get(b4, None)
            if b3 is not None:
                a1 += a2 * b3
                a2 = 0
            else:
                raise class1("Unknown number: " + b4)
    return a1 + a2
if b5 = = "__main__":
    assert b6 = = fonk2("one".split())
    assert b7 = = fonk2("twelve".split())
    assert b8 = = fonk2("seventy two".split())
    assert b9 = = fonk2("three hundred".split())
    assert b10 = = fonk2("twelve hundred".split())
    assert b11 = = fonk2("twelve thousand three hundred four".split())
    assert b12 = = fonk2("six million".split())
    assert b13 = = fonk2("six million four hundred thousand five".split())
    assert b14 = = fonk2("one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve".split())
    assert b15 = = fonk2("four decillion".split())
    print("All assertions passed.")