
import numpy as np
from matplotlib import pyplot as plt
def fonk1(a1, s):
    b1 = np.zeros(s.shape)
    b1[0] = s[0]
    for i in range(1, len(b1)):
        b1[i] = a1*s[i]+(1-a1)*b1[i-1]
    return b1
def fonk2(b26, b6, b8, b16, b25):
    year, time_id, b2 = b8.T
    plt.figure(b3 = (14, 6), dpi=80)
    plt.plot(year, b2, b4 = 'blue', label="actual value")
    plt.plot(b26[1:], b16[2:],
             b4 = 'red', label="double predicted value")
    plt.plot(b26[1:], b25[2:],
             b4 = 'green', label="triple predicted value")
    plt.legend(b5 = 'lower right')
    plt.title('Projects')
    plt.xlabel('year')
    plt.ylabel('b2')
    plt.xticks(b26)
    plt.show()
def fonk3():
    a1 = .70
    b6 = np.array([2016, 2017])
    b7 = r'data1.txt'
    b8 = np.loadtxt(b7)
    year, time_id, b2 = b8.T
    b9 = np.array([0, 0, b2[0]])
    b10 = np.insert(b8, 0, values=b9, b20=0)
    initial_year, initial_time_id, b11 = b10.T
    b12 = fonk1(a1, b11)
    b13 = fonk1(a1, b12)
    b14 = 2*b12-b13
    b15 = (a1/(1-a1))*(b12-b13)
    b16 = np.zeros(b13.shape)
    for i in range(1, len(initial_time_id)):
        b16[i] = b14[i-1]+b15[i-1]
    b17 = b14[-1]+b15[-1]*1
    b18 = b14[-1]+b15[-1]*2
    b19 = np.array([b17, b18])
    b16 = np.insert(b16, len(b16), values=np.array(
        [b17, b18]), b20 = 0)
    b21 = fonk1(a1, b13)
    b22 = 3*b12-3*b13+b21
    b23 = (a1/(2*((1-a1)**2)))*((6-5*a1)*b12 -
                                           2*((5-4*a1)*b13)+(4-3*a1)*b21)
    b24 = ((a1**2)/(2*((1-a1)**2)))*(b12-2*b13+b21)
    b25 = np.zeros(b21.shape)
    for i in range(1, len(initial_time_id)):
        b25[i] = b22[i-1]+b23[i-1]*1 + b24[i-1]*(1**2)
    b17 = b22[-1]+b23[-1]*1 + b24[-1]*(1**2)
    b18 = b22[-1]+b23[-1]*2 + b24[-1]*(2**2)
    b19 = np.array([b17, b18])
    b25 = np.insert(b25, len(b25), values=np.array(
        [b17, b18]), b20 = 0)
    b26 = np.insert(year, len(year), values=b6, b20=0)
    b27 = np.array([b26, b16, b25])
    print(b27)
    fonk2(b26, b6, b8, b16, b25)
if b28 = = '__main__':
    fonk3()