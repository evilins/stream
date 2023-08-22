import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title("Simple Streamlit App")

# Generate random data
data = np.random.randn(100)

# Create a histogram
st.subheader("Histogram")
plt.hist(data, bins=20)
st.pyplot()

# Show random numbers
st.subheader("Random Numbers")
st.write(data)
