import random
import math
import statistics
import pylab
def fonk1(b1, a):
    if b1 = = 0:
        return 1
    return (a * fonk1(b1 - 1, a)) / (b1 + a * fonk1(b1 - 1, a))
def fonk2(s, a):
    assert s > a, "Number of servers must be greater than the offered load."
    b2 = fonk1(s, a)
    return (s * b2) / (s - a * (1 - b2))
def fonk3(arrival_rate):
    return -(1 / arrival_rate) * math.log(1 - random.random())
def fonk4(avg_service_time):
    return -(avg_service_time) * math.log(1 - random.random())
def fonk5(b8):
    b3 = min(b8)
    b4 = b8.index(b3)
    return b4, b3
def fonk6(t, b9):
    b5 = [1 if el / (t * 2.4) > 1 else 0 for el in b9]
    b6 = sum(b5) / len(b5)
    return b6
def fonk7(b7 = 1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    b8 = [0] * S
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b9 = []
    b10 = []
    for d in range(b7):
        b11 = fonk3(arrival_rate)
        a1 += b11
        a5 = 0
        while a1 < b8[a5]:
            a5 += 1
            if a5 = = S:
                a2 += 1
                a5, b12 = fonk5(b8)
                b13 = b12 - a1
                b9.append(b13)
                a3 += b13
                b14 = fonk4(avg_service_time)
                a4 += b14
                b8[a5] = b12 + b14
                b10.append((d, b11, a1, b13, a5, S))
                break
        else:
            b9.append(0)
            b14 = fonk4(avg_service_time)
            a4 += b14
            b8[a5] = a1 + b14
    b15 = statistics.mean(b9)
    print(f'Statistical mean of b9: {b15}')
    b16 = (1 / avg_service_time) * sum(b9) / len(b9)
    b17 = a4 / a1
    print(f'Simulation carried load: {b17}')
    b18 = (arrival_rate * avg_service_time) * (1 - fonk1(S, arrival_rate * avg_service_time))
    print(f'Theory loss system carried load: {b18}')
    b19 = b17 / S
    print(f'Simulation server utilization, b19: {b19}')
    b20 = (arrival_rate * avg_service_time) / S
    print(f'Theory delay system rho: {b20}')
    print(f'Simulation E(b13) per unit time: {b16}')
    print(f'a3/a1: {a3 / a1}')
    print(f'a2/b7: {a2 / b7}')
    b21 = [a2 / b7]
    for t in range(1, 9):
        b22 = fonk6(t, b9)
        b21.append(b22)
        print(f'Probability b13 > {t}: {b22}')
    b23 = []
    for t in [t * 2.4 for t in range(9)]:
        b24 = fonk2(S, arrival_rate * avg_service_time) * math.exp(-1 * (1 - b20) * S * (1 / avg_service_time) * t)
        b23.append(b24)
        print(f'Theory delay system probability wait greater than {t} time units: {b24}')
    return b10, b21, b23
if b25 = = '__main__':
    random.seed(123)
    b10, sim_case1_probs, b23 = fonk7()
    b26 = list(range(9))
    b27 = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    b28 = pylab.figure()
    b29 = b28.add_subplot()
    b29.plot(b26, b23, b30 = 'lightblue', linewidth=3, label='Theory Probs')
    b29.scatter(b26, sim_case1_probs, b30 = 'darkgreen', marker='b26', label='Sim Case 1 Probs')
    b29.scatter(b26, b27, b30 = 'red', marker='o', label='Sim Case 2 Probs')
    b29.set(b31 = 'Case1: exponential arrivals & service, Case2: const. service time', ylabel='P(b13>t)', xlabel='t')
    b29.legend()
    pylab.show()