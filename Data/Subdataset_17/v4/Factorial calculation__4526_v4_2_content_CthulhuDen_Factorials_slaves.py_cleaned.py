import multiprocessing
def worker_function(task_function, operating_event, input_queue, output_queue, terminate_event, lock):
    while not terminate_event.is_set():
        operating_event.wait()
        with lock:
            if not input_queue.empty():
                task = input_queue.get()
                result = task_function(task)
                output_queue.put(result)
    output_queue.close()
class Slaves:
    def __init__(self, task_function, num_processes=None):
        if num_processes is None:
            num_processes = multiprocessing.cpu_count()
        self.input_queue = multiprocessing.Queue()
        self.output_queue = multiprocessing.Queue()
        self.terminate_event = multiprocessing.Event()
        self.operating_event = multiprocessing.Event()
        self.lock = multiprocessing.Lock()
        self.processes = [
            multiprocessing.Process(
                target=worker_function,
                args=(
                    task_function,
                    self.operating_event,
                    self.input_queue,
                    self.output_queue,
                    self.terminate_event,
                    self.lock
                )
            )
            for _ in range(num_processes)
        ]
    def start(self):
        self.operating_event.set()
        for process in self.processes:
            process.start()
    def put(self, task):
        self.input_queue.put(task)
    def get(self):
        return self.output_queue.get()
    def pause(self):
        self.operating_event.clear()
    def resume(self):
        self.operating_event.set()
    def terminate(self):
        self.operating_event.set()
        self.terminate_event.set()
        self.input_queue.close()
        for process in self.processes:
            process.join()
if __name__ == "__main__":
    def example_function(x):
        import time
        time.sleep(1)
        return x * x
    slaves = Slaves(task_function=example_function, num_processes=4)
    slaves.start()
    for i in range(10):
        slaves.put(i)
    for _ in range(10):
        print(slaves.get())
    slaves.terminate()