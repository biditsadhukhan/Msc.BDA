from qfunction import QFunction
import math

class NonLinearQFunction(QFunction):
    def __init__(self, features, weights=None, default=0.0):
        self.features = features
        if weights == None:
            self.weights = [
                default
                for _ in range(0, features.num_actions())
                for _ in range(0, features.num_features())
            ]

    def update(self, state, action, delta):
        # Update the weights using the sigmoid function
        feature_values = self.features.extract(state, action)
        for i in range(len(self.weights)):
            sigmoid_q = 1 / (1 + math.exp(-self.weights[i]*feature_values))
            self.weights[i] = self.weights[i] + (delta * (sigmoid_q * (1 - sigmoid_q) * feature_values[i]))

    def get_q_value(self, state, action):
        q_value = 0.0
        feature_values = self.features.extract(state, action)
        for i in range(len(feature_values)):
            q_value += 1/(1+math.exp(-feature_values[i] * self.weights[i]))
        return q_value
