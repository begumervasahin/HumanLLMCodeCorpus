import random
import math
import statistics
import matplotlib.pyplot as plt
def fonk1(b1, a):
    if b1 = = 0:
        return 1
    b2 = fonk1(b1 - 1, a)
    return (a * b2) / (b1 + a * b2)
def fonk2(s, a):
    assert s > a, "Number of servers must be greater than the offered load"
    b3 = fonk1(s, a)
    return (s * b3) / (s - a * (1 - b3))
def fonk3(arrival_rate):
    return -math.log(1 - random.random()) / arrival_rate
def fonk4(avg_service_time):
    return -avg_service_time * math.log(1 - random.random())
def fonk5(b7):
    b4 = min(b7)
    b5 = b7.index(b4)
    return b5, b4
def fonk6(t, b8):
    return sum(1 for wt in b8 if wt > t) / len(b8)
def fonk7(b6 = 1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    b7 = [0] * S
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b8 = []
    a5 = 0
    for _ in range(b6):
        b9 = fonk3(arrival_rate)
        a1 += b9
        server_index, b10 = fonk5(b7)
        if a1 < b10:
            a2 += 1
            b11 = b10 - a1
            b8.append(b11)
            a3 += b11
        else:
            a5 += 1
            b8.append(0)
            b11 = 0
        b12 = fonk4(avg_service_time)
        a4 += b12
        b7[server_index] = a1 + b11 + b12
    b13 = statistics.mean(b8)
    b14 = sum(b8) / (len(b8) * avg_service_time)
    b15 = a4 / a1
    b16 = arrival_rate * avg_service_time * (1 - fonk1(S, arrival_rate * avg_service_time))
    b17 = b15 / S
    b18 = arrival_rate * avg_service_time / S
    print(f'Statistical mean of wait times: {b13}')
    print(f'Simulation carried load: {b15}')
    print(f'Theoretical loss system carried load: {b16}')
    print(f'Simulation server b17 (RHO): {b17}')
    print(f'Theoretical delay system rho: {b18}')
    print(f'Simulation E(W) per unit time: {b14}')
    print(f'AB/A: {a3 / a1}')
    print(f'K/b6: {a2 / b6}')
    b19 = [a2 / b6]
    for t in range(1, 9):
        b20 = fonk6(t * avg_service_time, b8)
        b19.append(b20)
        print(f'Probability W > {t * avg_service_time}: {b20}')
    b21 = []
    for t in range(9):
        b22 = t * avg_service_time
        b23 = fonk2(S, arrival_rate * avg_service_time) * math.exp(-1 * (1 - b18) * S * (1 / avg_service_time) * b22)
        b21.append(b23)
        print(f'Theory delay system probability wait greater than {b22} time units: {b23}')
    return b19, b21
def fonk8(b19, b21):
    b24 = list(range(9))
    b25 = [0.85967, 0.574334, 0.38659, 0.265105, 0.178798, 0.119471, 0.081273, 0.056299, 0.03944]
    b26 = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    plt.plot(b24, b21, b27 = 'lightblue', linewidth=3, label='Theory Probs')
    plt.scatter(b24, b25, b27 = 'darkgreen', marker='b24', label='Sim Case 1')
    plt.scatter(b24, b26, b27 = 'red', marker='o', label='Sim Case 2')
    plt.title('P(W > t) vs t')
    plt.ylabel('P(W > t)')
    plt.xlabel('t (in units of avg service time)')
    plt.legend()
    plt.show()
if b28 = = '__main__':
    random.seed(123)
    b19, b21 = fonk7()
    fonk8(b19, b21)