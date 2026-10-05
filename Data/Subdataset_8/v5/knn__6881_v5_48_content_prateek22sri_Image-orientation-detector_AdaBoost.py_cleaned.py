from Model import Model
class AdaBoost(Model):
    def __init__(self):
        super().__init__()
        self.model_type = "adaboost"
ada_boost_model = AdaBoost()
print("AdaBoost model type:", ada_boost_model.model_type)