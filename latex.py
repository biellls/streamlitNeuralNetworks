from io import BytesIO

import matplotlib.pyplot as plt
import streamlit as st


def render_latex(formula, fontsize=12, dpi=300):
    """Renders LaTeX formula into Streamlit."""
    fig = plt.figure()
    text = fig.text(0, 0, '$%s$' % formula, fontsize=fontsize)

    fig.savefig(BytesIO(), dpi=dpi)  # triggers rendering

    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.05
    fig.set_size_inches((width, height))

    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))

    buffer = BytesIO()
    fig.savefig(buffer, dpi=dpi, format='jpg')
    plt.close(fig)

    st.image(buffer)
