import random
import math
import statistics
import matplotlib.pyplot as plt
def fonk1(b1, a):
    if b1 = = 0:
        return 1
    return (a * fonk1(b1 - 1, a)) / (b1 + a * fonk1(b1 - 1, a))
def fonk2(s, a):
    assert s > a, "Number of servers must be greater than the offered load"
    b2 = fonk1(s, a)
    return (s * b2) / (s - a * (1 - b2))
def fonk3(arrival_rate):
    return -math.log(1 - random.random()) / arrival_rate
def fonk4(avg_service_time):
    return -avg_service_time * math.log(1 - random.random())
def fonk5(b6):
    b3 = min(b6)
    b4 = b6.index(b3)
    return b4, b3
def fonk6(t, b7):
    return sum(1 for wt in b7 if wt > t) / len(b7)
def fonk7(b5 = 1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    b6 = [0] * S
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b7 = []
    a5 = 0
    for _ in range(b5):
        b8 = fonk3(arrival_rate)
        a1 += b8
        a6 = 0
        while a1 < b6[a6]:
            a6 += 1
            if a6 = = S:
                a2 += 1
                a6, b9 = fonk5(b6)
                b10 = b9 - a1
                b7.append(b10)
                a3 += b10
                b11 = fonk4(avg_service_time)
                a4 += b11
                b6[a6] = b9 + b11
                break
        else:
            a5 += 1
            b7.append(0)
            b11 = fonk4(avg_service_time)
            a4 += b11
            b6[a6] = a1 + b11
    b12 = statistics.mean(b7)
    b13 = sum(b7) / (len(b7) * avg_service_time)
    b14 = a4 / a1
    b15 = arrival_rate * avg_service_time * (1 - fonk1(S, arrival_rate * avg_service_time))
    b16 = b14 / S
    b17 = arrival_rate * avg_service_time / S
    print(f'Statistical mean of wait times: {b12}')
    print(f'Simulation carried load: {b14}')
    print(f'Theoretical loss system carried load: {b15}')
    print(f'Simulation server b16 (RHO): {b16}')
    print(f'Theoretical delay system rho: {b17}')
    print(f'Simulation E(W) per unit time: {b13}')
    print(f'AB/A: {a3 / a1}')
    print(f'K/b5: {a2 / b5}')
    b18 = [a2 / b5]
    for t in range(1, 9):
        b19 = fonk6(t * avg_service_time, b7)
        b18.append(b19)
        print(f'Probability W > {t * avg_service_time}: {b19}')
    b20 = []
    for t in [t * avg_service_time for t in range(9)]:
        b21 = fonk2(S, arrival_rate * avg_service_time) * math.exp(-1 * (1 - b17) * S * (1 / avg_service_time) * t)
        b20.append(b21)
        print(f'Theory delay system probability wait greater than {t} time units: {b21}')
    return b18, b20
if b22 = = '__main__':
    random.seed(123)
    b18, b20 = fonk7()
    b23 = list(range(9))
    b24 = [0.85967, 0.574334, 0.38659, 0.265105, 0.178798, 0.119471, 0.081273, 0.056299, 0.03944]
    b25 = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    plt.plot(b23, b20, b26 = 'lightblue', linewidth=3, label='Theory Probs')
    plt.scatter(b23, b24, b26 = 'darkgreen', marker='b23', label='Sim Case 1')
    plt.scatter(b23, b25, b26 = 'red', marker='o', label='Sim Case 2')
    plt.title('P(W > t) vs t')
    plt.ylabel('P(W > t)')
    plt.xlabel('t (in units of avg service time)')
    plt.legend()
    plt.show()