import random
import math
import statistics
import matplotlib.pyplot as plt
def erlang_B_rec(n, a):
    if n == 0:
        return 1
    previous_B = erlang_B_rec(n - 1, a)
    return (a * previous_B) / (n + a * previous_B)
def erlang_C(s, a):
    assert s > a, "Number of servers must be greater than the offered load"
    B = erlang_B_rec(s, a)
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
    server_status = [0] * S
    total_arrivals = 0
    num_customers_blocked = 0
    total_wait_time = 0
    total_service_time = 0
    wait_times = []
    num_customers_no_wait = 0
    for _ in range(NSTOP):
        inter_arrival = get_inter_arrival_time(arrival_rate)
        total_arrivals += inter_arrival
        server_index, next_available_time = first_available_server_and_time(server_status)
        if total_arrivals < next_available_time:
            num_customers_blocked += 1
            wait_time = next_available_time - total_arrivals
            wait_times.append(wait_time)
            total_wait_time += wait_time
        else:
            num_customers_no_wait += 1
            wait_times.append(0)
            wait_time = 0
        service_time = get_service_time(avg_service_time)
        total_service_time += service_time
        server_status[server_index] = total_arrivals + wait_time + service_time
    mean_wait_time = statistics.mean(wait_times)
    average_wait_time_per_unit_time = sum(wait_times) / (len(wait_times) * avg_service_time)
    carried_load = total_service_time / total_arrivals
    theoretical_loss_load = arrival_rate * avg_service_time * (1 - erlang_B_rec(S, arrival_rate * avg_service_time))
    utilization = carried_load / S
    theoretical_rho = arrival_rate * avg_service_time / S
    print(f'Statistical mean of wait times: {mean_wait_time}')
    print(f'Simulation carried load: {carried_load}')
    print(f'Theoretical loss system carried load: {theoretical_loss_load}')
    print(f'Simulation server utilization (RHO): {utilization}')
    print(f'Theoretical delay system rho: {theoretical_rho}')
    print(f'Simulation E(W) per unit time: {average_wait_time_per_unit_time}')
    print(f'AB/A: {total_wait_time / total_arrivals}')
    print(f'K/NSTOP: {num_customers_blocked / NSTOP}')
    sim_probs = [num_customers_blocked / NSTOP]
    for t in range(1, 9):
        prob = prob_wait_greater_than(t * avg_service_time, wait_times)
        sim_probs.append(prob)
        print(f'Probability W > {t * avg_service_time}: {prob}')
    theoretical_probs = []
    for t in range(9):
        t_scaled = t * avg_service_time
        prob_wait_greater_than_t = erlang_C(S, arrival_rate * avg_service_time) * math.exp(-1 * (1 - theoretical_rho) * S * (1 / avg_service_time) * t_scaled)
        theoretical_probs.append(prob_wait_greater_than_t)
        print(f'Theory delay system probability wait greater than {t_scaled} time units: {prob_wait_greater_than_t}')
    return sim_probs, theoretical_probs
def plot_results(sim_probs, theoretical_probs):
    x = list(range(9))
    sim_case1_probs = [0.85967, 0.574334, 0.38659, 0.265105, 0.178798, 0.119471, 0.081273, 0.056299, 0.03944]
    sim_case2_probs = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    plt.plot(x, theoretical_probs, color='lightblue', linewidth=3, label='Theory Probs')
    plt.scatter(x, sim_case1_probs, color='darkgreen', marker='x', label='Sim Case 1')
    plt.scatter(x, sim_case2_probs, color='red', marker='o', label='Sim Case 2')
    plt.title('P(W > t) vs t')
    plt.ylabel('P(W > t)')
    plt.xlabel('t (in units of avg service time)')
    plt.legend()
    plt.show()
if __name__ == '__main__':
    random.seed(123)
    sim_probs, theoretical_probs = run_simulation()
    plot_results(sim_probs, theoretical_probs)