import numpy as np
import matplotlib.pyplot as plt
import Processor
speed = 0.1
number_of_processes = 15
burst_time_lambda = 3
arrival_time_scale = 15.0
SJF_priority = 0.6
FCFS_priority = 1 - SJF_priority
max_arrival_time = 0
process_pool = []
def create_process_pool():
    print("Creating the process pool...")
    global max_arrival_time
    for i in range(number_of_processes):
        process = [i + 1, 0, 0, np.random.randint(1, 3)]
        process_pool.append(process)
    max_arrival_time = create_exponential_arrival_times()
    create_poisson_burst_times()
    print("Process pool successfully created.")
    return max_arrival_time
def create_poisson_burst_times():
    poisson = np.random.poisson(burst_time_lambda, number_of_processes)
    for i, burst_time in enumerate(poisson):
        process_pool[i][2] = max(burst_time, 1)
    plot_histogram(poisson, title='Poisson Burst Times')
def create_exponential_arrival_times():
    exponential = np.random.exponential(arrival_time_scale, number_of_processes)
    for i, exp in enumerate(exponential):
        process_pool[i][1] = max(int(exp), 1)
    plot_histogram(exponential, title='Exponential Arrival Times')
    return max(exponential)
def plot_histogram(data, title):
    plt.hist(data)
    plt.title(title)
    plt.ylabel('Frequency')
    plt.xlabel('Values')
    plt.tight_layout()
    plt.show()
def sort_process_pool():
    process_pool.sort(key=lambda x: x[1])
plt.figure(1)
max_arrival_time = create_process_pool()
sort_process_pool()
print("Number Of Processes:", number_of_processes)
print("Burst Time Lambda:", burst_time_lambda)
print("Arrival Time Scale:", arrival_time_scale)
print("SJF Priority:", SJF_priority * 100, "%")
print("FCFS Priority:", FCFS_priority * 100, "%")
print("[processID, arrivalTime, burstTime, priority]  priority=1=foreground(SJF), priority=2=batch(FCFS)")
print("Process Pool:", process_pool)
Processor.start(SJF_priority, FCFS_priority, process_pool, max_arrival_time, speed)