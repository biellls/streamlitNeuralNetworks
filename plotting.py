from typing import Callable, Tuple

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def plot_equation(f: Callable[[float], float], linspace: Tuple[float, float] = (-50., 50.)):
    x = np.linspace(0.2, *linspace)

    fig, ax = plt.subplots()
    ax.plot(x, f(x))
    ax.grid(True, which='both')

    ax.set_xlim(linspace)
    ax.set_ylim((-100., 100.))

    st.pyplot(fig)
