import numpy as np
def random_walk_1d(N, n_steps, delta,):
    steps = np.random.choice([-delta, delta], size=(N, n_steps))
    positions = np.cumsum(steps, axis=1)
    final_positions = positions[:, -1]
    return positions, final_positions 

def random_walk_2d(N, n_steps, delta):
    directions = np.random.randint(0, 4, size=(N, n_steps))
    dx = np.zeros((N, n_steps))
    dy = np.zeros((N, n_steps))

    dx[directions == 0] = delta
    dx[directions == 1] = -delta
    dy[directions == 2] = delta
    dy[directions == 3] = -delta

    x_positions = np.cumsum(dx, axis=1)
    y_positions = np.cumsum(dy, axis=1)

    x_final = x_positions[:, -1]
    y_final = y_positions[:, -1]

    return x_positions, y_positions, x_final, y_final

def random_walk_3d(N, n_steps, delta):
    directions = np.random.randint(0, 6, size=(N, n_steps))
    dx = np.zeros((N, n_steps))
    dy = np.zeros((N, n_steps))
    dz = np.zeros((N, n_steps))

    dx[directions == 0] = delta
    dx[directions == 1] = -delta
    dy[directions == 2] = delta
    dy[directions == 3] = -delta
    dz[directions == 4] = delta
    dz[directions == 5] = -delta

    x_positions = np.cumsum(dx, axis=1)
    y_positions = np.cumsum(dy, axis=1)
    z_positions = np.cumsum(dz, axis=1)

    x_final = x_positions[:, -1]
    y_final = y_positions[:, -1]
    z_final = z_positions[:, -1]

    return x_positions, y_positions, z_positions, x_final, y_final, z_final