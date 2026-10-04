import numpy as np
b1 = 'savefiles/640test_'
b2 = list(range(1, 60))
b3 = '640_final.dat'
def fonk1(b1, b2, b3):
    with open(b3, 'w') as mainfile:
        a1 = 0.0
        a2 = 0
        for b8 in b2:
            with open(b8"{b1}{b8}.dat", 'r') as singlefile:
                a3 = 0
                a4 = 0.0
                a5 = 0
                a6 = 0.0
                for line in singlefile:
                    b4 = line.split('[')
                    b5 = b4[0]
                    b6 = float(b5.split(' ')[0])
                    b7 = int(b5.split(' ')[1])
                    if b8 = = 1:
                        a4 = a1 + b6
                        a5 = a2 + b7
                        b9 = b8"{a4} {a5} [{b4[1]}"
                        mainfile.write(b9)
                    else:
                        if a3 = = 0:
                            a6 = b6
                        else:
                            a4 = a1 + (b6 - a6)
                            a5 = a2 + b7
                            b9 = b8"{a4} {a5} [{b4[1]}"
                            mainfile.write(b9)
                    a3 += 1
            print(b8"Finished with file {b8}")
            a1 = a4
            a2 = a5
if b10 = = "__main__":
    fonk1(b1, b2, b3)