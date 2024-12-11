import math
def fonk1():
    print("\nPrediction Steps")
    print("----------------------------------------")
    b1 = float(input("A: "))
    b2 = float(input("B: "))
    b3 = float(input("Enter Prior Mean: "))
    b4 = float(input("Enter Current Mean: "))
    b5 = b1 * b3 + b2 * b4
    print("Predicted Mean: ", b5)
    b6 = float(input("\nE(t-1): "))
    b7 = float(input("A(T/t): "))
    b8 = float(input("Q(t): "))
    b9 = b1 * b6 * b7 + b8
    print("Predicted Covariance: ", b9)
    while True:
        print("\nUpdate Steps")
        print("----------------------------------------")
        b10 = float(input("C(T/t): "))
        b11 = float(input("C/(t): "))
        b12 = float(input("Measurement Covariance: "))
        b13 = b9 * b10 * math.pow((b11 * b9 * b10 + b12), (-1))
        print("Kalman Gain: ", b13)
        b14 = float(input("\nActual Measurement: "))
        b15 = b5 + b13 * (b14 - b11 * b5)
        print("Updated Mean: ", b15)
        b16 = b9 - b13 * b11 * b9
        print("\nUpdated Covariance: ", b16)
        print("\nPrediction Steps")
        print("----------------------------------------")
        b1 = float(input("A: "))
        b2 = float(input("B: "))
        b4 = float(input("Enter Current Mean: "))
        b5 = b1 * b15 + b2 * b4
        print("Predicted Mean: ", b5)
        b7 = float(input("\nA(T/t): "))
        b8 = float(input("Q(t): "))
        b9 = b1 * b16 * b7 + b8
        print("Predicted Covariance: ", b9)
if b17 = = "__main__":
    fonk1()