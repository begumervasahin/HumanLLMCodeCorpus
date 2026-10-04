import numpy as np
import matplotlib.pyplot as plt
import Processor
SPEED = 0.1
NUMBER_OF_PROCESSES = 15
BURST_TIME_LAMBDA = 3
ARRIVAL_TIME_SCALE = 15.0
SJF_PRIORITY = 0.6
FCFS_PRIORITY = 1 - SJF_PRIORITY
process_pool = []
def create_process_pool():
    print("Creating the process pool...")
    for i in range(NUMBER_OF_PROCESSES):
        process = [i + 1, 0, 0, np.random.randint(1, 3)]
        process_pool.append(process)
    max_arrival_time = create_exponential_arrival_times()
    create_poisson_burst_times()
    print("Process pool successfully created.")
    return max_arrival_time
def create_poisson_burst_times():
    poisson_burst_times = np.random.poisson(BURST_TIME_LAMBDA, NUMBER_OF_PROCESSES)
    for i, burst_time in enumerate(poisson_burst_times):
        process_pool[i][2] = max(1, burst_time)
    plt.subplot(2, 1, 1)
    plt.hist(poisson_burst_times, bins=range(min(poisson_burst_times), max(poisson_burst_times) + 1), align='left')
    plt.tight_layout()
    plt.title('Poisson Burst Times')
    plt.ylabel('Frequency')
    plt.xlabel('Burst Times')
def create_exponential_arrival_times():
    exponential_arrival_times = np.random.exponential(ARRIVAL_TIME_SCALE, NUMBER_OF_PROCESSES)
    for i, arrival_time in enumerate(exponential_arrival_times):
        process_pool[i][1] = max(1, int(arrival_time))
    plt.subplot(2, 1, 2)
    plt.hist(exponential_arrival_times, bins=30)
    plt.tight_layout()
    plt.title('Exponential Arrival Times')
    plt.ylabel('Frequency')
    plt.xlabel('Arrival Times')
    return max(exponential_arrival_times)
def sort_process_pool():
    process_pool.sort(key=lambda elem: elem[1])
def display_process_pool():
    print("Number Of Processes:", NUMBER_OF_PROCESSES)
    print("Burst Time Lambda:", BURST_TIME_LAMBDA)
    print("Arrival Time Scale:", ARRIVAL_TIME_SCALE)
    print("SJF Priority:", SJF_PRIORITY * 100, "%")
    print("FCFS Priority:", FCFS_PRIORITY * 100, "%")
    print("[processID, arrivalTime, burstTime, priority]   priority=1=foreground(SJF), priority=2=batch(FCFS)")
    print("Process Pool:", process_pool)
def main():
    plt.figure(1)
    max_arrival_time = create_process_pool()
    sort_process_pool()
    display_process_pool()
    Processor.start(SJF_PRIORITY, FCFS_PRIORITY, process_pool, max_arrival_time, SPEED)
    plt.show()
if __name__ == "__main__":
    main()