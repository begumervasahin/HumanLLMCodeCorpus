import random
import math
import statistics
def earlang_B_recursive(n, a):
    if n == 0:
        return 1
    return a * earlang_B_recursive(n - 1, a) / (n + a * earlang_B_recursive(n - 1, a))
def earlang_C(s, a):
    assert s > a
    return (s * earlang_B_recursive(s, a)) / (s - a * (1 - earlang_B_recursive(s, a)))
def get_inter_arrival_time(arrival_rate):
    return -(1 / arrival_rate) * math.log(1 - random.random())
def get_service_time(avg_service_time):
    return -(avg_service_time) * math.log(1 - random.random())
def first_available_server_and_time(server_status):
    min_time = min(server_status)
    next_avail_server = server_status.index(min_time)
    return next_avail_server, min_time
def probability_wait_greater_than(t, wait_times):
    results = [1 if el / t > 1 else 0 for el in wait_times]
    prob_greater_than_t = sum(results) / len(results)
    return prob_greater_than_t
def run_simulation(NSTOP=1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    C = [0] * S
    A = 0
    K = 0
    AB = 0
    SX = 0
    wait_times = []
    for _ in range(NSTOP):
        inter_arrival_time = get_inter_arrival_time(arrival_rate)
        A += inter_arrival_time
        J = 0
        while A < C[J]:
            J += 1
            if J == S:
                K += 1
                next_server, min_time = first_available_server_and_time(C)
                wait_time = min_time - A
                wait_times.append(wait_time)
                AB += wait_time
                service_time = get_service_time(avg_service_time)
                SX += service_time
                C[J] = min_time + service_time
                break
        else:
            wait_times.append(0)
            service_time = get_service_time(avg_service_time)
            SX += service_time
            C[J] = A + service_time
    mean_wait_time = statistics.mean(wait_times)
    print(f'Statistical mean of wait times: {mean_wait_time}')
    average_wait_time_per_unit_time = (1 / avg_service_time) * sum(wait_times) / len(wait_times)
    carried_load = SX / A
    print(f'Simulation carried load: {carried_load}')
    RHO = carried_load / 10
    print(f'Simulation Server utilization, RHO: {RHO}')
    assert (len(wait_times) - K) == K
    print(f'Simulation E(W) per unit time: {average_wait_time_per_unit_time}')
    print(f'AB/A: {AB / A}')
    print(f'K/NSTOP: {K / NSTOP}')
    sim_probs = [K / NSTOP]
    for t in range(1, 9):
        prob = probability_wait_greater_than(t, wait_times)
        sim_probs.append(prob)
        print(f'Probability W > {t}: {prob}')
if __name__ == '__main__':
    random.seed(123)
    print(run_simulation())