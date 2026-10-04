import time
from threading import Thread, Timer
class CountDownTimer(Thread):
    def __init__(self, interval, target):
        super().__init__()
        self.target = target
        self.interval = interval
        self.stopped = False
        self.daemon = True
    def run(self):
        while not self.stopped:
            time.sleep(self.interval)
            self.target()
class ResetTimer:
    def __init__(self, interval, func_ptr, args=None):
        self.func_ptr = func_ptr
        self.interval = interval
        self.args = args if args is not None else []
        self.countdown_timer = self._create_timer()
    def _create_timer(self):
        return Timer(self.interval, self.func_ptr, self.args)
    def reset(self):
        self.stop()
        self.countdown_timer = self._create_timer()
        self.start()
    def start(self):
        self.countdown_timer.start()
    def stop(self):
        self.countdown_timer.cancel()
def example_function():
    print("Function called!")
if __name__ == "__main__":
    countdown_timer = CountDownTimer(1, example_function)
    countdown_timer.start()
    time.sleep(5)
    countdown_timer.stopped = True
    reset_timer = ResetTimer(2, example_function)
    reset_timer.start()
    time.sleep(3)
    reset_timer.reset()
    time.sleep(3)
    reset_timer.stop()