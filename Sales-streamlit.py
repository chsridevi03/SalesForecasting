import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

# Page config
st.set_page_config(page_title="Sales Forecasting Dashboard", layout="wide")
st.title("📦 Superstore Sales Forecasting Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('train.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
category = st.sidebar.selectbox("Select Category", ["All"] + list(df['Category'].unique()))
region = st.sidebar.selectbox("Select Region", ["All"] + list(df['Region'].unique()))

# Filter data
filtered_df = df.copy()
if category != "All":
    filtered_df = filtered_df[filtered_df['Category'] == category]
if region != "All":
    filtered_df = filtered_df[filtered_df['Region'] == region]

# KPIs
st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Total Orders", filtered_df['Order ID'].nunique())
col3.metric("Avg Order Value", f"${(filtered_df['Sales'].sum() / filtered_df['Order ID'].nunique()):,.2f}")

# Historical Trend
st.subheader("Historical Sales Trend (Monthly)")
monthly_sales = filtered_df.groupby('Order Date')['Sales'].sum().resample('M').sum().reset_index()
fig_hist = px.line(monthly_sales, x='Order Date', y='Sales', title='Actual Sales')
st.plotly_chart(fig_hist, use_container_width=True)

# Forecasting with Prophet
st.subheader("3-Month Prophet Forecast")
if len(monthly_sales) > 12:
    with st.spinner("Generating Forecast..."):
        prophet_df = monthly_sales.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
        m = Prophet(yearly_seasonality=True)
        m.fit(prophet_df)
        future = m.make_future_dataframe(periods=3, freq='M')
        forecast = m.predict(future)
        
        fig_forecast = px.line(forecast, x='ds', y='yhat', title='Predicted Sales (Next 3 Months)')
        fig_forecast.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', line=dict(dash='dot', color='rgba(255,0,0,0.5)'), name='Lower Bound')
        fig_forecast.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', line=dict(dash='dot', color='rgba(0,255,0,0.5)'), name='Upper Bound')
        
        st.plotly_chart(fig_forecast, use_container_width=True)
else:
    st.warning("Not enough data to generate a reliable forecast. Try changing your filters.")