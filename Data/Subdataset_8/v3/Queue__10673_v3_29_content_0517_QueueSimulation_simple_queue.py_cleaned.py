import queue
class SimulationQueue:
    def __init__(self, arrival_rate, service_rate, simulation_time=10000):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.simulation_time = simulation_time
        self.buffer = queue.Queue()
        self.num_in_system = []
        self.now_serve = 0
        self.next_free_time = 0
        self.delay_time = []
        self.departure_time = []
        self.workload = []
    def set_up(self):
        self.num_points = int(self.arrival_rate * self.simulation_time)
        self.inter_arrival_time = [1 / self.arrival_rate] * self.num_points
        self.service_time = [1 / self.service_rate] * self.num_points
        self.arrival_time = [sum(self.inter_arrival_time[:i + 1]) for i in range(self.num_points)]
    def reset_run(self):
        self.departure_time.clear()
        self.delay_time.clear()
        self.workload.clear()
        self.num_in_system.clear()
        self.next_free_time = 0
        self.now_serve = 0
        while not self.buffer.empty():
            self.buffer.get()
    def FIFO(self):
        self.reset_run()
        for i in range(len(self.arrival_time)):
            while self.now_serve > 0 and self.departure_time[self.now_serve] < self.arrival_time[i] and not self.buffer.empty():
                self.now_serve = self.buffer.get()
            if self.next_free_time > self.arrival_time[i]:
                self.workload.append(self.next_free_time - self.arrival_time[i])
                self.next_free_time += self.service_time[i]
                self.num_in_system.append(self.buffer.qsize() + 1)
                self.departure_time.append(self.next_free_time)
                self.delay_time.append(self.next_free_time - self.arrival_time[i])
                self.buffer.put(i)
            else:
                self.num_in_system.append(self.buffer.qsize())
                self.delay_time.append(self.service_time[i])
                self.now_serve = i
                self.next_free_time = self.arrival_time[self.now_serve] + self.service_time[self.now_serve]
                self.departure_time.append(self.next_free_time)
                self.workload.append(0)
        while not self.buffer.empty():
            self.now_serve = self.buffer.get()
    def time_average(self):
        dp_index = 0
        ar_index = 0
        Qs = 0
        self.time_total_Q = 0
        event_time = 0
        while dp_index < len(self.departure_time):
            if ar_index < len(self.arrival_time) and self.arrival_time[ar_index] < self.departure_time[dp_index]:
                self.time_total_Q += Qs * (self.arrival_time[ar_index] - event_time)
                Qs += 1
                event_time = self.arrival_time[ar_index]
                ar_index += 1
            else:
                self.time_total_Q += Qs * (self.departure_time[dp_index] - event_time)
                Qs -= 1
                event_time = self.departure_time[dp_index]
                dp_index += 1
        return self.time_total_Q / self.departure_time[-1]