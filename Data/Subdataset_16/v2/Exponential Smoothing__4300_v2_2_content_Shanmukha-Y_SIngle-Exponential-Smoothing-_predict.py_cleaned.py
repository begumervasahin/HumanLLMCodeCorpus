import matplotlib.pyplot as plt
def fonk1(b7):
    with open(b7, 'r') as file:
        b1 = list(map(float, file.read().strip().split("\n")))
    return b1
def fonk2(b1, a1):
    b2 = [b1[0], b1[1]]
    for i in range(2, len(b1)):
        b3 = a1 * b1[i - 1] + (1 - a1) * b2[i - 2]
        b2.append(round(b3, 3))
    return b2
def fonk3(b1, b2):
    b4 = sum(abs(b1[i] - b2[i]) for i in range(len(b1)))
    b5 = b4 / len(b1)
    return b5
def fonk4(original_data, b2):
    plt.plot(original_data, b6 = "blue", label="Original Data")
    plt.plot(b2, b6 = "red", label="Smoothed Data")
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Original vs Smoothed Data')
    plt.show()
def fonk5():
    b7 = "b1.txt"
    a1 = 0.98
    b1 = fonk1(b7)
    b2 = fonk2(b1, a1)
    b5 = fonk3(b1, b2)
    print(f"Mean Absolute Error: {b5}")
    fonk4(b1, b2)
if b8 = = "__main__":
    fonk5()