from qfunction import QFunction


class LinearQFunction(QFunction):
    def __init__(self, features, weights=None, default=0.0):
        self.features = features
        if weights == None:
            self.weights = [
                default
                for _ in range(0, features.num_actions())
                for _ in range(0, features.num_features())
            ]

    def update(self, state, action, delta):
        # update the weights
        feature_values = self.features.extract(state, action)
        # Print the lengths of self.weights and feature_values
        print(f"Length of self.weights: {len(self.weights)}")
        print(f"Length of feature_values: {len(feature_values)}")
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (delta * feature_values[i])

    def get_q_value(self, state, action):
        q_value = 0.0
        feature_values = self.features.extract(state, action)
        for i in range(len(feature_values)):
            q_value += feature_values[i] * self.weights[i]
        return q_value
