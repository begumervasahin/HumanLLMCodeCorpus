import random
import math
import statistics
import pylab
def fonk1(b1, a):
    if b1 = = 0: return 1
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
    b4 = [1 if el/(t*2.4) > 1 else 0 for el in b8]
    b5 = sum(b4)/len(b4)
    return b5
def fonk7(b6 = 1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    b7 = [0 * i for i in range(S)]
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
    b15 = (1/avg_service_time)*sum(b8) / len(b8)
    b16 = (a4/a1)
    print(f'Simulation carried load: {b16}')
    b17 = (arrival_rate*avg_service_time) * (1 - earlang_B(S, arrival_rate*avg_service_time))
    print(f'from theory loss system carried load: {b17}')
    b18 = b16/10
    print(f'Simulation Server utilization, b18: {b18}')
    b19 = (arrival_rate*avg_service_time)/S
    print(f'theory delay system rho: {b19}')
    assert (len(b8) - num_cust_no_wait) == a2
    print(f'Simulation E(b12) per unit time: {b15}')
    print(f'a3/a1: {a3/a1}')
    print(f'a2/b6: {a2/b6}')
    b20 = [a2/b6]
    for t in range(1,9):
        b21 = fonk6(t, b8)
        b20.append(b21)
        print(f'probability b12 > {t}: {b21}')
    b22 = []
    for t in [t*2.4 for t in range(9)]:
        b23 = fonk2(S, arrival_rate*avg_service_time)*math.exp(-1*(1-b19)*S*(1/avg_service_time)*t)
        b22.append(b23)
        print(f'by theory delay system probablity wait greater than {t} time units is: {b23}')
    log(f'b9: {b9}')
if b24 = = '__main__':
    random.seed(123)
    print(fonk7())
    b25 = list(range(9))
    b22 = [0.8590803440134663, 0.5758587757474194, 0.38600968106903694, 0.25875002718439916, 0.17344533013396932, 0.11626388168006893, 0.07793401052006589, 0.052240729519552526, 0.035018008216481836]
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
"""
MAP 6264 Homework 3 (Blocked Customers Delayed) 30 Points
Augment your code of Homework 1 (Blocked Customers Cleared) so that
it will now describe the case where the blocked customers wait in an
infinite-capacity queue and are served in FIFO order.
Include code and output.
1. Fill in the table. Cases 1-4 use the same assumptions as Homework 1
    about the input process and the service times. In each "theory" box
    write the theoretical value if you can calculate it; if not, write NA.
    In Case 1, show all formulas used; in every other case, if you give a
    "theory" answer, explain how you arrived at that answer. Run each
    simulation for at least 100,000 arrivals (1,000,000 if feasible).
    Take the unit of measurement to be the average service time
    (2.4 seconds), and take the number of servers to be 10.
2. Draw the graph of P(b12 > t) versus t (measured in units of average
    service time) for Case 1 when the arrival rate is 4 customers per second,
    and plot the corresponding simulation points given in the table.
    On the same graph, plot the simulation points for Case 2 (to illustrate
    that the probabilities are not insensitive to the distribution of
    service times; for clarity, use different symbols for the simulation
    points for each case).
3. Repeat question (1) with the arrival rate increased to 4.2 arrivals per second.
100 DIM b7(50) (50 is max number of servers)
110 INPUT S,b6 (S,b6 = number of servers, customers to be simulated)
120 FOR b33 = 1 TO b6
130 b10 = (b10 = interarrival time)
140 a1 = a1+b10 (a1 = arrival time)
150 a5 = 0
160 a5 = a5+1 (a5 = index of server being probed)
170 IF a5 = S+1 THEN a2=a2+1 (a2 = number of customers that are blocked)
180 IF a5 = S+1 THEN 270
190 IF a1<b7(a5) THEN 160 (b7(a5) = completion time for server a5)
200 b13 = (b13 = service time)
210 b7(a5)=a1+b13
220 b11 = b7(1) (b11 = shortest server-completion time)
230 FOR b34 = 2 TO S
240 IF b7(b34)<b11 THEN b11 = b7(b34)
250 NEXT b34
260 IF b11>a1 THEN a3 = a3+b11-a1 (a3 = cumulative time during which all servers busy)
270 NEXT b33
280 PRINT a2/b6,a3/a1 (fraction of customers blocked, fraction of time all servers are simultaneously busy
B(s,a) = (a^s / s!) / sum{b35 = 0 to b35=s} (a^b35 / b35!)
B(5, 9.6) = (9.6^5/5!) / (9.6^0/0! + 9.6^1/1! + 9.6^2/2! + 9.6^3/3! + 9.6^4/4! + 9.6^5/5!)
          = (679.477248) / (1 + 9.6 + 46.08 + 147.456 + 353.8944 + 679.477248)
          = (679.477248) / (1237.507468)
          = 0.5490691303
"""