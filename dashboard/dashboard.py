import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

data = pd.read_csv('dashboard/clean_data.csv')

data['Revenue_per_Employee'] = data['Revenue(USD millions)'] / data['Employees']

# Streamlit App
st.title("Company Data Analysis Dashboard")



t1, t2, t3 = st.tabs(['Overview', 'Visualizations', 'Insights'])

# Overview Section
with t1:
    st.header("Dataset Overview")
    st.write(data.head())
    st.write("Data Summary:")
    st.write(data.describe())

# Visualizations Section
with t2:
    c1, c2 = st.columns((5, 5))
    # 1. Industry Distribution
    with c1:
        st.subheader("Distribution of Companies by Industry")
        fig, ax = plt.subplots(figsize=(10, 5))
        industry_counts = data['Industry'].value_counts()
        sns.barplot(x=industry_counts.values, y=industry_counts.index, ax=ax)
        ax.set_title('Distribution of Companies by Industry')
        ax.set_xlabel('Number of Companies')
        st.pyplot(fig)

    # 2. Revenue vs Employees Scatter Plot

    with c2:
        st.subheader("Revenue vs Number of Employees by Industry")
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.scatterplot(data=data, x='Revenue(USD millions)', y='Employees', hue='Industry', ax=ax)
        ax.set_title('Revenue vs Number of Employees by Industry')
        st.pyplot(fig)

    c1, c2 = st.columns(2)
    # 3. Top 10 most Profitable Companies
    with c1:
        st.subheader('Top 10 most profitable companies')
        fig, ax = plt.subplots(figsize=(10, 8))
        top_profit_companies = data.nlargest(10, 'Profit(USD millions)')
        sns.barplot(data=top_profit_companies, x='Profit(USD millions)', y='Name')
        ax.set_title('Top 10 Companies by Profit')
        st.pyplot(fig)



    # 4. Revenue Distribution by Industry
    with c2:
        st.subheader("Revenue Distribution by Industry")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=data, x='Industry', y='Revenue(USD millions)', ax=ax)
        ax.set_title('Revenue Distribution by Industry')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    c1, c2 = st.columns((6, 4))
    # 5. Revenue per Employee Analysis
    with c1:
        st.subheader("Top 10 Companies by Revenue per Employee")
        fig, ax = plt.subplots(figsize=(10, 5))
        top_revenue_per_employee = data.nlargest(10, 'Revenue_per_Employee')
        sns.barplot(data=top_revenue_per_employee, x='Revenue_per_Employee', y='Name', ax=ax)
        ax.set_title('Top 10 Companies by Revenue per Employee')
        st.pyplot(fig)

    # 6. Industry Revenue Share
    with c2:
        st.subheader("Industry Revenue Share")
        fig, ax = plt.subplots()
        industry_revenue = data.groupby('Industry')['Revenue(USD millions)'].sum()
        ax.pie(industry_revenue, labels=industry_revenue.index, autopct='%1.1f%%')
        ax.set_title('Industry Share of Total Revenue')
        st.pyplot(fig)

    # 7. Profit Distribution by Industry
    st.subheader('Profit Distribution by Industry')
    plt.figure(figsize=(10, 3))
    sns.boxplot(data=data, x='Industry', y='Profit(USD millions)')
    plt.xticks(rotation=45)
    plt.title('Profit Distribution by Industry')
    st.pyplot(plt)
    

    
# Insights Section
with t3:
    st.header("Key Insights")
    st.write(f"1. Average Revenue per Employee (USD millions): {round(data['Revenue_per_Employee'].mean(), 2)}")
    st.write(f"2. Industry with most employees: {data.groupby('Industry')['Employees'].sum().idxmax()}")
    st.write(f"3. Average revenue (USD millions): {round(data['Revenue(USD millions)'].mean(), 2)}")
    st.write(f"4. Total number of employees: {format(data['Employees'].sum(), ',')}")
    st.write(f"5. Most common headquarters: {data['Headquarters'].mode()[0]}")
