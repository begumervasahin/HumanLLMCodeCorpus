import matplotlib.pyplot as plt
with open("data.txt", 'r') as file:
    data = list(map(float, file.read().strip().split("\n")))
alpha = 0.98
smoothed_data = [data[0], data[1]]
for i in range(2, len(data)):
    predicted_value = alpha * data[i - 1] + (1 - alpha) * smoothed_data[i - 2]
    smoothed_data.append(round(predicted_value, 3))
mean_abs_deviation = sum(abs(data[i] - smoothed_data[i]) for i in range(len(data))) / len(data)
print("Mean Absolute Deviation (MAD):", mean_abs_deviation)
plt.plot(data, color="blue", label="Original Data")
plt.plot(smoothed_data, color="red", label="Smoothed Data")
plt.title('Exponential Smoothing')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()