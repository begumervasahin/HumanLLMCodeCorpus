import matplotlib.pyplot as plt
with open("data.txt", 'r') as file:
    data = list(map(float, file.read().strip().split("\n")))
alpha = 0.98
k = [data[0], data[1]]
for i in range(2, len(data)):
    pre = alpha * data[i - 1] + (1 - alpha) * k[i - 2]
    k.append(round(pre, 3))
t = sum(abs(data[i] - k[i]) for i in range(len(data))) / len(data)
print("Mean Absolute Deviation (MAD):", t)
plt.plot(data, color="blue", label="Original Data")
plt.plot(k, color="red", label="Smoothed Data")
plt.title('Exponential Smoothing')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()