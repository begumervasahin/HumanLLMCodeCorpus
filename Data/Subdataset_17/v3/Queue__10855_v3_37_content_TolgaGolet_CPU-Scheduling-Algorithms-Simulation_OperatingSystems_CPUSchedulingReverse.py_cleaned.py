import numpy as np
import matplotlib.pyplot as plt
import Processor
SPEED = 0.1
NUMBER_OF_PROCESSES = 15
BURST_TIME_LAMBDA = 3
ARRIVAL_TIME_SCALE = 15.0
SJF_PRIORITY = 0.6
FCFS_PRIORITY = 1 - SJF_PRIORITY
def create_process_pool(number_of_processes):
    process_pool = []
    print("Creating the process pool...")
    for i in range(number_of_processes):
        process = [i + 1, 0, 0, np.random.randint(1, 3)]
        process_pool.append(process)
    max_arrival_time = create_exponential_arrival_times(process_pool)
    create_poisson_burst_times(process_pool)
    print("Process pool successfully created.")
    return process_pool, max_arrival_time
def create_poisson_burst_times(process_pool):
    poisson = np.random.poisson(BURST_TIME_LAMBDA, len(process_pool))
    for i, burst_time in enumerate(poisson):
        process_pool[i][2] = max(burst_time, 1)
    plt.subplot(2, 1, 1)
    plt.hist(poisson, bins=range(1, max(poisson) + 1), edgecolor='black')
    plt.tight_layout()
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
def create_exponential_arrival_times(process_pool):
    exponential = np.random.exponential(ARRIVAL_TIME_SCALE, len(process_pool))
    for i, exp in enumerate(exponential):
        process_pool[i][1] = max(int(exp), 1)
    plt.subplot(2, 1, 2)
    plt.hist(exponential, bins=range(1, int(max(exponential)) + 1), edgecolor='black')
    plt.tight_layout()
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    return max(exponential)
def sort_process_pool(process_pool):
    process_pool.sort(key=lambda elem: elem[1])
def main():
    plt.figure(1)
    process_pool, max_arrival_time = create_process_pool(NUMBER_OF_PROCESSES)
    sort_process_pool(process_pool)
    print("Number Of Processes:", NUMBER_OF_PROCESSES)
    print("Burst Time Lambda:", BURST_TIME_LAMBDA)
    print("Arrival Time Scale:", ARRIVAL_TIME_SCALE)
    print("SJF Priority:", SJF_PRIORITY * 100, "%")
    print("FCFS Priority:", FCFS_PRIORITY * 100, "%")
    print("[processID, arrivalTime, burstTime, priority] priority=1=foreground(SJF), priority=2=batch(FCFS)")
    print("Process Pool:", process_pool)
    Processor.start(SJF_PRIORITY, FCFS_PRIORITY, process_pool, max_arrival_time, SPEED)
    plt.show()
if __name__ == "__main__":
    main()