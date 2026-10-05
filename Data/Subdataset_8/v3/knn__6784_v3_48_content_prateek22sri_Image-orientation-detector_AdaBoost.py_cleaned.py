class Model:
    def __init__(self):
        self.model_type = "generic"
class AdaBoost(Model):
    def __init__(self):
        super().__init__()
        self.model_type = "AdaBoost"
adaboost_model = AdaBoost()
print(adaboost_model.model_type)
