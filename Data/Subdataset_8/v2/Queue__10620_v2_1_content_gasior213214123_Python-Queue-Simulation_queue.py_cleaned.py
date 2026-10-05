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
    def min1(data):
        return min(data)
    def max1(data):
        return max(data)
    def median1(data):
        sorted_data = sorted(data)
        n = len(data)
        if n % 2 == 1:
            return sorted_data[n
        else:
            return sum(sorted_data[n
    def mean1(data):
        return sum(data) / len(data)
    def stddev(data):
        mean = mean1(data)
        return math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    min_val = min1(data)
    max_val = max1(data)
    median = round(median1(data), 2)
    mean = round(mean1(data), 2)
    std_dev = round(stddev(data), 2)
    length = len(data)
    return [min_val, max_val, median, mean, std_dev, length]
class Clinic(object):
    def __init__(self, env, num_doctors):
        self.env = env
        self.doctor_rooms = [simpy.Resource(env, 1) for _ in range(NUM_DOCTORS)]
    def treat(self, patient):
        treatment_time = random.uniform(MIN_TREAT, MAX_TREAT)
        yield self.env.timeout(treatment_time)
def patient(env, name, clinic, i):
    arrive_time = env.now
    ArrivalTime[name] = arrive_time
    print(f'Patient {name} arrives at the clinic at {arrive_time:.2f}.')
    with clinic.doctor_rooms[i].request() as request:
        yield request
        wait_time = env.now - arrive_time
        start_treatment_time = env.now
        yield env.process(clinic.treat(name))
        treatment_time = env.now - start_treatment_time
        print(f'Patient {name} enters doctor room {i} after {wait_time:.2f} time and leaves after spending {treatment_time:.2f} time in doctor room')
        WaitTime[name] = wait_time
def setup(env, num_doctors, t_inter, num_queue):
    clinic = Clinic(env, num_doctors)
    for i in range(4):
        env.process(patient(env, i, clinic, random.randint(0, NUM_QUEUE - 1)))
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        i += 1
        env.process(patient(env, i, clinic, random.randint(0, NUM_QUEUE - 1)))
def chart(data, mean):
    plt.figure(1)
    plt.plot(data, 'r.')
    plt.plot([0, 400], [mean, mean], 'c-')
    plt.legend(['Wait time', 'Average wait time'])
    plt.gca().set_xlim([0, 60])
    plt.xlabel('Patient Number')
    plt.ylabel('Wait time')
    plt.title("Chart")
    plt.savefig("fig1.png")
    plt.show()
print('Clinic Simulation')
random.seed(RANDOM_SEED)
env = simpy.Environment()
env.process(setup(env, NUM_DOCTORS, T_INTER, NUM_QUEUE))
env.run(until=SIM_TIME)
print("Wait Times:", WaitTime)
wait_values = list(WaitTime.values())
arrival_values = list(ArrivalTime.values())
wait_stats = analyze(wait_values)
arrival_stats = analyze(arrival_values)
print("\nData:")
print("Doctors\tQueues\tMin\tMax\tMedian\tMean\tStd\tClients in\tClients out")
print(f"{NUM_DOCTORS}\t{NUM_QUEUE}\t{wait_stats[0]}\t{wait_stats[1]}\t{wait_stats[2]}\t{wait_stats[3]}\t{wait_stats[4]}\t{arrival_stats[5]}\t{wait_stats[5]}")
chart(wait_values, wait_stats[3])