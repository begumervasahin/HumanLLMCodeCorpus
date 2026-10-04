import sys
def fonk1(b1 = 1):
    b2 = (1 << 31) - 1
    b1 = b1 & b2
    while True:
        b1 = (b1 * 214013 + 2531011) & b2
        yield b1 >> 16
def fonk2(b1):
    a1 = 52
    b3 = list(range(a1 - 1, -1, -1))
    b4 = fonk1(b1)
    for i, r in zip(range(a1), b4):
        b5 = (a1 - 1) - r % (a1 - i)
        b3[i], b3[b5] = b3[b5], b3[i]
    return b3
def fonk3(b3):
    b6 = ["A23456789TJQK"[c
    for i in range(0, len(b3), 8):
        print(" ", " ".join(b6[i: i + 8]))
if b7 = = '__main__':
    b1 = int(sys.argv[1]) if len(sys.argv) == 2 else 11982
    print(f"Hand {b1}")
    b8 = fonk2(b1)
    fonk3(b8)