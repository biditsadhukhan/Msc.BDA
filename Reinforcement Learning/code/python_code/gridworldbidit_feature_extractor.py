import numpy as np
from feature_extractor import FeatureExtractor
from gridworld import GridWorld

class GridWorldBiditFeatureExtractor(FeatureExtractor):
    def __init__(self, mdp):
        self.mdp = mdp
        self.forbidden_states = [(1, 1)]  # Define your forbidden states

    def num_features(self):
        return 11  # Adjust the number of features

    def num_actions(self):
        return len(self.mdp.get_actions())

    def extract(self, state, action):
        goal = (self.mdp.width - 1, self.mdp.height - 1)
        x = 0
        y = 1
        e = 0.01
        feature_values = []

        for a in self.mdp.get_actions():
            if a == action and state != GridWorld.TERMINAL:
                # Check if the next state after taking 'action' is forbidden
                next_state = self.mdp.get_transitions(state, action)
                is_forbidden = next_state in self.forbidden_states

                # Feature values for state and action
                feature_values += [(state[x] + e) / (goal[x] + e)]
                feature_values += [(state[y] + e) / (goal[y] + e)]
                feature_values += [
                    (goal[x] - state[x] + goal[y] - state[y] + e)
                    / (goal[x] + goal[y] + e)
                ]
                feature_values += [1 if goal[x] == state[x] else 0]
                feature_values += [1 if goal[y] == state[y] else 0]
                feature_values += [1 if action == 'UP' and state[x] < goal[x] and state[y] < goal[y] else 0]
                feature_values += [1 if state[x] < self.mdp.width / 2 and state[y] < self.mdp.height / 2 else 0]

                # Additional feature to indicate if the next state is forbidden
                feature_values += [1 if is_forbidden else 0]

                # Calculate direction to the nearest forbidden state
                nearest_forbidden_state = self.find_nearest_forbidden(state)
                direction_to_forbidden = self.calculate_direction(state, nearest_forbidden_state)
                feature_values += [direction_to_forbidden]

                # New feature: Angle to goal
                angle_to_goal = np.arctan2(goal[y] - state[y], goal[x] - state[x])
                feature_values += [angle_to_goal]

                # New feature: Check if the resulting state is valid
                valid_state = self.is_valid_state(state, action)
                feature_values += [1 if valid_state else 0]

            else:
                for _ in range(0, self.num_features()):
                    feature_values += [0.0]

        return feature_values

    def find_nearest_forbidden(self, state):
        nearest_distance = float('inf')
        nearest_forbidden = None
        for forbidden_state in self.forbidden_states:
            distance = np.linalg.norm(np.array(state) - np.array(forbidden_state))
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_forbidden = forbidden_state
        return nearest_forbidden

    def calculate_direction(self, from_state, to_state):
        direction = np.arctan2(to_state[1] - from_state[1], to_state[0] - from_state[0])
        return direction

    def is_valid_state(self, state, action):
        action_mapping = {
                    '▲': (0,1),
                    '▼': (0,-1),
                    '◄': (-1,0),
                    '►': (1,0),
                    'terminate': (3,2)
        }
        next_state = (state[0] + action_mapping[action][0], state[1] + action_mapping[action][1])
        return next_state not in self.mdp.blocked_states and next_state in self.mdp.get_states()
