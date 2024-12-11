import numpy as np
with open("distance2.csv", "w+") as f:
    b1 = [0, ",", 1]
    f.write(str(b1))
    f.write("hello\n")
    f.write(str(b1))
    b2 = np.zeros((2, 2))
    b2[1][0] = 2
    b2[0][1] = b2[1][0]
    b2[1][0] -= 1
    print(b2[1][0], b2[0][1])