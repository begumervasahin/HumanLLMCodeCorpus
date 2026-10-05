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
class Slaves:
    def __init__(self, function, number=None):
        if number is None:
            number = multiprocessing.cpu_count()
        self.queueIn = multiprocessing.Queue()
        self.queueOut = multiprocessing.Queue()
        self.terminator = multiprocessing.Event()
        self.operating = multiprocessing.Event()
        self.lock = multiprocessing.Lock()
        self.processes = []
        for _ in range(number):
            process = multiprocessing.Process(target=worker_function, args=(function, self.operating, self.queueIn, self.queueOut, self.terminator, self.lock))
            self.processes.append(process)
    def start(self):
        self.operating.set()
        for p in self.processes:
            p.start()
    def put(self, info):
        self.queueIn.put(info)
    def get(self):
        return self.queueOut.get()
    def terminate(self):
        self.operating.set()
        self.terminator.set()
        self.queueIn.close()
    def pause(self):
        self.operating.clear()
    def resume(self):
        self.operating.set()
if __name__ == "__main__":
    def square(x):
        return x ** 2
    slaves = Slaves(square)
    slaves.start()
    for i in range(10):
        slaves.put(i)
    for i in range(10):
        result = slaves.get()
        print("Result:", result)
    slaves.terminate()