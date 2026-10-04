import unittest
from SentimentPredictor import SentimentPredictor
from driver_3 import imdb_data_preprocess
class Reporter:
    def write(self, msg):
        pass
class NullReporter(Reporter):
    def write(self, msg):
        print()
def generate_corpus():
    return []
class TestPredictorBuilder(unittest.TestCase):
    def setUp(self):
        self.default_predictor = SentimentPredictor()
        self.null_reporter = NullReporter()
    def test_can_create_from_default(self):
        sut = self.default_predictor.build()
        self.assertIsNotNone(sut, "SentimentPredictor should be instantiated successfully")
    def test_can_inject_console_reporter(self):
        sut = self.default_predictor.with_reporter(self.null_reporter).build()
        self.assertIsNotNone(sut, "SentimentPredictor with injected reporter should be instantiated successfully")
    def test_can_run_on_default_test_data(self):
        sut = self.default_predictor.with_reporter(self.null_reporter).build()
        corpus = generate_corpus()
        sut.fit()
        results = [sut.predict(x) for x in corpus]
        self.assertIsNotNone(results, "Results should not be None after prediction")
class ImdbDataPreprocessTests(unittest.TestCase):
    def test_run(self):
        imdb_data_preprocess('./')
    def test_run_mixed(self):
        imdb_data_preprocess('./', mix=True)
if __name__ == '__main__':
    unittest.main()