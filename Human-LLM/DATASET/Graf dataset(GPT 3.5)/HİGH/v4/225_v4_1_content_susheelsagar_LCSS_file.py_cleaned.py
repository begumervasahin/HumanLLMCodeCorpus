import numpy as np
b1 = open("distance2.csv", "r+")
b2 = [0, ",", 1]
b1.write(str(b2))
b1.write("hello\n")
b1.write(str(b2))
b3 = np.zeros((2, 2))
b3[1][0] = 2
b3[0][1] = b3[1][0]
b3[1][0] -= 1
print(b3[1][0], b3[0][1])
b1.close()