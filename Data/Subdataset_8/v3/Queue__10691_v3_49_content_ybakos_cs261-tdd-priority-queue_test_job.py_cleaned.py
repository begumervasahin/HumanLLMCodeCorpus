import unittest
import time
class Job:
    def __init__(self):
        pass
class TestJob(unittest.TestCase):
    def test_instantiation(self):
        try:
            Job()
        except NameError:
            self.fail("Could not instantiate Job.")
def fake_value():
    return f"FAKE {time.time()}"
if __name__ == '__main__':
    unittest.main()