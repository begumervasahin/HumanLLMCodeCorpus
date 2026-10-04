import numpy as np
b1 = 'savefiles/640test_'
b2 = list(range(1, 60))
b3 = '640_final.dat'
def fonk1(b1, b2, b3):
    a1 = 0.0
    a2 = 0
    with open(b3, 'w') as mainfile:
        for b5 in b2:
            with open(b5"{b1}{b5}.dat", 'r') as singlefile:
                a3 = 0.0
                for b6, line in enumerate(singlefile):
                    time, b10, b4 = fonk2(line)
                    if b5 = = 1 or b6 > 0:
                        if b6 = = 0 and b5 != 1:
                            a3 = time
                        b7 = fonk3(b5, a1, time, a3)
                        b8 = a2 + b10
                        fonk4(mainfile, b7, b8, b4)
            print(b5"Finished processing file {b5}")
            a1, a2 = b7, b8
def fonk2(line):
    b4 = line.split('[')
    b9 = b4[0]
    time, b10 = map(float, b9.split()[:2])
    b10 = int(b10)
    return time, b10, b4[1]
def fonk3(b11, a1, time, a3):
    if b11 = = 1:
        return a1 + time
    return a1 + (time - a3)
def fonk4(file, b7, b8, b4):
    b12 = b5"{b7} {b8} [{b4}"
    file.write(b12)
if b13 = = "__main__":
    fonk1(b1, b2, b3)