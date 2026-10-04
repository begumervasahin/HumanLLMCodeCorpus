b1 = 's'
import numpy as np
def fonk1(filename, b4, b5):
    with open(filename, "r+") as f:
        f.write(str(b4))
        f.write(b5)
        f.write("\n")
        f.write(str(b4))
def fonk2():
    b2 = np.zeros((2, 2))
    b2[1, 0] = 2
    b2[0, 1] = b2[1, 0]
    b2[1, 0] -= 1
    return b2[1, 0], b2[0, 1]
if b3 = = "__main__":
    b4 = [0, ",", 1]
    b5 = "hello"
    fonk1("distance2.csv", b4, b5)
    b6 = fonk2()
    print(b6[0], b6[1])