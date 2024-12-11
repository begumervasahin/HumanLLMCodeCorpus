import numpy as np
with open("distance2.csv", "r+") as file:
    b1 = [0, ",", 1]
    file.write(str(b1))
    file.write("hello\n")
    file.write(str(b1))
    b2 = np.zeros((2, 2))
    b2[1][0] = 2
    b2[0][1] = b2[1][0]
    b2[1][0] -= 1
    print("Modified values:", b2[1][0], b2[0][1])