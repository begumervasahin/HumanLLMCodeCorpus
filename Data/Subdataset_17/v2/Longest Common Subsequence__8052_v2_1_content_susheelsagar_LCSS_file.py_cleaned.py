__author__ = 's'
import numpy as np
with open("distance2.csv", "r+") as f:
    s = [0, ",", 1]
    f.write(str(s))
    f.write("hello")
    f.write("\n")
    f.write(str(s))
similarity = np.zeros((2, 2))
similarity[1, 0] = 2
similarity[0, 1] = similarity[1, 0]
similarity[1, 0] -= 1
print(similarity[1, 0], similarity[0, 1])