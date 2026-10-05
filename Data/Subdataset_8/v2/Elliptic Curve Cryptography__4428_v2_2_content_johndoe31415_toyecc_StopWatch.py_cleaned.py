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
        self._finishtime = time.time() - self._t
        return self.finishtime
    def finish(self):
        self._finishtime = self.stop()
        if self._noisy:
            print(f"{self._component} took {str(self)}")
    def reset(self):
        self._finishtime = None
        self._t = time.time()
    def __str__(self):
        t = self.stop()
        if t < 1:
            return f"{round(1000 * t)} ms"
        elif t < 10:
            return f"{t:.1f} sec"
        else:
            tint = round(t)
            if tint < 60:
                return f"{tint} sec"
            elif tint < 3600:
                return f"{tint
            elif tint < 86400:
                return f"{tint
            else:
                return f"{tint
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