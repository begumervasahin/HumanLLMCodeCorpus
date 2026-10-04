import numpy as np
b1 = 'savefiles/640test_'
b2 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
    44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
]
with open('640_final.dat', 'w') as mainfile:
    a1 = 0.0
    a2 = 0
    for b7 in b2:
        with open(b7'{b1}{b7}.dat', 'r') as singlefile:
            a3 = 0
            a4 = 0.0
            for line in singlefile:
                b3 = line.split('[')
                b4 = b3[0]
                b5 = float(b4.split()[0])
                b6 = int(b4.split()[1])
                if b7 = = 1 or a3 >= 1:
                    if a3 = = 0 and b7 != 1:
                        a4 = b5
                    b8 = a1 + (b5 - a4 if b7 != 1 else b5)
                    b9 = a2 + b6
                    b10 = b7'{b8} {b9} [{b3[1]}'
                    mainfile.write(b10)
                a3 += 1
        print(b7"Finished with file {b7}")
        a1 = b8
        a2 = b9