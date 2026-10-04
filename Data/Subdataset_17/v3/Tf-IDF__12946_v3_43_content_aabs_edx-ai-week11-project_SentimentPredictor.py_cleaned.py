from sklearn.linear_model import SGDClassifier
class SentimentPredictorImpl:
    def __init__(self, training_data, test_data, training_labels, test_labels, reporter, cls):
        self.training_data = training_data
        self.test_data = test_data
        self.training_labels = training_labels
        self.test_labels = test_labels
        self.reporter = reporter
        self.cls = cls
        if self.training_data is not None and self.training_labels is not None:
            self.cls.fit(self.training_data, self.training_labels)
    def predict(self, data):
        return self.cls.predict(data)
    def score(self):
        if self.test_data is not None and self.test_labels is not None:
            return self.cls.score(self.test_data, self.test_labels)
        return None
class SentimentPredictor:
    def __init__(self):
        self.reporter = None
        self.test_labels = None
        self.training_labels = None
        self.test_data = None
        self.training_data = None
        self.cls = SGDClassifier()
    def with_training_data(self, training_data):
        self.training_data = training_data
        return self
    def with_training_labels(self, training_labels):
        self.training_labels = training_labels
        return self
    def with_test_data(self, test_data):
        self.test_data = test_data
        return self
    def with_test_labels(self, test_labels):
        self.test_labels = test_labels
        return self
    def with_reporter(self, reporter):
        self.reporter = reporter
        return self
    def build(self) -> SentimentPredictorImpl:
        return SentimentPredictorImpl(
            self.training_data,
            self.test_data,
            self.training_labels,
            self.test_labels,
            self.reporter,
            self.cls
        )
def main():
    training_data = [[0.1, 0.2], [0.2, 0.3], [0.3, 0.4]]
    training_labels = [0, 1, 0]
    test_data = [[0.2, 0.1], [0.3, 0.2]]
    test_labels = [0, 1]
    predictor = (SentimentPredictor()
                 .with_training_data(training_data)
                 .with_training_labels(training_labels)
                 .with_test_data(test_data)
                 .with_test_labels(test_labels)
                 .with_reporter(None)
                 .build())
    predictions = predictor.predict(test_data)
    score = predictor.score()
    print(f"Predictions: {predictions}")
    print(f"Score: {score}")
if __name__ == "__main__":
    main()