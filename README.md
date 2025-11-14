Dynamic Data Visualization Dashboard

An interactive dashboard built using Python, Streamlit, Pandas, and Plotly that allows users to upload datasets, apply filters, and generate dynamic visualizations easily.

📌 Overview

This project provides an intuitive platform to explore data visually.
Users can upload CSV files, filter the data in real time, and create multiple types of charts for better understanding and decision-making.

🎯 Objectives

Allow users to upload and analyze datasets

Automatically detect numeric and categorical columns

Provide dynamic filtering options

Generate multiple interactive chart types

Support Light/Dark themes

Enable downloading of filtered datasets

🛠 Technologies Used

Python 3.8+

Streamlit

Pandas

Plotly Express

NumPy (optional)

✨ Key Features

📁 Upload CSV datasets

🧮 Automatic column classification

🔍 Advanced filters (categorical + numeric sliders)

📊 Interactive charts including:

Scatter

Line

Histogram

Box

Heatmap

Pie

Bar

Area

Violin

Treemap

🌗 Light / Dark Theme Toggle

📥 Download filtered data as CSV

📋 Summary statistics and data preview

🧱 System Architecture

User Interface Layer – Streamlit components

Application Layer – filter logic & chart configuration

Data Layer – Pandas preprocessing

Visualization Layer – Plotly interactive charts

Export Layer – CSV download

📂 Installation & Setup

Install dependencies:

pip install streamlit pandas plotly


Run the application:

streamlit run app.py


