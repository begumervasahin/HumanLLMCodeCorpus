import numpy as np
import matplotlib.pyplot as plt
def create_process_pool(number_of_processes, burst_time_lambda, arrival_time_scale, sjf_priority):
    speed = 0.1
    max_arrival_time = 0
    process_pool = []
    print("Creating the process pool...")
    for i in range(number_of_processes):
        process = [i+1, 0, 0, np.random.randint(1, 3)]
        process_pool.append(process)
    max_arrival_time = create_exponential_arrival_times(process_pool, number_of_processes, arrival_time_scale)
    create_poisson_burst_times(process_pool, number_of_processes, burst_time_lambda)
    print("Process pool successfully created.")
    sort_process_pool(process_pool)
    print("Number Of Processes: ", number_of_processes)
    print("Burst Time Lambda: ", burst_time_lambda)
    print("Arrival Time Scale: ", arrival_time_scale)
    print("SJF Priority: ", sjf_priority * 100, "%")
    print("FCFS Priority: ", (1 - sjf_priority) * 100, "%")
    print("[processID, arrivalTime, burstTime, priority]   priority=1=foreground(SJF), priority=2=batch(FCFS)")
    print("Process Pool: ", process_pool)
def create_poisson_burst_times(process_pool, number_of_processes, burst_time_lambda):
    poisson = np.random.poisson(burst_time_lambda, number_of_processes)
    for i, burst_time in zip(range(number_of_processes), poisson):
        if burst_time <= 0:
            burst_time = 1
        process_pool[i][2] = burst_time
    plt.subplot(2, 1, 1)
    plt.hist(poisson)
    plt.tight_layout()
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
def create_exponential_arrival_times(process_pool, number_of_processes, arrival_time_scale):
    exponential = np.random.exponential(arrival_time_scale, number_of_processes)
    max_arrival_time = 0
    for i, exp in zip(range(number_of_processes), exponential):
        if int(exp) <= 0:
            arrival_time = 1
        else:
            arrival_time = int(exp)
        process_pool[i][1] = arrival_time
        if exp > max_arrival_time:
            max_arrival_time = exp
    plt.subplot(2, 1, 2)
    plt.hist(exponential)
    plt.tight_layout()
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    return max_arrival_time
def sort_process_pool(process_pool):
    process_pool.sort(key=lambda x: x[1])
if __name__ == "__main__":
    number_of_processes = 15
    burst_time_lambda = 3
    arrival_time_scale = 15.0
    sjf_priority = 0.6
    create_process_pool(number_of_processes, burst_time_lambda, arrival_time_scale, sjf_priority)