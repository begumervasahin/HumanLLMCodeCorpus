import time
class StopWatch:
    def __init__(self, component=None, noisy=False):
        self._component = component
        self._noisy = noisy
        self.reset()
    @property
    def finishtime(self):
        return self._finishtime
    def stop(self):
        self._finishtime = time.time() - self._start_time
        return self.finishtime
    def finish(self):
        self.stop()
        if self._noisy:
            print(f"{self._component} took {self}")
    def reset(self):
        self._finishtime = None
        self._start_time = time.time()
    def __str__(self):
        elapsed_time = self.stop()
        if elapsed_time < 1:
            return f"{int(elapsed_time * 1000)} ms"
        elif elapsed_time < 60:
            return f"{elapsed_time:.2f} sec"
        else:
            minutes, seconds = divmod(int(elapsed_time), 60)
            if minutes < 60:
                return f"{minutes} min {seconds} sec"
            else:
                hours, minutes = divmod(minutes, 60)
                days, hours = divmod(hours, 24)
                if days > 0:
                    return f"{days} days {hours} hours {minutes} min {seconds} sec"
                return f"{hours} hours {minutes} min {seconds} sec"
    def __enter__(self):
        self.reset()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.finish()
if __name__ == "__main__":
    stopwatch = StopWatch("Example Task", True)
    time.sleep(0.1)
    stopwatch.finish()
    print(f"Elapsed time: {stopwatch.finishtime} seconds")
    with StopWatch("Example Task in Context Manager", True):
        time.sleep(0.1)