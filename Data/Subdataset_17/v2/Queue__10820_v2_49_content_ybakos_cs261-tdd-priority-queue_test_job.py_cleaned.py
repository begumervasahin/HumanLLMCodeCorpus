import unittest
import time
class Job:
    def __init__(self, priority=0, description=''):
        self.priority = priority
        self.description = description
    def __eq__(self, other):
        return self.priority == other.priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __str__(self):
        return f"Job(priority={self.priority}, description='{self.description}')"
class TestJob(unittest.TestCase):
    def test_instantiation(self):
        try:
            Job()
        except NameError:
            self.fail("Could not instantiate Job.")
    def test_comparison(self):
        job1 = Job(priority=1)
        job2 = Job(priority=2)
        job3 = Job(priority=1)
        self.assertTrue(job1 < job2, "Job with lower priority should be less than job with higher priority.")
        self.assertTrue(job2 > job1, "Job with higher priority should be greater than job with lower priority.")
        self.assertFalse(job1 == job2, "Jobs with different priorities should not be equal.")
        self.assertTrue(job1 == job3, "Jobs with the same priority should be equal.")
    def test_string_representation(self):
        job = Job(priority=1, description="Test job")
        self.assertEqual(str(job), "Job(priority=1, description='Test job')")
def fake_value():
    return f"FAKE {time.time()}"
if __name__ == '__main__':
    unittest.main()