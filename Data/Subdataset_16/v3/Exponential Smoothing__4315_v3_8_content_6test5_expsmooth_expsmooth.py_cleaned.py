
import numpy as np
import xlwings as xw
@xw.func
def fonk1(b1):
    b1 = list(b1)
    def fonk2(alpha, b1):
        a1 = 0
        b2 = b1[0]
        for i in range(1, len(b1)):
            b2 = alpha * b1[i] + (1 - alpha) * b2
            a1 += (b2 - b1[i]) ** 2
        return a1 / len(b1)
    def fonk3(b1, alpha_range, b3 = 0.001):
        b4 = np.arange(alpha_range[0], alpha_range[1], b3)
        b5 = [fonk2(alpha, b1) for alpha in b4]
        b6 = np.argmin(b5)
        return b4[b6]
    b7 = np.arange(0.1, 2.0, 0.1)
    b8 = [fonk2(alpha, b1) for alpha in b7]
    b9 = b7[np.argmin(b8)]
    b10 = (max(0, b9 - 0.2), b9 + 0.2)
    b11 = fonk3(b1, b10)
    b2 = b1[0]
    for i in range(1, len(b1)):
        b2 = b11 * b1[i] + (1 - b11) * b2
    return b2
if b12 = = '__main__':
    xw.Book().set_mock_caller()
    fonk1()