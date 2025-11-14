import streamlit as st 
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 
 
# Page configuration 
st.set_page_config(page_title="🌈 Interactive and Colorful Data Dashboard", 
layout="wide") 
st.markdown("<h1 style='text-align:center; color:#FF6347;'>🚀 Supercharged 
Interactive Data Dashboard</h1>", unsafe_allow_html=True) 
 
# Sidebar: Upload and Theme 
st.sidebar.markdown("## 📁 Upload & Options") 
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type="csv") 
 
# Dark/Light Theme Toggle 
theme = st.sidebar.radio("🌓 Select Theme", ["Light", "Dark"]) 
 
# Track theme across reruns 
if 'theme' not in st.session_state: 
st.session_state.theme = theme 
else: 
st.session_state.theme = theme 
 
# Load Data 
if uploaded_file: 
try: 
df = pd.read_csv(uploaded_file) 
st.success("✅ File uploaded successfully!") 
df.dropna(axis=1, how='all', inplace=True) # Drop empty columns 
 
 
 
 
'category']).columns.tolist() 
# Summary Metrics 
col1, col2, col3 = st.columns(3) 
col1.metric("📊 Numeric Columns", len(numeric_cols)) 
col2.metric("🔠 Categorical Columns", len(cat_cols)) 
col3.metric("📦 Total Rows", df.shape[0]) 
 
# Sidebar Filters 
st.sidebar.markdown("### Filter Settings") 
filters_df = df.copy() 
# Column classification  
numeric_cols 
'float64']).columns.tolist() 
cat_cols = 
= df.select_dtypes(include=['int64', 
 
df.select_dtypes(include=['object', 
26  
if cat_cols: 
selected_category = st.sidebar.selectbox("Select Category to Filter", 
cat_cols) 
selected_values = st.sidebar.multiselect("Filter Values", 
df[selected_category].dropna().unique()) 
if selected_values: 
filters_df = 
filters_df[filters_df[selected_category].isin(selected_values)] 
 
for col in numeric_cols[:3]: # Limit filters to 3 for performance 
min_val, max_val = float(df[col].min()), float(df[col].max()) 
sel_min, sel_max = st.sidebar.slider(f"Filter {col}", min_val, 
max_val, (min_val, max_val)) 
filters_df = filters_df[(filters_df[col] >= sel_min) & 
(filters_df[col] <= sel_max)] 
 
# Reset filters button 
if st.sidebar.button("🔄 Reset Filters"): 
st.experimental_rerun() 
 
# Data View Options 
view_choice = st.radio("📊 Choose Data to Display", ["Filtered Data", 
"Original Data"]) 
display_df = filters_df if view_choice == "Filtered Data" else df 
st.markdown(f"### 📋 {view_choice} Preview") 
st.dataframe(display_df.style.highlight_max(axis=0).highlight_min(axis=0), 
use_container_width=True) 
 
# Summary Statistics 
if st.checkbox("📈 Show Summary Statistics"): 
st.write(display_df.describe(include='all')) 
 
# Sidebar: Chart Configuration 
st.sidebar.markdown("### 📊 Chart Options") 
chart_type = st.sidebar.selectbox("Chart Type", ["Scatter", "Line", 
"Histogram", "Box", "Heatmap", "Pie", "Bar", "Area", "Violin", "Treemap"]) 
chart_title = st.sidebar.text_input("Chart Title", value="📊 Interactive 
Data Chart") 
chart_size = st.sidebar.selectbox("Chart Size", ["Small", "Medium", 
"Large"]) 
chart_width = {"Small": 400, "Medium": 700, "Large": 1000}[chart_size] 
chart_height = {"Small": 300, "Medium": 500, "Large": 700}[chart_size] 
fig = None # Initialize chart 
# Chart Generation Logic 
if chart_type == "Scatter": 
x = st.sidebar.selectbox("X-axis", numeric_cols) 
y = st.sidebar.selectbox("Y-axis", numeric_cols) 
color = st.sidebar.selectbox("Color by", [None] + cat_cols) 
27  
fig = px.scatter(filters_df, x=x, y=y, color=color, 
title=chart_title) 
elif chart_type == "Line": 
x = st.sidebar.selectbox("X-axis", numeric_cols + cat_cols) 
y = st.sidebar.selectbox("Y-axis", numeric_cols) 
color = st.sidebar.selectbox("Color by", [None] + cat_cols) 
fig = px.line(filters_df, x=x, y=y, color=color, title=chart_title) 
 
elif chart_type == "Histogram": 
col = st.sidebar.selectbox("Column", numeric_cols) 
bins = st.sidebar.slider("Bins", 5, 100, 30) 
fig = px.histogram(filters_df, x=col, nbins=bins, title=chart_title) 
 
elif chart_type == "Box": 
y = st.sidebar.selectbox("Y-axis", numeric_cols) 
x = st.sidebar.selectbox("Group by", cat_cols) 
color = st.sidebar.selectbox("Color by", [None] + cat_cols) 
fig = px.box(filters_df, x=x, y=y, color=color, title=chart_title) 
 
elif chart_type == "Heatmap": 
if len(numeric_cols) >= 2: 
corr = filters_df[numeric_cols].corr() 
fig = px.imshow(corr, text_auto=True, 
color_continuous_scale="RdBu_r", title=chart_title) 
else: 
st.warning("At least 2 numeric columns required for Heatmap.") 
 
elif chart_type == "Pie": 
labels = st.sidebar.selectbox("Labels", cat_cols) 
values = st.sidebar.selectbox("Values", numeric_cols) 
fig = px.pie(filters_df, names=labels, values=values, 
title=chart_title) 
 
elif chart_type == "Bar": 
x = st.sidebar.selectbox("X-axis", cat_cols) 
y = st.sidebar.selectbox("Y-axis", numeric_cols) 
color = st.sidebar.selectbox("Color by", [None] + cat_cols) 
fig = px.bar(filters_df, x=x, y=y, color=color, title=chart_title) 
 
elif chart_type == "Area": 
x = st.sidebar.selectbox("X-axis", numeric_cols + cat_cols) 
y = st.sidebar.selectbox("Y-axis", numeric_cols) 
color = st.sidebar.selectbox("Color by", [None] + cat_cols) 
fig = px.area(filters_df, x=x, y=y, color=color, title=chart_title) 
 
elif chart_type == "Violin": 
y = st.sidebar.selectbox("Y-axis", numeric_cols) 
x = st.sidebar.selectbox("Category", cat_cols) 
color = st.sidebar.selectbox("Color by", [None] + cat_cols) 
fig = px.violin(filters_df, y=y, x=x, color=color, box=True, 
points="all", title=chart_title) 
 
elif chart_type == "Treemap": 
28  
 
cat_cols) 
path_col = st.sidebar.multiselect("Hierarchy (Top to Bottom)", 
 
value_col = st.sidebar.selectbox("Size by", numeric_cols) 
if path_col: 
fig = px.treemap(filters_df, path=path_col, values=value_col, 
title=chart_title) 
else: 
st.warning("Select at least one category for Treemap hierarchy.") 
 
# Apply Theme 
if fig: 
fig.update_layout( 
width=chart_width, 
height=chart_height, 
hovermode="closest", 
template="plotly_dark" if theme == "Dark" else "plotly_white", 
plot_bgcolor="rgba(0,0,0,0)" if theme == "Dark" else 
"rgba(255,255,255,1)", 
paper_bgcolor="rgba(0,0,0,0)" if theme == "Dark" else 
"rgba(255,255,255,1)" 
) 
st.plotly_chart(fig, use_container_width=True) 
 
# Download Buttons 
st.download_button("⬇ Download Filtered Data", 
filters_df.to_csv(index=False), file_name="filtered_data.csv", mime="text/csv") 
 
except Exception as e: 
st.error(f"❌ Error loading file: {e}") 
 
else: 
st.info("📂 Please upload a CSV file to begin.