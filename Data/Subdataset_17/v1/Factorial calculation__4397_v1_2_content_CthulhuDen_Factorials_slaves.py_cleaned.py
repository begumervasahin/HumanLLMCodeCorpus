import multiprocessing
def worker_function(function, operating, queue_in, queue_out, terminator, lock):
    while not terminator.is_set():
        operating.wait()
        with lock:
            if queue_in.empty():
                continue
            task = queue_in.get()
        result = function(task)
        queue_out.put(result)
    queue_out.close()
class Slaves:
    def __init__(self, function, number=multiprocessing.cpu_count()):
        self.queue_in = multiprocessing.Queue()
        self.queue_out = multiprocessing.Queue()
        self.terminator = multiprocessing.Event()
        self.operating = multiprocessing.Event()
        self.lock = multiprocessing.Lock()
        self.processes = []
        for _ in range(number):
            p = multiprocessing.Process(target=worker_function,
                                        args=(function, self.operating, self.queue_in, self.queue_out, self.terminator, self.lock))
            self.processes.append(p)
    def start(self):
        self.operating.set()
        for p in self.processes:
            p.start()
    def put(self, info):
        self.queue_in.put(info)
    def get(self):
        return self.queue_out.get()
    def pause(self):
        self.operating.clear()
    def resume(self):
        self.operating.set()
    def terminate(self):
        self.operating.set()
        self.terminator.set()
        self.queue_in.close()
        for p in self.processes:
            p.join()
if __name__ == "__main__":
    import time
    def example_function(x):
        time.sleep(1)
        return x * x
    slaves = Slaves(function=example_function, number=4)
    slaves.start()
    for i in range(10):
        slaves.put(i)
    for _ in range(10):
        print(slaves.get())
    slaves.terminate()