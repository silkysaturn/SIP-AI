import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#-------------------------------------------------#

## AI INTERVIEW




#-------------------------------------------------#


# Sample Data
data = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2020', periods=100),
    'Value': np.random.randn(100).cumsum()
})

# Set the title of the app
st.title("My Streamlit Dashboard")

# Display data
st.subheader("Sample Data")
st.write(data.head())

# Slider and display selected value
slider_value = st.slider('Select a range of values', 0, 100, (25, 75))
st.write(f'Selected range: {slider_value}')


# Matplotlib Plot
st.subheader("Seaborn Line Plot")
plt.figure(figsize=(10, 5))
sns.lineplot(data=data, x='Date', y='Value')
st.pyplot(plt)

# Sidebar
st.sidebar.title("Sidebar Options")
sidebar_option = st.sidebar.radio('Choose a view', ['View 1', 'View 2', 'View 3'])
st.sidebar.write(f'Selected: {sidebar_option}')

# Display Columns Layout
col1, col2 = st.columns(2)

with col1:
    st.header('Column 1')
    st.write('This is the first column.')

with col2:
    st.header('Column 2')
    st.write('This is the second column.')
