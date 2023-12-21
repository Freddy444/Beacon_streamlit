import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
github_data = pd.read_csv('/Users/freddyfabian/Downloads/archive (2)/github_dataset.csv')

# Page Configuration
st.set_page_config(page_title="GitHub Explorer", page_icon="🚀", layout="wide")

# Sidebar for user interaction
st.sidebar.title("GitHub Explorer Options")

# Data Exploration Section
st.title("🚀 GitHub Dataset Analysis")

# Dataset Overview
st.sidebar.subheader("Dataset Overview")
st.write("## Dataset Overview")
st.write(github_data.head())

# Numeric Columns Summary
st.sidebar.subheader("Numeric Columns Summary")
st.write("## Numeric Columns Summary")
st.write(github_data.describe())

# Number of Repositories by Language
st.sidebar.subheader("Number of Repositories by Language")
st.write("## Number of Repositories by Language")
language_counts_streamlit = github_data['language'].value_counts()
st.bar_chart(language_counts_streamlit)

# Box Plots for Numeric Columns by Language
st.sidebar.subheader("Box Plots for Numeric Columns by Language")
st.write("## Box Plots for Numeric Columns by Language")

numeric_columns_streamlit = ['stars_count', 'forks_count', 'issues_count', 'pull_requests', 'contributors']

for column in numeric_columns_streamlit:
    st.write(f"### {column} by Language")
    box_plot_streamlit = sns.catplot(data=github_data, kind='box', y='language', x=column, height=8, palette='viridis', hue='language', legend=False)
    plt.close()
    st.pyplot(box_plot_streamlit)

# Correlation Analysis
st.sidebar.subheader("Correlation Analysis")
st.write("## Correlation Analysis")

numeric_columns_only_streamlit = github_data.select_dtypes(include=['float64', 'int64'])
corr_heatmap_streamlit = sns.heatmap(numeric_columns_only_streamlit.corr(method='spearman'), cmap='coolwarm', annot=True)
st.pyplot(corr_heatmap_streamlit.figure)

# Data Cleaning Section
st.title("Data Cleaning")

# Original Data
st.write("### Original Data:")
st.write(github_data.head())

# Drop Rows with Missing Values
github_data_cleaned_streamlit = github_data.dropna()
st.write("### Data after removing rows with missing values:")
st.write(github_data_cleaned_streamlit.head())

# Language with the Highest Frequency
language_HF_streamlit = language_counts_streamlit.idxmax()
st.write(f"### Language with the highest frequency: {language_HF_streamlit}")

st.markdown("---")
st.markdown("Built with ❤️ by Your Name | 🚀 GitHub Dataset Explorer")
