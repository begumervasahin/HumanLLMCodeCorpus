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
        return f"Request(creation_time={round(self.creation_time, 6)}, timeout={round(self.timeout, 6)})"
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
        self.response_time_so_far += sim_time - request.creation_time
        if request.creation_time + request.timeout >= sim_time:
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
def run(mean_service_time, mean_interarrival_time, mean_timeout, max_customers_to_service, verbose=True):
if __name__ == "__main__":
    mean_service_time = float(input("Enter mean service time of server: "))
    mean_interarrival_time = float(input("Enter mean interarrival time of requests: "))
    mean_timeout = float(input("Enter average timeout of requests: "))
    MAX_CUSTOMERS_TO_SERVICE = int(input("Enter maximum number of customers to service before stopping a run: "))
    NUM_OF_RUNS = int(input("Enter number of runs: "))
    verbose = bool(int(input("Type 1 for verbose and 0 for no verbose: ")))
    avg_utilization = []
    avg_queue_length = []
    avg_response_time = []
    avg_goodput = []
    avg_badput = []
    for i in range(NUM_OF_RUNS):
        print("--------------------------------------------------")
        print("Run", i)
        utilization, queue_length, response_time, goodput, badput = run(
            mean_service_time, mean_interarrival_time, mean_timeout, MAX_CUSTOMERS_TO_SERVICE, verbose)
        avg_utilization.append(utilization)
        avg_queue_length.append(queue_length)
        avg_response_time.append(response_time)
        avg_goodput.append(goodput)
        avg_badput.append(badput)
    print("\nAverage Results:")
    print("Server Utilization:\t", sum(avg_utilization) / len(avg_utilization))
    print("Queue Length:\t\t", sum(avg_queue_length) / len(avg_queue_length))
    print("Response Time:\t\t", sum(avg_response_time) / len(avg_response_time))
    print("Goodput:\t\t", sum(avg_goodput) / len(avg_goodput))
    print("Badput:\t\t\t", sum(avg_badput) / len(avg_badput))