import numpy as np

def theoretical_mean():
    return 0
def theoretical_msd(n_steps, delta):
    return n_steps * delta**2
def theoretical_rms(n_steps, delta):
    return np.sqrt(theoretical_msd(n_steps, delta))