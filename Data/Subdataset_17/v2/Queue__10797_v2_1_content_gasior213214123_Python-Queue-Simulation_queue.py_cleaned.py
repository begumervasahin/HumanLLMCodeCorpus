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
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:
            return sorted_data[n
        else:
            return (sorted_data[n
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
class Clinic:
    def __init__(self, env, num_doctors):
        self.env = env
        self.docroom = [simpy.Resource(env, 1) for _ in range(num_doctors)]
    def treat(self, patient):
        treatment_time = random.uniform(MIN_TREAT, MAX_TREAT)
        yield self.env.timeout(treatment_time)
def patient(env, name, clinic, queue_id):
    arrive = env.now
    ArrivalTime[name] = arrive
    print(f'Patient {name} arrives at the clinic at {arrive:.2f}.')
    with clinic.docroom[queue_id].request() as request:
        yield request
        wait = env.now - arrive
        waiting = env.now
        yield env.process(clinic.treat(name))
        treatment = env.now - waiting
        print(f'Patient {name} enters doctor room {queue_id} after {wait:.2f} time and leaves after spending {treatment:.2f} time in doctor room')
        WaitTime[name] = wait
def setup(env, num_doctors, t_inter, num_queue):
    clinic = Clinic(env, num_doctors)
    for i in range(4):
        env.process(patient(env, i, clinic, random.randint(0, num_queue - 1)))
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        i += 1
        env.process(patient(env, i, clinic, random.randint(0, num_queue - 1)))
def chart(data, mean):
    plt.figure(1)
    plt.plot(data, 'r.')
    plt.plot([0, len(data)], [mean, mean], 'c-')
    plt.legend(['Wait time', 'Average wait time'])
    plt.gca().set_xlim([0, len(data)])
    plt.xlabel('Patient number')
    plt.ylabel('Wait time')
    plt.title("Wait Time Chart")
    plt.savefig("fig1.png")
    plt.show()
print('Clinic Simulation')
random.seed(RANDOM_SEED)
env = simpy.Environment()
env.process(setup(env, NUM_DOCTORS, T_INTER, NUM_QUEUE))
env.run(until=SIM_TIME)
print("Wait time: ", WaitTime)
keys, values = WaitTime.keys(), WaitTime.values()
arrival_values = ArrivalTime.values()
wait_stats = analyze(values)
arrival_stats = analyze(arrival_values)
print("Data:")
print(f"{'Doctors':>7}\t{'Queues':>7}\t{'Min':>7}\t{'Max':>7}\t{'Median':>7}\t{'Mean':>7}\t{'Std':>7}\t{'Clients in':>11}\t{'Clients out':>12}")
print(f"{NUM_DOCTORS:7}\t{NUM_QUEUE:7}\t{wait_stats[0]:7}\t{wait_stats[1]:7.2f}\t{wait_stats[2]:7}\t{wait_stats[3]:7}\t{wait_stats[4]:7}\t{arrival_stats[5]:11}\t{wait_stats[5]:12}")
chart(values, wait_stats[3])