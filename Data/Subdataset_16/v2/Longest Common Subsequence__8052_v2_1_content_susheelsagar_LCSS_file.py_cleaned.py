b1 = 'b2'
import numpy as np
with open("distance2.csv", "r+") as f:
    b2 = [0, ",", 1]
    f.write(str(b2))
    f.write("hello")
    f.write("\n")
    f.write(str(b2))
b3 = np.zeros((2, 2))
b3[1, 0] = 2
b3[0, 1] = b3[1, 0]
b3[1, 0] -= 1
print(b3[1, 0], b3[0, 1])