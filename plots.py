import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D

def plot_sample_walks_1d(positions, n_walks=10):

    fig, ax = plt.subplots(figsize=(8,4))
    n_walks = min(n_walks, positions.shape[0])

    for i in range(n_walks):
        ax.plot(np.arange(1, positions.shape[1] + 1), positions[i], linewidth=1)

    ax.set_xlabel("Step number")
    ax.set_ylabel("Position")
    ax.set_title("Sample random walks")

    return fig

def plot_sample_walks_2d(x_positions, y_positions, n_walks=10):
    fig, ax = plt.subplots(figsize=(6,6))
    n_walks = min(n_walks, x_positions.shape[0])

    for i in range(n_walks):
        ax.plot(x_positions[i], y_positions[i], linewidth=1)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Sample 2D random walks")
    ax.axis('equal')

    return fig

def plot_final_positions_2d(x_final, y_final):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.scatter(x_final, y_final, alpha=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Final particle positions (2D)")
    ax.axis('equal')

    return fig

def plot_sample_walks_3d(x_positions, y_positions, z_positions, n_walks=10):
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111, projection='3d')
    n_walks = min(n_walks, x_positions.shape[0])

    for i in range(n_walks):
        ax.plot(x_positions[i], y_positions[i], z_positions[i])

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Sample 3D random walks")

    return fig

def plot_final_positions_3d(x_final, y_final, z_final):
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_final, y_final, z_final, alpha=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Final particle positions (3D)")

    return fig

def plot_histogram(final_positions):

    fig, ax = plt.subplots(figsize=(8,4))
    ax.hist(final_positions, bins=30)

    ax.set_xlabel("Final position")
    ax.set_ylabel("Number of particles")
    ax.set_title("Distribution of final positions")
    return fig
    
def plot_binomial(n,p):
    k = np.arange(n+1)
    probabilities = binom.pmf(k, n, p)

    fig, ax = plt.subplots()
    ax.bar(k, probabilities)
    ax.set_xlabel("Number of steps to the right")
    ax.set_ylabel("Probability")
    ax.set_title(f"Binomial Distribution (n={n}, p={p})")
    return fig

def plot_histogram_gaussian(final_positions,n_steps,delta):

    fig, ax = plt.subplots()
    ax.hist( final_positions,bins=40,density=True,alpha=0.6)
    ax.set_xlabel("Final position")
    ax.set_ylabel("Probability Density")
    sigma = np.sqrt(n_steps*delta**2)
    x = np.linspace(final_positions.min(),final_positions.max(),500)
    y = norm.pdf(x,0,sigma)
    ax.plot(x,y,linewidth=3)
    ax.set_title("Histogram + Gaussian Theory")
    return fig

def plot_r2_histogram(r2):

    fig, ax = plt.subplots(figsize=(8,4))

    ax.hist(r2, bins=40)

    ax.set_xlabel("r²")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of r²")

    return fig