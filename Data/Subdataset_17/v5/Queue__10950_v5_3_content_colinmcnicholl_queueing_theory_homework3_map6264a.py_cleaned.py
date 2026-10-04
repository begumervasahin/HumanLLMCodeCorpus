import random
import math
import statistics
import pylab
def erlang_B_recursive(n, a):
    if n == 0:
        return 1
    prev_B = erlang_B_recursive(n - 1, a)
    return (a * prev_B) / (n + a * prev_B)
def erlang_C(s, a):
    assert s > a, "Number of servers must be greater than the offered load."
    B = erlang_B_recursive(s, a)
    return (s * B) / (s - a * (1 - B))
def get_inter_arrival_time(arrival_rate):
    return -(1 / arrival_rate) * math.log(1 - random.random())
def get_service_time(avg_service_time):
    return -(avg_service_time) * math.log(1 - random.random())
def find_first_available_server(server_status):
    min_time = min(server_status)
    next_server = server_status.index(min_time)
    return next_server, min_time
def calculate_probability_greater_than(t, wait_times):
    return sum(1 if wait > t else 0 for wait in wait_times) / len(wait_times)
def run_simulation(NSTOP=1000000, S=10, arrival_rate=4, avg_service_time=2.4):
    server_status = [0] * S
    current_time = 0
    blocked_calls = 0
    total_wait_time = 0
    total_service_time = 0
    wait_times = []
    for _ in range(NSTOP):
        inter_arrival_time = get_inter_arrival_time(arrival_rate)
        current_time += inter_arrival_time
        server_index = next((i for i, status in enumerate(server_status) if status <= current_time), None)
        if server_index is None:
            blocked_calls += 1
            server_index, next_available_time = find_first_available_server(server_status)
            wait_time = next_available_time - current_time
            wait_times.append(wait_time)
            total_wait_time += wait_time
            service_time = get_service_time(avg_service_time)
            total_service_time += service_time
            server_status[server_index] = next_available_time + service_time
        else:
            wait_times.append(0)
            service_time = get_service_time(avg_service_time)
            total_service_time += service_time
            server_status[server_index] = current_time + service_time
    mean_wait_time = statistics.mean(wait_times)
    carried_load = total_service_time / current_time
    theory_carried_load = (arrival_rate * avg_service_time) * (1 - erlang_B_recursive(S, arrival_rate * avg_service_time))
    utilization = carried_load / S
    theory_utilization = (arrival_rate * avg_service_time) / S
    avg_wait_time_per_unit_time = (1 / avg_service_time) * sum(wait_times) / len(wait_times)
    print(f'Statistical mean of wait times: {mean_wait_time}')
    print(f'Simulation carried load: {carried_load}')
    print(f'Theory loss system carried load: {theory_carried_load}')
    print(f'Simulation server utilization (RHO): {utilization}')
    print(f'Theory delay system utilization (RHO): {theory_utilization}')
    print(f'Simulation average wait time per unit time: {avg_wait_time_per_unit_time}')
    print(f'Total blocked calls ratio (K/NSTOP): {blocked_calls / NSTOP}')
    sim_probs = [blocked_calls / NSTOP]
    for t in range(1, 9):
        prob = calculate_probability_greater_than(t, wait_times)
        sim_probs.append(prob)
        print(f'Probability W > {t}: {prob}')
    theory_probs = []
    for t in [t * avg_service_time for t in range(9)]:
        prob_wait_greater_than_t = erlang_C(S, arrival_rate * avg_service_time) * math.exp(-1 * (1 - theory_utilization) * S * (1 / avg_service_time) * t)
        theory_probs.append(prob_wait_greater_than_t)
        print(f'Theory delay system probability wait greater than {t} time units: {prob_wait_greater_than_t}')
    return sim_probs, theory_probs
def plot_results(sim_probs, theory_probs):
    x = list(range(9))
    sim_case2_probs = [0.845178, 0.38427, 0.168627, 0.071811, 0.028784, 0.010539, 0.003378, 0.001134, 0.000469]
    fig, ax = pylab.subplots()
    ax.plot(x, theory_probs, color='lightblue', linewidth=3, label='Theory Probs')
    ax.scatter(x, sim_probs, color='darkgreen', marker='x', label='Sim Case 1 Probs')
    ax.scatter(x, sim_case2_probs, color='red', marker='o', label='Sim Case 2 Probs')
    ax.set(title='Case1: exponential arrivals & service, Case2: const. service time', ylabel='P(W>t)', xlabel='t')
    ax.legend()
    pylab.show()
if __name__ == '__main__':
    random.seed(123)
    sim_probs, theory_probs = run_simulation()
    plot_results(sim_probs, theory_probs)