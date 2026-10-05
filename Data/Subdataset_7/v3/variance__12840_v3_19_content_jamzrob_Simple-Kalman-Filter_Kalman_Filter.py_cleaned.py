import math
def fonk1(header_text):
    print("\n" + header_text)
    print("----------------------------------------")
def fonk2(message):
    return float(input(message))
def fonk3(b1, b2, b3, b4):
    return b1 * b3 + b2 * b4
def fonk4(b1, b6, b7, b8):
    return b1 * b6 * b7 + b8
def fonk5(b5, b9, b13, b14, b11):
    return b5 + b13 * (b14 - b11 * b5)
def fonk6(b9, b13, b11):
    return b9 - b13 * b11 * b9
def fonk7():
    fonk1("Prediction Steps")
    b1 = fonk2("A: ")
    b2 = fonk2("B: ")
    b3 = fonk2("Enter Prior Mean: ")
    b4 = fonk2("Enter Current Mean: ")
    b5 = fonk3(b1, b2, b3, b4)
    print("Predicted Mean: ", b5)
    b6 = fonk2("\nE(t-1): ")
    b7 = fonk2("A(T/t): ")
    b8 = fonk2("Q(t): ")
    b9 = fonk4(b1, b6, b7, b8)
    print("Predicted Convariance: ", b9)
    while True:
        fonk1("Update Steps")
        b10 = fonk2("C(T/t): ")
        b11 = fonk2("C/(t): ")
        b12 = fonk2("Measurement Covariance: ")
        b13 = b9 * b10 * math.pow((b11 * b9 * b10 + b12), (-1))
        print("Kalman Gain: ", b13)
        b14 = fonk2("\nActual Measurement: ")
        b15 = fonk5(b5, b9, b13, b14, b11)
        print("Updated Mean: ", b15)
        b16 = fonk6(b9, b13, b11)
        print("\nUpdated Covariance: ", b16)
        fonk1("Prediction Steps")
        b1 = fonk2("A: ")
        b2 = fonk2("B: ")
        b4 = fonk2("Enter Current Mean: ")
        b5 = fonk3(b1, b2, b15, b4)
        print("Predicted Mean: ", b5)
        b7 = fonk2("\nA(T/t): ")
        b8 = fonk2("Q(t): ")
        b9 = fonk4(b1, b16, b7, b8)
        print("Predicted Convariance: ", b9)
fonk7()