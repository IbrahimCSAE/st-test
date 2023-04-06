# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:11:51 2023

@author: Marwan
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
heart_data = pd.read_csv('C:/Users\Marwan\Desktop\Model\pages/heart_cleveland.csv')

# Create histogram of age variable
fig, ax = plt.subplots()
bins = np.arange(20, 90, 5)
ax.hist(heart_data['age'], bins=bins)
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Age')
st.pyplot(fig)

# Add slider widget to adjust bin size
bin_size = st.slider('Bin Size', min_value=1, max_value=10, value=5)
bins = np.arange(20, 90, bin_size)
ax.clear()
ax.hist(heart_data['age'], bins=bins)
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Age')
st.pyplot(fig)
