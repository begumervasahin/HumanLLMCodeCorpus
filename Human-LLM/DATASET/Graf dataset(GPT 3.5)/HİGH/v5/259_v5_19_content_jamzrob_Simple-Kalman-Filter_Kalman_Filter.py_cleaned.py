import math
def fonk1(prompt, b1 = float):
    return b1(input(prompt))
def fonk2(b3, b5, b4, b6):
    return b3 * b5 + b4 * b6
def fonk3(b3, b8, b9, b10):
    return b3 * b8 * b9 + b10
def fonk4(b11, b12, b13, b14):
    b2 = (b13 * b11 * b12 + b14)
    if b2 = = 0:
        return 0
    return b11 * b12 / b2
def fonk5(b7, b15, b16, b13):
    return b7 + b15 * (b16 - b13 * b7)
def fonk6(b11, b15, b13):
    return b11 - b15 * b13 * b11
def fonk7():
    print("\nPrediction Steps")
    print("----------------------------------------")
    b3 = fonk1("A: ")
    b4 = fonk1("B: ")
    b5 = fonk1("Enter Prior Mean: ")
    b6 = fonk1("Enter Current Mean: ")
    b7 = fonk2(b3, b5, b4, b6)
    print("Predicted Mean: ", b7)
    b8 = fonk1("\nE(t-1): ")
    b9 = fonk1("A(T/t): ")
    b10 = fonk1("Q(t): ")
    b11 = fonk3(b3, b8, b9, b10)
    print("Predicted Covariance: ", b11)
    while True:
        print("\nUpdate Steps")
        print("----------------------------------------")
        b12 = fonk1("C(T/t): ")
        b13 = fonk1("C/(t): ")
        b14 = fonk1("Measurement Covariance: ")
        b15 = fonk4(b11, b12, b13, b14)
        print("Kalman Gain: ", b15)
        b16 = fonk1("\nActual Measurement: ")
        b17 = fonk5(b7, b15, b16, b13)
        print("Updated Mean: ", b17)
        b18 = fonk6(b11, b15, b13)
        print("\nUpdated Covariance: ", b18)
        print("\nPrediction Steps")
        print("----------------------------------------")
        b3 = fonk1("A: ")
        b4 = fonk1("B: ")
        b6 = fonk1("Enter Current Mean: ")
        b7 = fonk2(b3, b17, b4, b6)
        print("Predicted Mean: ", b7)
        b9 = fonk1("\nA(T/t): ")
        b10 = fonk1("Q(t): ")
        b11 = fonk3(b3, b18, b9, b10)
        print("Predicted Covariance: ", b11)
if b19 = = "__main__":
    fonk7()