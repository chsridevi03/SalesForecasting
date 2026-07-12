# SalesForecasting



📈 End-to-End Sales Forecasting & Demand Intelligence System

Overview

This project was developed as part of my Data Science Internship (Week 3 & Week 4). It demonstrates an end-to-end sales forecasting pipeline using real-world retail sales data. The project predicts future sales, detects anomalies, segments product demand, and provides an interactive business dashboard for decision-making.

---

Project Objectives

- Analyze historical retail sales data
- Perform time series decomposition and stationarity testing
- Build and compare three forecasting models:
  - SARIMA
  - Prophet
  - XGBoost
- Detect unusual sales patterns using anomaly detection
- Segment products using K-Means clustering
- Develop an interactive Streamlit dashboard
- Present business insights through an executive report

---

Dataset

Primary Dataset

- Superstore Sales Dataset (Kaggle)

Secondary Dataset

- Video Game Sales Dataset (Kaggle)

---

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Statsmodels
- Prophet
- XGBoost
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

Project Structure

SalesForecasting_CHSridevi/
│
├── analysis.ipynb
├── app.py
├── requirements.txt
├── train.csv
├── summary.pdf
├── charts/
│   ├── monthly_sales.png
│   ├── decomposition.png
│   ├── forecast.png
│   ├── anomalies.png
│   └── clusters.png
│
└── README.md

---

Features

Exploratory Data Analysis

- Data cleaning
- Missing value analysis
- Feature engineering
- Sales trend visualization

Time Series Analysis

- Monthly sales trend
- Seasonal decomposition
- ADF stationarity test
- Differencing

Forecasting Models

- SARIMA
- Prophet
- XGBoost

Model Evaluation

- MAE
- RMSE
- MAPE

Anomaly Detection

- Isolation Forest
- Z-Score Method

Product Demand Segmentation

- K-Means Clustering
- PCA Visualization

Interactive Dashboard

- Sales Overview
- Forecast Explorer
- Anomaly Report
- Product Demand Segments

---

Installation

Clone the repository:

git clone https://github.com/yourusername/SalesForecasting_CHSridevi.git

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

---

Results

- Compared three forecasting models
- Selected the best-performing model using MAE, RMSE, and MAPE
- Forecasted future product demand
- Detected abnormal sales spikes and drops
- Segmented products into demand clusters
- Built an interactive dashboard for business users

---

Future Improvements

- Deep learning models (LSTM)
- Real-time forecasting
- Inventory optimization
- Cloud deployment
- Automated model retraining

---

Author

CH Sridevi

B.Tech – Artificial Intelligence & Data Science

GitHub: https://github.com/chsridevi03

