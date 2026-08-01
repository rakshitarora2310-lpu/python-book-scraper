import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="E-Commerce Sales Analytics", layout="wide")

st.title("📊 Executive Sales & Revenue Analytics")
st.markdown("Interactive business intelligence dashboard tracking key performance metrics, product category margins, and unit performance.")

# Sample Data Generation
@st.cache_data
def load_data():
    data = {
        "Category": ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports"],
        "Revenue ($)": [45000, 28000, 19000, 12000, 15000],
        "Units Sold": [150, 420, 210, 310, 180],
        "Profit Margin (%)": [22, 35, 28, 40, 25]
    }
    return pd.DataFrame(data)

df = load_data()

# Executive KPI Summary Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${df['Revenue ($)'].sum():,}")
col2.metric("Total Units Sold", f"{df['Units Sold'].sum():,}")
col3.metric("Avg Profit Margin", f"{df['Profit Margin (%)'].mean():.1f}%")

st.divider()

# Interactive Visualizations
col_left, col_right = st.columns(2)

with col_left:
    fig_bar = px.bar(
        df, 
        x="Category", 
        y="Revenue ($)", 
        color="Profit Margin (%)",
        title="Revenue & Margin Distribution by Category",
        text_auto=True
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    fig_pie = px.pie(
        df, 
        names="Category", 
        values="Units Sold", 
        title="Unit Share by Category",
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)