import random
import simpy
import math
import matplotlib.pyplot as plt
RANDOM_SEED = 42
NUM_QUEUE = 2
NUM_DOCTORS = 2
T_INTER = 6
MIN_TREAT = 5
MAX_TREAT = 10
SIM_TIME = 300
WaitTime = {}
ArrivalTime = {}
def analyze(data):
    def min_value(data):
        return min(data)
    def max_value(data):
        return max(data)
    def median_value(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n
        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    def mean_value(data):
        return sum(data) / len(data)
    def stddev_value(data):
        mean = mean_value(data)
        return math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    return [
        min_value(data),
        max_value(data),
        round(median_value(data), 2),
        round(mean_value(data), 2),
        round(stddev_value(data), 2),
        len(data)
    ]
class Clinic:
    def __init__(self, env, num_doctors):
        self.env = env
        self.docrooms = [simpy.Resource(env, 1) for _ in range(num_doctors)]
    def treat(self, patient):
        treatment_time = random.uniform(MIN_TREAT, MAX_TREAT)
        yield self.env.timeout(treatment_time)
def patient(env, name, clinic, queue_id):
    arrive_time = env.now
    ArrivalTime[name] = arrive_time
    print(f'Patient {name} arrives at the clinic at {arrive_time:.2f}.')
    with clinic.docrooms[queue_id].request() as request:
        yield request
        wait_time = env.now - arrive_time
        WaitTime[name] = wait_time
        print(f'Patient {name} enters doctor room {queue_id} after waiting {wait_time:.2f} minutes.')
        yield env.process(clinic.treat(name))
        treatment_time = env.now - arrive_time - wait_time
        print(f'Patient {name} leaves doctor room {queue_id} after {treatment_time:.2f} minutes of treatment.')
def setup(env, num_doctors, t_inter, num_queue):
    clinic = Clinic(env, num_doctors)
    for i in range(4):
        env.process(patient(env, i, clinic, random.randint(0, num_queue - 1)))
    i = 4
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        env.process(patient(env, i, clinic, random.randint(0, num_queue - 1)))
        i += 1
def plot_wait_times(wait_times, mean_wait_time):
    plt.figure(1)
    plt.plot(wait_times, 'r.')
    plt.axhline(y=mean_wait_time, color='c', linestyle='-')
    plt.legend(['Wait time', 'Average wait time'])
    plt.xlim([0, len(wait_times)])
    plt.xlabel('Patient number')
    plt.ylabel('Wait time (minutes)')
    plt.title("Wait Time Chart")
    plt.savefig("fig1.png")
    plt.show()
def main():
    print('Clinic Simulation')
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    env.process(setup(env, NUM_DOCTORS, T_INTER, NUM_QUEUE))
    env.run(until=SIM_TIME)
    wait_times = list(WaitTime.values())
    arrival_times = list(ArrivalTime.values())
    wait_stats = analyze(wait_times)
    arrival_stats = analyze(arrival_times)
    print("Data:")
    print(f"{'Doctors':>7}\t{'Queues':>7}\t{'Min':>7}\t{'Max':>7}\t{'Median':>7}\t{'Mean':>7}\t{'Std Dev':>7}\t{'Arrivals':>11}\t{'Served':>7}")
    print(f"{NUM_DOCTORS:7}\t{NUM_QUEUE:7}\t{wait_stats[0]:7}\t{wait_stats[1]:7.2f}\t{wait_stats[2]:7.2f}\t{wait_stats[3]:7.2f}\t{wait_stats[4]:7.2f}\t{arrival_stats[5]:11}\t{wait_stats[5]:7}")
    plot_wait_times(wait_times, wait_stats[3])
if __name__ == "__main__":
    main()