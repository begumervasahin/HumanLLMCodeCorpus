from feature_type import *
class NaiveBayes:
    def __init__(self, sensor_name, feature_weights, satisfaction_threshold):
        self.__satisfactions = []
        self.__sensor_name = sensor_name
        self.__feature_weights = feature_weights
        self.__cpt = {}
        self.__satisfaction_threshold = satisfaction_threshold
        self.__total_interactions = 0
        self.__success_interactions = 0
        self.__reputation_history = {}
        self.__simulation_steps = 0
    def add_satisfaction(self, satisfaction):
        self.__satisfactions.append(satisfaction)
        self.__cpt[satisfaction.get_feature_type()] = 0
        self.__reputation_history[satisfaction.get_feature_type()] = []
    def compute(self, data):
        self.__total_interactions += 1
        satisfaction_score = 0
        for satisfaction in self.__satisfactions:
            feature_type = satisfaction.get_feature_type()
            satisfaction_score += self.__feature_weights[feature_type] * satisfaction.get_satisfaction(data)
        if satisfaction_score >= self.__satisfaction_threshold:
            self.__success_interactions += 1
            for satisfaction in self.__satisfactions:
                feature_type = satisfaction.get_feature_type()
                if satisfaction.get_satisfaction(data) >= self.__feature_weights[feature_type] * self.__satisfaction_threshold:
                    self.__cpt[feature_type] += 1
    def __get_feature_reputation(self, feature):
        if self.__total_interactions == 0 or self.__success_interactions == 0:
            return (0, 0)
        trust_probability = self.__success_interactions / self.__total_interactions
        feature_probability = self.__cpt[feature] / self.__total_interactions
        return (feature_probability / trust_probability, trust_probability)
    def save_reputation(self):
        for feature in self.__cpt.keys():
            self.__reputation_history[feature].append(self.__get_feature_reputation(feature))
        self.__simulation_steps += 1
    def get_reputation_history(self, features):
        reputation_history = []
        for i in range(self.__simulation_steps):
            reputation_score = self.__reputation_history[features[0]][i][1]
            for feature in features:
                reputation_score *= self.__reputation_history[feature][i][0]
            reputation_history.append(reputation_score)
        return reputation_history
if __name__ == "__main__":
    feature_weights = {'feature1': 0.3, 'feature2': 0.7}
    satisfaction_threshold = 0.5
    nb = NaiveBayes(sensor_name="Sensor1", feature_weights=feature_weights, satisfaction_threshold=satisfaction_threshold)
    satisfaction1 = FeatureSatisfaction('feature1')
    satisfaction2 = FeatureSatisfaction('feature2')
    nb.add_satisfaction(satisfaction1)
    nb.add_satisfaction(satisfaction2)
    data = {}
    nb.compute(data)
    nb.save_reputation()
    features = ['feature1', 'feature2']
    reputation_history = nb.get_reputation_history(features)
    print(reputation_history)