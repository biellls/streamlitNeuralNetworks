from typing import NamedTuple

import matplotlib.pylab as pl
import numpy as np
import streamlit as st

from latex import render_latex
from neural_network_graphviz import render_graph
from plotting import plot_equation

index = {
    'Architecture Diagram': True,
    'General Equations': True,
    'Activation Functions': True,
}


st.header('Neural Networks')
st.subheader("Index")
for section in index:
    index[section] = st.checkbox(section, value=True)

section = 'Architecture Diagram'
if index[section]:
    st.subheader(section)
    n_layers = st.sidebar.slider('Number of layers', min_value=1, max_value=4)
    layers = [0]*(n_layers+1)
    layers[0] = st.sidebar.slider(f'Neurons in input layer', min_value=1, max_value=4)
    for n_layer in range(1, n_layers):
        layers[n_layer] = st.sidebar.slider(f'Neurons in layer {n_layer}', min_value=2, max_value=10)
    layers[-1] = st.sidebar.slider(f'Neurons in output layer', min_value=1, max_value=4)

    st.graphviz_chart(render_graph(layers), width=800, height=400)

section = 'General Equations'
if index[section]:
    st.subheader(section)
    render_latex(r'Z_i = w^TA_{i-1} +b')
    # render_latex(r'A_i = \sigma(A_i)')
    render_latex(r'A_i = g(A_i)')

section = 'Activation Functions'
if index[section]:
    st.subheader(section)
    st.selectbox('Activation Function', ('Sigmoid', 'ReLU', 'Leaky ReLU'))
    # plot_equation(lambda x: x*x)

# m_examples = st.slider('Training size', min_value=2, max_value=30)
# n_neurons = st.slider('Number of neurons', min_value=2, max_value=10)

# @st.cache
# def create_training_set(m, n):
#     return np.random.randn((m, n))
#
#
# W = np.zeros((m_examples, n_neurons))
#
# matrix = st.radio('Show Matrix', ('W', 'X', 'B'))
# if matrix == 'W':
#     st.dataframe(W)
# elif matrix == 'X':
#     st.write('X')
# else:
#     st.write('B')
