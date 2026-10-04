class Model:
    def __init__(self):
        self.model_type = "base_model"
class AdaBoost(Model):
    def __init__(self):
        super().__init__()
        self.model_type = "adaboost"
if __name__ == "__main__":
    ada_boost_model = AdaBoost()
    print(f"The model type is: {ada_boost_model.model_type}")