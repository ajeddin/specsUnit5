import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
st.title("Grocery Store Admin Dashboard")

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

data = pd.read_csv("supermarket.csv")

st.header("Store Sales Distribution")
# st.write("This barplot shows the top 10 selling stores.")w
st.bar_chart(data.groupby(['store_area']).sum()[['store_id','store_sales']].sort_values(by='store_sales',ascending=False).head(10))
# grouped = data.groupby(['store_area'])['store_sales'].sum()
# dfSorted = grouped.sort_values(ascending=False)
# st.bar_chart(dfSorted.head(10))

grouped = data.groupby(['store_area']).sum()
st.header("Daily Customer Count by Store")
st.write("This bar chart shows the average daily customer count for top 10 stores.")
store_customer_count = grouped.sort_values(by='store_sales',ascending=False).head(10).groupby("store_id")["daily_customer_count"].mean()
st.bar_chart(store_customer_count)

store_area = st.selectbox("Select Store ID", data["store_area"].unique())
store_data = data[data["store_area"] == store_area]
store_sales = store_data["store_sales"].sum()
st.write("Store ID: ", store_area)
st.write("Store Sales: ", store_sales)