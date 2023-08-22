import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title("Data Visualization with Streamlit")

# Load sample data
data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100)
})

# Sidebar section
st.sidebar.header("Settings")

# Scatter plot customization
scatter_color = st.sidebar.color_picker("Choose scatter plot color", '#1f77b4')
scatter_size = st.sidebar.slider("Choose scatter plot size", 10, 100, 30)

# Show scatter plot
st.subheader("Scatter Plot")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='x', y='y', color=scatter_color, s=scatter_size, ax=ax)
st.pyplot(fig)

# Line chart customization
line_color = st.sidebar.color_picker("Choose line color", '#ff7f0e')
line_style = st.sidebar.selectbox("Choose line style", ['solid', 'dashed', 'dotted'])

# Show line chart
st.subheader("Line Chart")
fig, ax = plt.subplots()
sns.lineplot(data=data, x='x', y='y', color=line_color, linestyle=line_style, ax=ax)
st.pyplot(fig)

# Footer
st.markdown("---")
st.write("Created with ❤️ by Your Name")
