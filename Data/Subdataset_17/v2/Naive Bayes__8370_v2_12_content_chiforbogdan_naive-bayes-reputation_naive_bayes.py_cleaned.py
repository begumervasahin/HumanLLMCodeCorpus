from feature_type import FeatureSatisfaction
class NaiveBayes:
    def __init__(self, sensor_name, feature_weights, satisfaction_threshold):
        self.satisfactions = []
        self.sensor_name = sensor_name
        self.feature_weights = feature_weights
        self.cpt = {}
        self.satisfaction_threshold = satisfaction_threshold
        self.total_interactions = 0
        self.success_interactions = 0
        self.reputation_history = {}
        self.simulation_steps = 0
    def add_satisfaction(self, satisfaction):
        self.satisfactions.append(satisfaction)
        feature_type = satisfaction.get_feature_type()
        self.cpt[feature_type] = 0
        self.reputation_history[feature_type] = []
    def compute(self, data):
        self.total_interactions += 1
        satisfaction_score = sum(
            self.feature_weights[satisfaction.get_feature_type()] * satisfaction.get_satisfaction(data)
            for satisfaction in self.satisfactions
        )
        if satisfaction_score >= self.satisfaction_threshold:
            self.success_interactions += 1
            for satisfaction in self.satisfactions:
                feature_type = satisfaction.get_feature_type()
                if satisfaction.get_satisfaction(data) >= self.feature_weights[feature_type] * self.satisfaction_threshold:
                    self.cpt[feature_type] += 1
    def _get_feature_reputation(self, feature):
        if self.total_interactions == 0 or self.success_interactions == 0:
            return (0, 0)
        trust_probability = self.success_interactions / self.total_interactions
        feature_probability = self.cpt[feature] / self.total_interactions
        return (feature_probability / trust_probability, trust_probability)
    def save_reputation(self):
        for feature in self.cpt:
            self.reputation_history[feature].append(self._get_feature_reputation(feature))
        self.simulation_steps += 1
    def get_reputation_history(self, features):
        reputation_history = []
        for step in range(self.simulation_steps):
            reputation_score = self.reputation_history[features[0]][step][1]
            for feature in features:
                reputation_score *= self.reputation_history[feature][step][0]
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