import random
import math
import statistics
import pylab
def fonk1(b1, a):
    if b1 = = 0:
        return 1
    return a * fonk1(b1-1, a) / (b1 + a*fonk1(b1-1, a))
def fonk2(s, a):
    assert s > a
    return (s * fonk1(s, a)) / (s - a*(1 - fonk1(s, a)))
def fonk3(arrival_rate):
    return -(1 / arrival_rate) * math.log(1 - random.random())
def fonk4(avg_service_time):
    return -(avg_service_time) * math.log(1 - random.random())
def fonk5(server_status):
    b2 = min(server_status)
    b3 = server_status.index(b2)
    return b3, b2
def fonk6(t, b8):
    b4 = [1 if el/t > 1 else 0 for el in b8]
    b5 = sum(b4)/len(b4)
    return b5
def fonk7(b6 = 1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    b7 = [0 for _ in range(S)]
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b8 = []
    for _ in range(b6):
        b9 = fonk3(arrival_rate)
        a1 += b9
        a5 = 0
        while a1 < b7[a5]:
            a5 += 1
            if a5 = = S:
                a2 += 1
                a5, b10 = fonk5(b7)
                b11 = b10 - a1
                b8.append(b11)
                a3 += b11
                b12 = fonk4(avg_service_time)
                a4 += b12
                b7[a5] = b10 + b12
                break
        else:
            b8.append(0)
            b12 = fonk4(avg_service_time)
            a4 += b12
            b7[a5] = a1 + b12
    b13 = statistics.mean(b8)
    print(f'Statistical mean of wait times: {b13}')
    b14 = (1/avg_service_time)*sum(b8) / len(b8)
    b15 = (a4/a1)
    print(f'Simulation carried load: {b15}')
    b16 = b15/10
    print(f'Simulation Server utilization, b16: {b16}')
    assert (len(b8) - a2) == a2
    print(f'Simulation E(b11) per unit time: {b14}')
    print(f'a3/a1: {a3/a1}')
    print(f'a2/b6: {a2/b6}')
    b17 = [a2/b6]
    for t in range(1, 9):
        b18 = fonk6(t, b8)
        b17.append(b18)
        print(f'Probability b11 > {t}: {b18}')
if b19 = = '__main__':
    random.seed(123)
    print(fonk7())