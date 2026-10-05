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
    min_val = min(data)
    max_val = max(data)
    sorted_data = sorted(data)
    n = len(data)
    median = sorted_data[n
    mean = sum(data) / n
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / n)
    length = n
    return [min_val, max_val, round(median, 2), round(mean, 2), round(std_dev, 2), length]
class Clinic:
    def __init__(self, env, num_doctors):
        self.env = env
        self.doctor_rooms = [simpy.Resource(env, 1) for _ in range(num_doctors)]
    def treat(self, patient):
        treatment_time = random.uniform(MIN_TREAT, MAX_TREAT)
        yield self.env.timeout(treatment_time)
def patient(env, name, clinic, num_queues):
    arrive_time = env.now
    ArrivalTime[name] = arrive_time
    print(f'Patient {name} arrives at the clinic at {arrive_time:.2f}.')
    with clinic.doctor_rooms[random.randint(0, num_queues - 1)].request() as request:
        yield request
        wait_time = env.now - arrive_time
        start_treatment_time = env.now
        yield env.process(clinic.treat(name))
        treatment_time = env.now - start_treatment_time
        print(f'Patient {name} enters doctor room after {wait_time:.2f} time and leaves after spending {treatment_time:.2f} time in doctor room')
        WaitTime[name] = wait_time
def setup(env, num_doctors, t_inter, num_queue):
    clinic = Clinic(env, num_doctors)
    for i in range(4):
        env.process(patient(env, i, clinic, num_queue))
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        env.process(patient(env, i + 1, clinic, num_queue))
def chart(data, mean):
    plt.figure(1)
    plt.plot(data, 'r.')
    plt.plot([0, len(data)], [mean, mean], 'c-')
    plt.legend(['Wait time', 'Average wait time'])
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