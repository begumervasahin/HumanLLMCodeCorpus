import time
class StopWatch:
    def __init__(self, component=None, noisy=False):
        self.component = component
        self.noisy = noisy
        self.reset()
    @property
    def finishtime(self):
        return self._finishtime
    def stop(self):
        self._finishtime = time.time() - self._start_time
        return self.finishtime
    def finish(self):
        self._finishtime = self.stop()
        if self.noisy:
            print(f"{self.component} took {self}")
    def reset(self):
        self._finishtime = None
        self._start_time = time.time()
    def __str__(self):
        elapsed_time = self.stop()
        if elapsed_time < 1:
            return f"{round(1000 * elapsed_time)} ms"
        elif elapsed_time < 10:
            return f"{elapsed_time:.1f} sec"
        else:
            elapsed_seconds = round(elapsed_time)
            if elapsed_seconds < 60:
                return f"{elapsed_seconds} sec"
            elif elapsed_seconds < 3600:
                return f"{elapsed_seconds
            elif elapsed_seconds < 86400:
                return f"{elapsed_seconds
            else:
                days = elapsed_seconds
                elapsed_seconds %= 86400
                hours = elapsed_seconds
                elapsed_seconds %= 3600
                minutes = elapsed_seconds
                seconds = elapsed_seconds % 60
                return f"{days}-{hours}:{minutes:02d}:{seconds:02d} d-h:m:s"
    def __enter__(self):
        self.reset()
    def __exit__(self, type, value, traceback):
        self.finish()
if __name__ == "__main__":
    x = StopWatch("foobar", True)
    time.sleep(0.1)
    x.finish()
    print("Finish time:", x.finishtime)
    with StopWatch("foobar2", True):
        time.sleep(0.1)