import time
from threading import Thread, Timer
class CountDownTimer(Thread):
    def __init__(self, interval, target):
        super().__init__()
        self.target = target
        self.interval = interval
        self.daemon = True
        self.stopped = False
    def run(self):
        while not self.stopped:
            time.sleep(self.interval)
            self.target()
class ResetTimer:
    def __init__(self, interval, func_ptr, args=None):
        if args:
            assert isinstance(args, list)
        self.func_ptr = func_ptr
        self.interval = interval
        self.args = args
        self.countdown_timer = self.new_timer()
    def new_timer(self):
        timer = Timer(self.interval, self.func_ptr, self.args)
        timer.daemon = True
        return timer
    def reset(self):
        self.stop()
        self.countdown_timer = self.new_timer()
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