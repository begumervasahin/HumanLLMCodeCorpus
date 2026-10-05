import matplotlib.pyplot as plt
with open("b1.txt", 'r') as file:
    b1 = [float(line) for line in file]
a1 = 0.98
b2 = [b1[0], b1[1]]
for i in range(2, len(b1)):
    b3 = a1 * b1[i - 1] + (1 - a1) * b2[i - 2]
    b2.append(round(b3, 3))
b4 = sum(abs(b1[i] - b2[i]) for i in range(len(b1))) / len(b1)
print("Mean Absolute Deviation (MAD):", b4)
plt.plot(b1, b5 = "blue", label="Original Data")
plt.plot(b2, b5 = "red", label="Smoothed Data")
plt.title('Exponential Smoothing')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()