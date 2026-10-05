import numpy as np
file = open("distance2.csv", "r+")
data = [0, ",", 1]
file.write(str(data))
file.write("hello\n")
file.write(str(data))
similarity = np.zeros((2, 2))
similarity[1][0] = 2
similarity[0][1] = similarity[1][0]
similarity[1][0] -= 1
print(similarity[1][0], similarity[0][1])
file.close()