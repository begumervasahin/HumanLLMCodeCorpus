import numpy as np
b1 = 'savefiles/640test_'
b2 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
    44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
]
def fonk1(line, a1, b14, b3 = 0.0):
    b4 = line.split('[')
    b5 = b4[0].split()
    b6 = float(b5[0])
    b7 = int(b5[1])
    b8 = a1 + (b6 - b3)
    b9 = b14 + b7
    b10 = f'{b8} {b9} [{'['.join(b4[1:])}'
    return b10, b8, b9
def fonk2(b12, a1, b14):
    with open(f'{b1}{b12}.dat', 'r') as file:
        b11 = file.readlines()
        if b12 = = 1:
            b3 = 0.0
        else:
            b13 = b11[0].split('[')[0].split()
            b3 = float(b13[0])
        for i, line in enumerate(b11):
            if b12 = = 1 or i >= 1:
                b10, b8, b9 = fonk1(line, a1, b14, b3)
                yield b10, b8, b9
                a1, b14 = b8, b9
def fonk3():
    a1 = 0.0
    b14 = 0
    with open('640_final.dat', 'w') as mainfile:
        for b12 in b2:
            for b10, b8, b9 in fonk2(b12, a1, b14):
                mainfile.write(b10)
                a1, b14 = b8, b9
            print(f"Finished with file {b12}")
if b15 = = "__main__":
    fonk3()