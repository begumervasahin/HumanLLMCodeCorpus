b1 = 'b3'
import numpy as np
b2 = open("distance2.csv", "r+")
b3 = []
b3.append(0)
b3.append(",")
b3.append(1)
b2.write(str(b3))
b2.write("hello")
b2.write("\n")
b2.write(str(b3))
b4 = np.zeros((2, 2))
b4[1][0] = 2
b4[0][1] = b4[1][0]
b4[1][0] -= 1
print(b4[1][0], b4[0][1])
b2.close()