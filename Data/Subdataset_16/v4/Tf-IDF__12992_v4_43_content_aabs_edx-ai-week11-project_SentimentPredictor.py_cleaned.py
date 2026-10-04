from sklearn.linear_model import SGDClassifier
from SentimentPredictorImpl import SentimentPredictorImpl
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = SGDClassifier()
    def fonk2(self, b5):
        self.b5 = b5
        return self
    def fonk3(self, b3):
        self.b3 = b3
        return self
    def fonk4(self, b4):
        self.b4 = b4
        return self
    def fonk5(self, b2):
        self.b2 = b2
        return self
    def fonk6(self, b1):
        self.b1 = b1
        return self
    def fonk7(self) -> SentimentPredictorImpl:
        return SentimentPredictorImpl(
            self.b5,
            self.b4,
            self.b3,
            self.b2,
            self.b1,
            self.b6
        )