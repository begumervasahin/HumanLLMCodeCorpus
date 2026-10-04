import unittest
from SentimentPredictor import SentimentPredictor
from driver_3 import imdb_data_preprocess
class class1:
    def fonk1(self, msg):
        pass
class class2(class1):
    def fonk2(self, msg):
        print()
def fonk3():
    return []
class class3(unittest.TestCase):
    def fonk4(self):
        b1 = SentimentPredictor().build()
        self.assertIsNotNone(b1)
    def fonk5(self):
        b1 = SentimentPredictor().with_reporter(class2()).build()
        self.assertIsNotNone(b1)
    def fonk6(self):
        b1 = SentimentPredictor().with_reporter(class2()).build()
        b2 = fonk3()
        b1.fit()
        b3 = [b1.predict(x) for x in b2]
        self.assertIsNotNone(b3)
class class4(unittest.TestCase):
    def fonk7(self):
        imdb_data_preprocess('./')
    def fonk8(self):
        imdb_data_preprocess('./', b4 = True)
if b5 = = '__main__':
    unittest.main()