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
WaitTime = dict()
ArrivalTime = dict()
def analyze(data):
    def min1(data):
        return min(data)
    def max1(data):
        return max(data)
    def median1(data):
        n = len(data)
        sorted_data = sorted(data)
        if n % 2 == 1:
            return sorted_data[n
        else:
            return sum(sorted_data[n
    def mean1(data):
        return sum(data) / len(data)
    def stddev(data):
        mean = mean1(data)
        return math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    return [
        min1(data),
        max1(data),
        round(median1(data), 2),
        round(mean1(data), 2),
        round(stddev(data), 2),
        len(data)
    ]
class Clinic(object):
    def __init__(self, env, num_doctors):
        self.env = env
        self.docroom = [simpy.Resource(env, 1) for _ in range(num_doctors)]
    def treat(self, patient):
        treatment_time = random.uniform(MIN_TREAT, MAX_TREAT)
        yield self.env.timeout(treatment_time)
def patient(env, name, clinic, doctor_id):
    arrival_time = env.now
    ArrivalTime[name] = arrival_time
    print(f'Patient {name} arrives at the clinic at {arrival_time:.2f}.')
    with clinic.docroom[doctor_id].request() as request:
        yield request
        wait_time = env.now - arrival_time
        WaitTime[name] = wait_time
        print(f'Patient {name} enters doctor room {doctor_id} after waiting {wait_time:.2f} time units.')
        yield env.process(clinic.treat(name))
        treatment_time = env.now - (arrival_time + wait_time)
        print(f'Patient {name} leaves doctor room {doctor_id} after spending {treatment_time:.2f} time units.')
def setup(env, num_doctors, t_inter, num_queue):
    clinic = Clinic(env, num_doctors)
    for i in range(4):
        env.process(patient(env, i, clinic, random.randint(0, num_queue - 1)))
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        i += 1
        env.process(patient(env, i, clinic, random.randint(0, num_queue - 1)))
def plot_wait_times(wait_times, mean_wait_time):
    plt.figure()
    plt.plot(wait_times, 'r.')
    plt.axhline(y=mean_wait_time, color='c', linestyle='-')
    plt.legend(['Wait Time', 'Mean Wait Time'])
    plt.xlim([0, len(wait_times)])
    plt.xlabel('Patient Number')
    plt.ylabel('Wait Time')
    plt.title('Patient Wait Times')
    plt.savefig('fig1.png')
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
    print("Wait Time Statistics:")
    print(f"Min: {wait_stats[0]}, Max: {wait_stats[1]}, Median: {wait_stats[2]}, Mean: {wait_stats[3]}, Std: {wait_stats[4]}, Clients Processed: {wait_stats[5]}")
    plot_wait_times(wait_times, wait_stats[3])
if __name__ == '__main__':
    main()