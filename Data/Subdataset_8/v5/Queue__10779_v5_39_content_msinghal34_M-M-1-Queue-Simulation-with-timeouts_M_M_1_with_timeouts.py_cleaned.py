import random
from enum import Enum
from collections import deque
from util import PriorityQueue
class EventType(Enum):
    ARRIVAL = "Arrival"
    DEPARTURE = "Departure"
class Request:
    def __init__(self, creation_time, timeout):
        self.creation_time = creation_time
        self.timeout = timeout
    def __repr__(self):
        return f"(Request creation time = {round(self.creation_time, 6)} timeout = {round(self.timeout, 6)})"
class Server:
    def __init__(self, mean_service_time):
        self.mean_service_time = mean_service_time
        self.queue = deque([])
        self.is_busy = False
        self.customers_serviced = 0
        self.response_time_so_far = 0.0
        self.goodput = 0
        self.badput = 0
    def handle_departure(self, request, sim_time, event_list, verbose=True):
        self.customers_serviced += 1
        self.response_time_so_far += (sim_time - request.creation_time)
        if (request.creation_time + request.timeout >= sim_time):
            self.goodput += 1
            if verbose:
                print(f"{sim_time}\t: {request}\tDeparted as Goodput")
        else:
            self.badput += 1
            if verbose:
                print(f"{sim_time}\t: {request}\tDeparted as Badput")
        if len(self.queue) == 0:
            self.is_busy = False
        else:
            self.is_busy = True
            request = self.queue.popleft()
            service_time = random.expovariate(1.0 / self.mean_service_time)
            event_list.push(sim_time + service_time, EventType.DEPARTURE, request)
    def handle_arrival(self, request, sim_time, event_list, verbose=True):
        if verbose:
            print(f"{sim_time}\t: {request}\tArrived ")
        if not self.is_busy:
            self.is_busy = True
            service_time = random.expovariate(1.0 / self.mean_service_time)
            event_list.push(sim_time + service_time, EventType.DEPARTURE, request)
        else:
            self.queue.append(request)
    def get_customers_serviced(self):
        return self.customers_serviced
    def get_status(self):
        return self.is_busy
    def get_queue_length(self):
        return len(self.queue)
    def get_total_response_time(self):
        return self.response_time_so_far
    def get_goodput(self):
        return self.goodput
    def get_badput(self):
        return self.badput
def run(i, mean_service_time, mean_interarrival_time, mean_timeout, max_customers_to_service):
    event_list = PriorityQueue()
    sim_time = 0.0
    server = Server(mean_service_time)
    interarrival_time = random.expovariate(1.0 / mean_interarrival_time)
    timeout = random.expovariate(1.0 / mean_timeout)
    event_list.push(sim_time + interarrival_time, EventType.ARRIVAL, Request(sim_time + interarrival_time, timeout))
    utilization_time = 0.0
    queue_length_area = 0
    while not (event_list.is_empty() or server.get_customers_serviced() == max_customers_to_service):
        event_start_time, event_type, request = event_list.pop()
        prev_sim_time = sim_time
        sim_time = event_start_time
        if event_type == EventType.DEPARTURE:
            utilization_time += (sim_time - prev_sim_time)
            queue_length_area += (sim_time - prev_sim_time) * server.get_queue_length()
            server.handle_departure(request, sim_time, event_list, verbose)
        elif event_type == EventType.ARRIVAL:
            if server.get_status() == True:
                utilization_time += (sim_time - prev_sim_time)
            queue_length_area += (sim_time - prev_sim_time) * server.get_queue_length()
            server.handle_arrival(request, sim_time, event_list, verbose)
            interarrival_time = random.expovariate(1.0 / mean_interarrival_time)
            timeout = random.expovariate(1.0 / mean_timeout)
            event_list.push(sim_time + interarrival_time, EventType.ARRIVAL, Request(sim_time + interarrival_time, timeout))
    assert server.get_customers_serviced() == max_customers_to_service
    total_time = sim_time
    response_time_so_far = server.get_total_response_time()
    utilization = utilization_time / total_time
    queue_length = queue_length_area / total_time
    response_time = response_time_so_far / max_customers_to_service
    throughput = max_customers_to_service / total_time
    goodput = server.get_goodput() / total_time
    badput = server.get_badput() / total_time
    assert abs(goodput + badput - throughput) < 1e-3
    print("")
    print("Server Utilization:\t", utilization)
    print("Average Queue Length:\t", queue_length)
    print("Average Response Time:\t", response_time)
    print("Goodput:\t\t", goodput)
    print("Badput:\t\t\t", badput)
    return utilization, queue_length, response_time, goodput, badput
def get_mean(list_):
    return sum(list_) / len(list_)
mean_service_time = float(input("Enter mean service time of server: "))
mean_interarrival_time = float(input("Enter mean interarrival time of requests: "))
mean_timeout = float(input("Enter average timeout of requests: "))
max_customers_to_service = int(input("Enter maximum number of customers to service before stopping a run: "))
num_of_runs = int(input("Enter number of runs: "))
verbose = bool(int(input("Type 1 for verbose and 0 for no verbose: ")))
avg_utilization = []
avg_queue_length = []
avg_response_time = []
avg_goodput = []
avg_badput = []
for i in range(num_of_runs):
    print("--------------------------------------------------")
    print("Run", i)
    utilization, queue_length, response_time, goodput, badput = run(i, mean_service_time, mean_interarrival_time, mean_timeout, max_customers_to_service)
    avg_utilization.append(utilization)
    avg_queue_length.append(queue_length)
    avg_response_time.append(response_time)
    avg_goodput.append(goodput)
    avg_badput.append(badput)
print("\nAverage Results Over All Runs:")
print("Server Utilization:\t", get_mean(avg_utilization))
print("Queue Length:\t\t", get_mean(avg_queue_length))
print("Response Time:\t\t", get_mean(avg_response_time))
print("Goodput:\t\t", get_mean(avg_goodput))
print("Badput:\t\t\t", get_mean(avg_badput))