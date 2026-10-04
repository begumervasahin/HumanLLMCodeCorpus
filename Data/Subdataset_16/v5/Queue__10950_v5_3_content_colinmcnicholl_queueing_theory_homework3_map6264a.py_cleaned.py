import random
import math
import statistics
import pylab
def fonk1(b1, a):
    if b1 = = 0:
        return 1
    b2 = fonk1(b1 - 1, a)
    return (a * b2) / (b1 + a * b2)
def fonk2(s, a):
    assert s > a, "Number of servers must be greater than the offered load."
    b3 = fonk1(s, a)
    return (s * b3) / (s - a * (1 - b3))
def fonk3(arrival_rate):
    return -(1 / arrival_rate) * math.log(1 - random.random())
def fonk4(avg_service_time):
    return -(avg_service_time) * math.log(1 - random.random())
def fonk5(b7):
    b4 = min(b7)
    b5 = b7.index(b4)
    return b5, b4
def fonk6(t, b8):
    return sum(1 if wait > t else 0 for wait in b8) / len(b8)
def fonk7(b6 = 1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    b7 = [0] * S
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b8 = []
    for _ in range(b6):
        b9 = fonk3(arrival_rate)
        a1 += b9
        b10 = next((i for i, status in enumerate(b7) if status <= a1), None)
        if b10 is None:
            a2 += 1
            b10, b11 = fonk5(b7)
            b12 = b11 - a1
            b8.append(b12)
            a3 += b12
            b13 = fonk4(avg_service_time)
            a4 += b13
            b7[b10] = b11 + b13
        else:
            b8.append(0)
            b13 = fonk4(avg_service_time)
            a4 += b13
            b7[b10] = a1 + b13
    b14 = statistics.mean(b8)
    b15 = a4 / a1
    b16 = (arrival_rate * avg_service_time) * (1 - fonk1(S, arrival_rate * avg_service_time))
    b17 = b15 / S
    b18 = (arrival_rate * avg_service_time) / S
    b19 = (1 / avg_service_time) * sum(b8) / len(b8)
    print(f'Statistical mean of wait times: {b14}')
    print(f'Simulation carried load: {b15}')
    print(f'Theory loss system carried load: {b16}')
    print(f'Simulation server b17 (RHO): {b17}')
    print(f'Theory delay system b17 (RHO): {b18}')
    print(f'Simulation average wait time per unit time: {b19}')
    print(f'Total blocked calls ratio (K/b6): {a2 / b6}')
    b20 = [a2 / b6]
    for t in range(1, 9):
        b21 = fonk6(t, b8)
        b20.append(b21)
        print(f'Probability W > {t}: {b21}')
    b22 = []
    for t in [t * avg_service_time for t in range(9)]:
        b23 = fonk2(S, arrival_rate * avg_service_time) * math.exp(-1 * (1 - b18) * S * (1 / avg_service_time) * t)
        b22.append(b23)
        print(f'Theory delay system probability wait greater than {t} time units: {b23}')
    return b20, b22
def fonk8(b20, b22):
    b24 = list(range(9))
    b25 = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    fig, b26 = pylab.subplots()
    b26.plot(b24, b22, b27 = 'lightblue', linewidth=3, label='Theory Probs')
    b26.scatter(b24, b20, b27 = 'darkgreen', marker='b24', label='Sim Case 1 Probs')
    b26.scatter(b24, b25, b27 = 'red', marker='o', label='Sim Case 2 Probs')
    b26.set(b28 = 'Case1: exponential arrivals & service, Case2: const. service time', ylabel='P(W>t)', xlabel='t')
    b26.legend()
    pylab.show()
if b29 = = '__main__':
    random.seed(123)
    b20, b22 = fonk7()
    fonk8(b20, b22)