import matplotlib.pyplot as plt
def fonk1(file_path):
    with open(file_path, 'r') as file:
        return list(map(float, file.read().strip().split("\n")))
def fonk2(b4, a1):
    b1 = [b4[0], b4[1]]
    for i in range(2, len(b4)):
        b2 = a1 * b4[i - 1] + (1 - a1) * b1[i - 2]
        b1.append(round(b2, 3))
    return b1
def fonk3(original_data, b1):
    return sum(abs(original_data[i] - b1[i]) for i in range(len(original_data))) / len(original_data)
if b3 = = "__main__":
    b4 = fonk1("b4.txt")
    a1 = 0.98
    b1 = fonk2(b4, a1)
    b5 = fonk3(b4, b1)
    print("Mean Absolute Deviation (MAD):", b5)
    plt.plot(b4, b6 = "blue", label="Original Data")
    plt.plot(b1, b6 = "red", label="Smoothed Data")
    plt.title('Exponential Smoothing')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()