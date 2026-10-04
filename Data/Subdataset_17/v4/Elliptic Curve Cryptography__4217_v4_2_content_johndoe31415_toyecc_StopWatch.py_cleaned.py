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
            return f"{round(1000 * elapsed_time)} ms"
        elif elapsed_time < 10:
            return f"{elapsed_time:.1f} sec"
        else:
            elapsed_seconds = round(elapsed_time)
            if elapsed_seconds < 60:
                return f"{elapsed_seconds} sec"
            elif elapsed_seconds < 3600:
                minutes, seconds = divmod(elapsed_seconds, 60)
                return f"{minutes}:{seconds:02d} m:s"
            elif elapsed_seconds < 86400:
                hours, remainder = divmod(elapsed_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                return f"{hours}:{minutes:02d}:{seconds:02d} h:m:s"
            else:
                days, remainder = divmod(elapsed_seconds, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)
                return f"{days}-{hours}:{minutes:02d}:{seconds:02d} d-h:m:s"
    def __enter__(self):
        self.reset()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.finish()
if __name__ == "__main__":
    stopwatch = StopWatch("foobar", True)
    time.sleep(0.1)
    stopwatch.finish()
    print(f"Elapsed time: {stopwatch.finishtime} seconds")
    with StopWatch("foobar2", True):
        time.sleep(0.1)