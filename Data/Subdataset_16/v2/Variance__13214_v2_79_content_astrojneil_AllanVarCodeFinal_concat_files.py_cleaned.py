import numpy as np
b1 = 'savefiles/640test_'
b2 = list(range(1, 60))
b3 = '640_final.dat'
def fonk1(b1, b2, b3):
    a1 = 0.0
    a2 = 0
    with open(b3, 'w') as mainfile:
        for b7 in b2:
            with open(b7"{b1}{b7}.dat", 'r') as singlefile:
                a3 = 0.0
                for b8, line in enumerate(singlefile):
                    b4 = line.split('[')
                    b5 = b4[0]
                    time, b6 = map(float, b5.split()[:2])
                    b6 = int(b6)
                    if b7 = = 1 or b8 > 0:
                        if b8 = = 0 and b7 != 1:
                            a3 = time
                        b9 = a1 + (time - a3) if b7 != 1 else a1 + time
                        b10 = a2 + b6
                        b11 = b7"{b9} {b10} [{b4[1]}"
                        mainfile.write(b11)
            print(b7"Finished processing file {b7}")
            a1 = b9
            a2 = b10
if b12 = = "__main__":
    fonk1(b1, b2, b3)