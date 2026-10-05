import random
import math
import statistics
import pylab
def fonk1(b1, a):
    if b1 = = 0:
        return 1
    return a * fonk1(b1 - 1, a) / (b1 + a * fonk1(b1 - 1, a))
def fonk2(s, a):
    assert s > a
    return (s * fonk1(s, a)) / (s - a * (1 - fonk1(s, a)))
def fonk3(arrival_rate):
    return -(1 / arrival_rate) * math.log(1 - random.random())
def fonk4(avg_service_time):
    return -(avg_service_time) * math.log(1 - random.random())
def fonk5(server_status):
    b2 = min(server_status)
    b3 = server_status.index(b2)
    return b3, b2
def fonk6(t, b8):
    b4 = [1 if el / (t * 2.4) > 1 else 0 for el in b8]
    b5 = sum(b4) / len(b4)
    return b5
def fonk7(b6 = 1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    b7 = [0] * S
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b8 = []
    b9 = []
    for d in range(b6):
        b10 = fonk3(arrival_rate)
        a1 += b10
        a5 = 0
        while a1 < b7[a5]:
            a5 += 1
            if a5 = = S:
                a2 += 1
                a5, b11 = fonk5(b7)
                b12 = b11 - a1
                b8.append(b12)
                a3 += b12
                b13 = fonk4(avg_service_time)
                a4 += b13
                b7[a5] = b11 + b13
                b9.append((d, b10, a1, b12, a5, S))
                break
        else:
            b8.append(0)
            b13 = fonk4(avg_service_time)
            a4 += b13
            b7[a5] = a1 + b13
    b14 = statistics.mean(b8)
    print(f'statistical mean of b8: {b14}')
    b15 = (1 / avg_service_time) * sum(b8) / len(b8)
    b16 = (a4 / a1)
    print(f'Simulation carried load: {b16}')
    b17 = (arrival_rate * avg_service_time) * (1 - earlang_B(S, arrival_rate * avg_service_time))
    print(f'from theory loss system carried load: {b17}')
    b18 = b16 / 10
    print(f'Simulation Server utilization, b18: {b18}')
    b19 = (arrival_rate * avg_service_time) / S
    print(f'theory delay system rho: {b19}')
    assert (len(b8) - num_cust_no_wait) == a2
    print(f'Simulation E(b12) per unit time: {b15}')
    print(f'a3/a1: {a3 / a1}')
    print(f'a2/b6: {a2 / b6}')
    b20 = [a2 / b6]
    for t in range(1, 9):
        b21 = fonk6(t, b8)
        b20.append(b21)
        print(f'probability b12 > {t}: {b21}')
    b22 = []
    for t in [t * 2.4 for t in range(9)]:
        b23 = fonk2(S, arrival_rate * avg_service_time) * math.exp(
            -1 * (1 - b19) * S * (1 / avg_service_time) * t)
        b22.append(b23)
        print(f'by theory delay system probablity wait greater than {t} time units is: {b23}')
    log(f'b9: {b9}')
if b24 = = '__main__':
    random.seed(123)
    print(fonk7())
    b25 = list(range(9))
    b22 = [0.8590803440134663, 0.5758587757474194, 0.38600968106903694, 0.25875002718439916, 0.17344533013396932,
                    0.11626388168006893, 0.07793401052006589, 0.052240729519552526, 0.035018008216481836]
    b26 = [0.85967, 0.574334, 0.38659, 0.265105, 0.178798, 0.119471, 0.081273, 0.056299, 0.03944]
    b27 = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    b28 = pylab.figure()
    b29 = b28.add_subplot()
    b29.plot(b25, b22, b30 = 'lightblue', linewidth=3)
    b29.scatter(b25, b26, b30 = 'darkgreen', marker='b25')
    b29.scatter(b25, b27, b30 = 'red', marker='o')
    b29.set(b31 = 'Case1: exponential arrivals & service, Case2: const. service time', ylabel='P(b12>t)', xlabel='t')
    handles, b32 = b29.get_legend_handles_labels()
    b29.legend(handles, b32)
    pylab.show()