import numpy as np
def random_walk_1d(N, n_steps, delta):
    steps = np.random.choice([-delta, delta], size=(N, n_steps))
    positions = np.cumsum(steps, axis=1)
    final_positions = positions[:, -1]
    return positions, final_positions 