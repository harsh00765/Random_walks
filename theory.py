import numpy as np


# 1D Random walk

def theoretical_mean():
    return 0
def theoretical_msd_1d(n_steps, delta):
    return n_steps * delta**2
def theoretical_rms_1d(n_steps, delta):
    return np.sqrt(theoretical_msd_1d(n_steps, delta))
def diffusion_coefficient_1d(delta, tau):
    return delta**2 / (2 * tau)

# 2D Random walk

def theoretical_msd_2d(n_steps, delta):
    return n_steps * delta**2
def theoretical_rms_2d(n_steps, delta):
    return np.sqrt(theoretical_msd_2d(n_steps, delta))
def diffusion_coefficient_2d(delta, tau):
    return delta**2 / (4 * tau)

# 3D Random walk

def theoretical_msd_3d(n_steps, delta):
    return n_steps * delta**2
def theoretical_rms_3d(n_steps, delta):
    return np.sqrt(theoretical_msd_3d(n_steps, delta))
def diffusion_coefficient_3d(delta, tau):
    return delta**2 / (6 * tau)