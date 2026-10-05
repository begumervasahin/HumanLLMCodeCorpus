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
        n = len(data)
        sorted_data = sorted(data)
        if n % 2 == 1:
            return sorted_data[n
        else:
            return sum(sorted_data[n
    def mean1(data):
        return sum(data) / len(data)
    def stddev(data):
        mean = sum(data) / len(data)
        return math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    minval = min1(data)
    maxval = max1(data)
    median = round(median1(data), 2)
    mean = round(mean1(data), 2)
    std = round(stddev(data), 2)
    lngth = len(data)
    return [minval, maxval, median, mean, std, lngth]
class Clinic(object):
    def __init__(self, env, num_doctors):
        self.env = env
        self.docroom = [simpy.Resource(env, 1) for _ in range(NUM_DOCTORS)]
    def treat(self, patient):
        treatment_time = random.uniform(MIN_TREAT, MAX_TREAT)
        yield self.env.timeout(treatment_time)
def patient(env, name, clinic, i):
    arrive_time = env.now
    ArrivalTime[name] = arrive_time
    print('Patient %d arrives at the clinic at %.2f.' % (name, arrive_time))
    with clinic.docroom[i].request() as request:
        yield request
        wait_time = env.now - arrive_time
        treatment_start_time = env.now
        yield env.process(clinic.treat(name))
        treatment_time = env.now - treatment_start_time
        print('Patient %d enters doctor room %d after %.2f time and leaves after spending %.2f time in doctor room' % (name, i, wait_time, treatment_time))
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
    plt.legend(['Wait Time', 'Average Wait Time'])
    plt.gca().set_xlim([0, 60])
    plt.xlabel('Patient Number')
    plt.ylabel('Wait Time')
    plt.title("Chart")
    plt.savefig("fig1.png")
    plt.show()
if __name__ == '__main__':
    print('Clinic Simulation')
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    env.process(setup(env, NUM_DOCTORS, T_INTER, NUM_QUEUE))
    env.run(until=SIM_TIME)
    print "Wait Times: " , WaitTime
    keys, values = WaitTime.keys(), WaitTime.values()
    arrival_times = ArrivalTime.values()
    wait_time_stats = analyze(values)
    arrival_time_stats = analyze(arrival_times)
    print "Data: "
    print "{:>7}".format("Doctors"), "\t", \
          "{:>7}".format("Queues"), "\t", \
          "{:>7}".format("Min"), "\t", \
          "{:>7}".format("Max"), "\t", \
          "{:>7}".format("Median"), "\t", \
          "{:>7}".format("Mean"), "\t", \
          "{:>7}".format("Std"), "\t", \
          "{:>7}".format("Clients in"), "\t", \
          "{:>7}".format("Clients out"), "\t"
    print "Data:", \
          "{:7}".format(NUM_DOCTORS), "\t", \
          "{:7}".format(NUM_QUEUE), "\t", \
          "{:7}".format(wait_time_stats[0]), "\t", \
          "{:7}".format(round(wait_time_stats[1], 2)), "\t", \
          "{:7}".format(wait_time_stats[2]), "\t", \
          "{:7}".format(wait_time_stats[3]), "\t", \
          "{:7}".format(wait_time_stats[4]), "\t", \
          "{:7}".format(arrival_time_stats[5]), "\t", \
          "{:7}".format(wait_time_stats[5]), "\t"
    chart(values, wait_time_stats[3])