import numpy as np
with open("distance2.csv", "w+") as f:
    s = [0, ",", 1]
    f.write(str(s))
    f.write("hello\n")
    f.write(str(s))
    similarity = np.zeros((2, 2))
    similarity[1][0] = 2
    similarity[0][1] = similarity[1][0]
    similarity[1][0] -= 1
    print(similarity[1][0], similarity[0][1])