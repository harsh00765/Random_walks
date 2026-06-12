import streamlit as st
import numpy as np
from simulations import *
from theory import *

st.title("Random Walks in Biology")

N = st.slider("Number of particles", 100, 50000, 5000)
n_steps =st.slider("Number of steps", 10, 1000, 100)
delta = st.number_input("Step length", value = 1.0)

positions, final_positions = random_walk_1d(N, n_steps, delta)

mean_x = np.mean(final_positions)
msd = np.mean(final_positions**2)
rms = np.sqrt(msd)

st.subheader("Simulation")
st.write("Mean displacement =", mean_x)
st.write("Mean-squared displacement =", msd)
st.write("RMS displacement =", rms)

st.subheader("Theory")
st.write("Mean displacement =", theoretical_mean())
st.write("Mean-squared displacement =", theoretical_msd(n_steps, delta))
st.write("RMS displacement =", theoretical_rms(n_steps, delta))
