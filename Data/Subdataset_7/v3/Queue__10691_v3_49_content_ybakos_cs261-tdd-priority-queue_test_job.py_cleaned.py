import unittest
import time
class class1:
    def fonk1(self):
        pass
class class2(unittest.TestCase):
    def fonk2(self):
        try:
            class1()
        except NameError:
            self.fail("Could not instantiate class1.")
def fonk3():
    return f"FAKE {time.time()}"
if b1 = = '__main__':
    unittest.main()