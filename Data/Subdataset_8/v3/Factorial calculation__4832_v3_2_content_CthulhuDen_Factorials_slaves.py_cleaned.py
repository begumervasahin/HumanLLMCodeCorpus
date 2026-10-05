import multiprocessing
def worker_function(function, operating, input_queue, output_queue, terminator, lock):
    while not terminator.is_set():
        operating.wait()
        lock.acquire()
        if not input_queue.empty():
            item = input_queue.get()
            lock.release()
            result = function(item)
            output_queue.put(result)
        else:
            lock.release()
    output_queue.close()
    return 0
class MultiprocessingPool:
    def __init__(self, function, num_processes=None):
        if num_processes is None:
            num_processes = multiprocessing.cpu_count()
        self.input_queue = multiprocessing.Queue()
        self.output_queue = multiprocessing.Queue()
        self.terminator = multiprocessing.Event()
        self.operating = multiprocessing.Event()
        self.lock = multiprocessing.Lock()
        self.processes = []
        for _ in range(num_processes):
            process = multiprocessing.Process(target=worker_function, args=(function, self.operating, self.input_queue, self.output_queue, self.terminator, self.lock))
            self.processes.append(process)
    def start(self):
        self.operating.set()
        for process in self.processes:
            process.start()
    def put(self, item):
        self.input_queue.put(item)
    def get(self):
        return self.output_queue.get()
    def terminate(self):
        self.operating.set()
        self.terminator.set()
        self.input_queue.close()
    def pause(self):
        self.operating.clear()
    def resume(self):
        self.operating.set()
if __name__ == "__main__":
    def square(x):
        return x ** 2
    pool = MultiprocessingPool(square)
    pool.start()
    for i in range(10):
        pool.put(i)
    for _ in range(10):
        result = pool.get()
        print("Result:", result)
    pool.terminate()