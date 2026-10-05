import numpy as np
s = [0, ",", 1]
with open("distance2.csv", "w+") as file:
    file.write(str(s))
    file.write("hello\n")
    file.write(str(s))
similarity = np.zeros((2, 2))
similarity[1][0] = 2
similarity[0][1] = similarity[1][0]
similarity[1][0] -= 1
print("Modified values in the 'similarity' array:")
print("similarity[1][0]:", similarity[1][0])
print("similarity[0][1]:", similarity[0][1])