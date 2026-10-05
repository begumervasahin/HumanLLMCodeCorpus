import unittest
import time
from job import Job
class class1(unittest.TestCase):
    def fonk1(self):
        try:
            Job()
        except NameError:
            self.fail("Could not instantiate Job.")
def fonk2():
    return f"FAKE {time.time()}"
if b1 = = '__main__':
    unittest.main()