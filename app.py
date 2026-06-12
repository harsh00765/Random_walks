import streamlit as st
import math
import pandas as pd
import numpy as np
from simulations import *
from theory import *
from plots import *

st.title("Random Walks in Biology")

N = st.slider("Number of particles", 100, 50000, 5000)
n_steps = st.slider("Number of steps", 10, 1000, 100)
tau = st.number_input("Time per step (τ)", value=1.0, min_value=0.0001)
delta = st.number_input("Step length", value=1.0)

dimension = st.selectbox("Dimension", ["1D", "2D", "3D"])

if dimension == "1D":
    positions, final_positions = random_walk_1d(N, n_steps,delta)
    mean_x = np.mean(final_positions)
    msd = np.mean(final_positions**2)
    rms = np.sqrt(msd)

    D = diffusion_coefficient_1d(delta,tau)

    st.subheader("Simulation")
    st.write("Mean displacement =", mean_x)
    st.write("Mean-square displacement =", msd)
    st.write("RMS displacement =", rms)

    st.subheader("Theory")
    st.write("Mean displacement =",theoretical_mean())
    st.write("Mean-square displacement =",theoretical_msd_1d(n_steps,delta))
    st.write("RMS displacement =",theoretical_rms_1d(n_steps,delta))
    st.write("Diffusion Coefficient D =",D)

    st.subheader("Sample Random Walks")
    st.pyplot(plot_sample_walks_1d(positions,n_walks=10))

    st.subheader("Final Position Histogram")
    st.pyplot(plot_histogram(final_positions))

    st.subheader("Binomial Distribution")
    st.pyplot(plot_binomial(n_steps,0.5))

    st.subheader("Histogram + Gaussian Theory")
    st.pyplot(plot_histogram_gaussian(final_positions,n_steps,delta))

    comparison = pd.DataFrame({"Quantity":["Mean","Mean-square","RMS"],"Simulation":[mean_x,msd,rms],"Theory":[theoretical_mean(),theoretical_msd_1d(n_steps,delta),theoretical_rms_1d(n_steps,delta)]})

    comparison["Absolute Error"] = abs(comparison["Simulation"] - comparison["Theory"])

    st.dataframe(comparison)


elif dimension == "2D":
    x_positions, y_positions, x_final, y_final = random_walk_2d(N, n_steps, delta)
    r2 = x_final**2 + y_final**2
    msd = np.mean(r2)
    rms = np.sqrt(msd)
    
    D = diffusion_coefficient_2d(delta, tau)

    st.subheader("Simulation")
    st.write("<r²> =", msd)
    st.write("RMS distance =", rms)

    st.subheader("Theory")
    st.write("<r²> =", theoretical_msd_2d(n_steps, delta))
    st.write("RMS distance =", theoretical_rms_2d(n_steps, delta))
    st.write("Diffusion Coefficient D =", D)

    st.subheader("Sample 2D Walks")
    st.pyplot(plot_sample_walks_2d(x_positions, y_positions))

    st.subheader("Final Particle Cloud")
    st.pyplot(plot_final_positions_2d(x_final, y_final))

    st.subheader("Distribution of r²")
    st.pyplot(plot_r2_histogram(r2))

elif dimension == "3D":
    x_positions, y_positions, z_positions, x_final, y_final, z_final = random_walk_3d(N, n_steps, delta)
    r2 = x_final**2 + y_final**2 + z_final**2
    msd = np.mean(r2)
    rms = np.sqrt(msd)

    D = diffusion_coefficient_3d(delta, tau)

    st.subheader("Simulation")
    st.write("<r²> =", msd)
    st.write("RMS distance =", rms)

    st.subheader("Theory")
    st.write("<r²> =", theoretical_msd_3d(n_steps, delta))
    st.write("RMS distance =", theoretical_rms_3d(n_steps, delta))
    st.write("Diffusion Coefficient D =", D)

    st.subheader("Sample 3D Walks")
    st.pyplot(plot_sample_walks_3d(x_positions, y_positions, z_positions))

    st.subheader("Final Particle Cloud")
    st.pyplot(plot_final_positions_3d(x_final, y_final, z_final))

    st.subheader("Distribution of r²")
    st.pyplot(plot_r2_histogram(r2))