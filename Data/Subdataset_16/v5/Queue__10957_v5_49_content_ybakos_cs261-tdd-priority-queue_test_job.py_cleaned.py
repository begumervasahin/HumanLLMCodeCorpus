import unittest
import time
from b1 import Job
class class1(unittest.TestCase):
    def fonk1(self):
        try:
            b1 = Job()
        except NameError:
            self.fail("Failed to instantiate Job.")
        self.assertIsInstance(b1, Job, "Job instance creation failed.")
def fonk2():
    return f"FAKE {time.time()}"
if b2 = = '__main__':
    unittest.main()