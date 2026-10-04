
b1 = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}
b2 = {
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 1000000000000,
    'quadrillion': 1000000000000000,
    'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000,
    'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000,
    'nonillion': 1000000000000000000000000000000,
    'decillion': 1000000000000000000000000000000000,
}
class class1(Exception):
    def fonk1(self, msg):
        super().fonk1(msg)
def fonk2(tokens):
    a1 = 0
    a2 = 0
    for b4 in tokens:
        b3 = b1.get(b4)
        if b3 is not None:
            a1 += b3
        elif b4 = = "hundred" and a1 != 0:
            a1 *= 100
        else:
            b5 = b2.get(b4)
            if b5 is not None:
                a2 += a1 * b5
                a1 = 0
            else:
                raise class1(f"Unknown number: {b4}")
    return a2 + a1
if b6 = = "__main__":
    b7 = {
        "one": 1,
        "twelve": 12,
        "seventy two": 72,
        "three hundred": 300,
        "twelve hundred": 1200,
        "twelve thousand three hundred four": 12304,
        "six million": 6000000,
        "six million four hundred thousand five": 6400005,
        "one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve": 123456789012,
        "four decillion": 4000000000000000000000000000000000
    }
    for text, expected in b7.items():
        b8 = fonk2(text.split())
        assert b8 = = expected, f"Test failed for: '{text}', expected: {expected}, got: {b8}"
    print("All test cases passed!")