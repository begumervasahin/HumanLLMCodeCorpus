import unittest
import time
from job import Job
class TestJob(unittest.TestCase):
    def test_instantiation(self):
        try:
            job = Job()
        except NameError:
            self.fail("Failed to instantiate Job.")
        self.assertIsInstance(job, Job, "Job instance creation failed.")
def generate_fake_value():
    return f"FAKE {time.time()}"
if __name__ == '__main__':
    unittest.main()