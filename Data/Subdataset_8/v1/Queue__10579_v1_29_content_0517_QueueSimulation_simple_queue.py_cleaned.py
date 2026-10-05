import queue
class SimulationQueue:
    def __init__(self, lamb, mu, simu_time=10000):
        self.lamb = lamb
        self.mu = mu
        self.rho = float(self.lamb) / self.mu
        self.simu_time = simu_time
        self.buffer = queue.Queue()
        self.num_in_sys = []
        self.now_serve = 0
        self.next_free_t = 0
        self.delay_time = []
        self.depart_time = []
        self.workload = []
    def set_up(self):
        self.num_points = self.lamb * self.simu_time
        self.inter_arrival_time = [1 / self.lamb for _ in range(self.num_points)]
        self.service_time = [1 / self.mu for _ in range(self.num_points)]
        self.arrival_time = [sum(self.inter_arrival_time[:i + 1]) for i in range(self.num_points)]
    def reset_run(self):
        self.depart_time = []
        self.delay_time = []
        self.workload = []
        self.num_in_sys = []
        self.next_free_t = 0
        self.now_serve = 0
        while not self.buffer.empty():
            self.buffer.get()
    def FIFO(self):
        self.reset_run()
        for i in range(len(self.arrival_time)):
            while self.now_serve > 0 and self.depart_time[self.now_serve] < self.arrival_time[i] and not self.buffer.empty():
                self.now_serve = self.buffer.get()
            if self.next_free_t > self.arrival_time[i]:
                self.workload.append(self.next_free_t - self.arrival_time[i])
                self.next_free_t += self.service_time[i]
                self.num_in_sys.append(self.buffer.qsize() + 1)
                self.depart_time.append(self.next_free_t)
                self.delay_time.append(self.next_free_t - self.arrival_time[i])
                self.buffer.put(i)
            else:
                self.num_in_sys.append(self.buffer.qsize())
                self.delay_time.append(self.service_time[i])
                self.now_serve = i
                self.next_free_t = self.arrival_time[self.now_serve] + self.service_time[self.now_serve]
                self.depart_time.append(self.next_free_t)
                self.workload.append(0)
        while not self.buffer.empty():
            self.now_serve = self.buffer.get()
    def time_average(self):
        dp_index = 0
        ar_index = 0
        Qs = 0
        self.time_total_Q = 0
        event_t = 0
        while dp_index < self.num_points:
            if ar_index < self.num_points and self.arrival_time[ar_index] < self.depart_time[dp_index]:
                self.time_total_Q += (Qs * (self.arrival_time[ar_index] - event_t))
                Qs += 1
                event_t = self.arrival_time[ar_index]
                ar_index += 1
            else:
                self.time_total_Q += (Qs * (self.depart_time[dp_index] - event_t))
                Qs -= 1
                event_t = self.depart_time[dp_index]
                dp_index += 1
        return self.time_total_Q / self.depart_time[-1]