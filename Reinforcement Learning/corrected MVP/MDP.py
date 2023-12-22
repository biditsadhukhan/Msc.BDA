import random

def vector_add(a, b):
    """Vector addition."""
    return (a[0] + b[0], a[1] + b[1])

def turn_right(orientation):
    """Turn the orientation to the right."""
    return (orientation[1], -orientation[0])

def turn_left(orientation):
    """Turn the orientation to the left."""
    return (-orientation[1], orientation[0])

def update(obj, **kwargs):
    """Update object attributes."""
    obj.__dict__.update(kwargs)

class MDP:
    def __init__(self, init, actlist, terminals, gamma=0.9):
        self.init = init
        self.actlist = actlist
        self.terminals = terminals
        self.gamma = gamma
        self.states = set()
        self.reward = {}

    def R(self, state):
        """Return a numeric reward for this state."""
        return self.reward[state]

    def T(self, state, action):
        """Transition model. From a state and an action, return a list
        of (result-state, probability) pairs."""
        raise NotImplementedError("Subclasses must implement this method")

    def actions(self, state):
        """Set of actions that can be performed in this state."""
        if state in self.terminals:
            return [None]
        else:
            return self.actlist

class GridMDP(MDP):
    def __init__(self, grid, terminals, init=(0, 0), gamma=0.9):
        grid.reverse()
        super().__init__(init, actlist=[(1, 0), (0, 1), (-1, 0), (0, -1)], terminals=terminals, gamma=gamma)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        for x in range(self.cols):
            for y in range(self.rows):
                self.reward[(x, y)] = grid[y][x]
                if grid[y][x] is not None:
                    self.states.add((x, y))

    def T(self, state, action):
        if action is None:
            return [(0.0, state)]
        else:
            return [(0.8, self.go(state, action)),
                    (0.1, self.go(state, turn_right(action))),
                    (0.1, self.go(state, turn_left(action)))]

    def go(self, state, direction):
        state1 = vector_add(state, direction)
        return state1 if state1 in self.states else state

    def to_grid(self, mapping):
        return list(reversed([[mapping.get((x, y), None) for x in range(self.cols)] for y in range(self.rows)]))

    def to_arrows(self, policy):
        chars = {(1, 0): '>', (0, 1): '^', (-1, 0): '<', (0, -1): 'v', None: '.'}
        return self.to_grid({s: chars[a] for s, a in policy.items()})

def value_iteration(mdp, epsilon=0.001):
    U1 = {s: 0 for s in mdp.states}
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)]) for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
             return U

def best_policy(mdp, U):
    pi = {}
    for s in mdp.states:
        pi[s] = max(mdp.actions(s), key=lambda a: expected_utility(a, s, U, mdp))
    return pi

def expected_utility(a, s, U, mdp):
    return sum([p * U[s1] for (p, s1) in mdp.T(s, a)])

def policy_iteration(mdp):
    U = {s: 0 for s in mdp.states}
    pi = {s: random.choice(mdp.actions(s)) for s in mdp.states}
    while True:
        U = policy_evaluation(pi, U, mdp)
        unchanged = True
        for s in mdp.states:
            a = max(mdp.actions(s), key=lambda a: expected_utility(a, s, U, mdp))
            if a != pi[s]:
                pi[s] = a
                unchanged = False
        if unchanged:
            return pi

def policy_evaluation(pi, U, mdp, k=20):
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for i in range(k):
        for s in mdp.states:
            U[s] = R(s) + gamma * sum([p * U[s] for (p, s1) in T(s, pi[s])])
    return U



if __name__ == "__main__":
    grid = [[-0.04, -0.04, -0.04, +1],
            [-0.04, None, -0.04, -1],
            [-0.04, -0.04, -0.04, -0.04]]
    terminals = [(3, 2), (3, 1)]

    mdp = GridMDP(grid, terminals)

    U = value_iteration(mdp)
    pi = best_policy(mdp, U)

    print("Optimal Policy:")
    print(pi)
    display_policy_with_arrows(pi)

