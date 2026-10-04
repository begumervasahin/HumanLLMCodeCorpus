from itertools import combinations
def fonk1(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])
def fonk2(of_length):
    b1 = ['hello', 'world', 'apple', 'lemon', 'peach']
    return [word.encode('utf-8') for word in b1 if len(word) == of_length]
def fonk3():
    b2 = b'\x0b\x0e\x1e\x0b\x17'
    b3 = b'\x15\x0a\x1b\x1d\x01'
    b4 = fonk2(of_length=len(b2))
    b5 = combinations(b4, r=2)
    for word1, word2 in b5:
        b6 = fonk1(word1, word2)
        print(f'Word 1: {word1}, Word 2: {word2}, XOR Result: {b6}')
if b7 = = "__main__":
    fonk3()