import random
import math
import statistics
import matplotlib.pyplot as plt
def earlang_B_rec(n, a):
    if n == 0:
        return 1
    return (a * earlang_B_rec(n - 1, a)) / (n + a * earlang_B_rec(n - 1, a))
def earlang_C(s, a):
    assert s > a, "Number of servers must be greater than the offered load"
    B = earlang_B_rec(s, a)
    return (s * B) / (s - a * (1 - B))
def get_inter_arrival_time(arrival_rate):
    return -math.log(1 - random.random()) / arrival_rate
def get_service_time(avg_service_time):
    return -avg_service_time * math.log(1 - random.random())
def first_available_server_and_time(server_status):
    min_time = min(server_status)
    next_avail_server = server_status.index(min_time)
    return next_avail_server, min_time
def prob_wait_greater_than(t, wait_times):
    return sum(1 for wt in wait_times if wt > t) / len(wait_times)
def run_simulation(NSTOP=1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    C = [0] * S
    A = 0
    K = 0
    AB = 0
    SX = 0
    wait_times = []
    num_cust_no_wait = 0
    for _ in range(NSTOP):
        IA = get_inter_arrival_time(arrival_rate)
        A += IA
        J = 0
        while A < C[J]:
            J += 1
            if J == S:
                K += 1
                J, M = first_available_server_and_time(C)
                W = M - A
                wait_times.append(W)
                AB += W
                X = get_service_time(avg_service_time)
                SX += X
                C[J] = M + X
                break
        else:
            num_cust_no_wait += 1
            wait_times.append(0)
            X = get_service_time(avg_service_time)
            SX += X
            C[J] = A + X
    mean_wait_time = statistics.mean(wait_times)
    average_wait_time_per_unit_time = sum(wait_times) / (len(wait_times) * avg_service_time)
    carried_load = SX / A
    theory_loss_system_carried_load = arrival_rate * avg_service_time * (1 - earlang_B_rec(S, arrival_rate * avg_service_time))
    RHO = carried_load / S
    theory_delay_system_rho = arrival_rate * avg_service_time / S
    print(f'Statistical mean of wait times: {mean_wait_time}')
    print(f'Simulation carried load: {carried_load}')
    print(f'Theory loss system carried load: {theory_loss_system_carried_load}')
    print(f'Simulation server utilization (RHO): {RHO}')
    print(f'Theory delay system rho: {theory_delay_system_rho}')
    print(f'Simulation E(W) per unit time: {average_wait_time_per_unit_time}')
    print(f'AB/A: {AB / A}')
    print(f'K/NSTOP: {K / NSTOP}')
    sim_probs = [K / NSTOP]
    for t in range(1, 9):
        prob = prob_wait_greater_than(t * avg_service_time, wait_times)
        sim_probs.append(prob)
        print(f'Probability W > {t * avg_service_time}: {prob}')
    theory_probs = []
    for t in [t * avg_service_time for t in range(9)]:
        prob_wait_greater_than_t = earlang_C(S, arrival_rate * avg_service_time) * math.exp(-1 * (1 - theory_delay_system_rho) * S * (1 / avg_service_time) * t)
        theory_probs.append(prob_wait_greater_than_t)
        print(f'Theory delay system probability wait greater than {t} time units: {prob_wait_greater_than_t}')
    return sim_probs, theory_probs
if __name__ == '__main__':
    random.seed(123)
    sim_probs, theory_probs = run_simulation()
    x = list(range(9))
    sim_case1_probs = [0.85967, 0.574334, 0.38659, 0.265105, 0.178798, 0.119471, 0.081273, 0.056299, 0.03944]
    sim_case2_probs = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    plt.plot(x, theory_probs, color='lightblue', linewidth=3, label='Theory Probs')
    plt.scatter(x, sim_case1_probs, color='darkgreen', marker='x', label='Sim Case 1')
    plt.scatter(x, sim_case2_probs, color='red', marker='o', label='Sim Case 2')
    plt.title('P(W > t) vs t')
    plt.ylabel('P(W > t)')
    plt.xlabel('t (in units of avg service time)')
    plt.legend()
    plt.show()