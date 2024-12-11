import matplotlib.pyplot as plt
b1 = open("b2.txt",'r')
b2 = list(map(float,b1.read().strip().split("\n")))
b3 = [b2[0], b2[1]]
a1 = 0.98
for i in range(2,len(b2)):
    b4 = a1*b2[i-1] + (1-a1)*b3[i-2]
    b3.append(round(b4,3))
a2 = 0
for i in range(len(b2)):
    a2 = a2+abs(b2[i]-b3[i])
a2 = a2/len(b2)
print(a2)
plt.plot(b2,b5 = "blue")
plt.plot(b3,b5 = "red")
plt.show()