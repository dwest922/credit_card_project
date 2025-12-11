import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Page config
st.set_page_config(page_title="Credit Card Churn Analysis", page_icon="💔", layout="wide")

# Title
st.title("Credit Card Churn Prediction Analysis")
st.write("Analysing factors that influence credit card churn")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('../datasets/bank-churners.csv')
    return df

df = load_data()

# Basic info
st.header("Dataset Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Customers", len(df))
with col2:
    st.metric("Features", len(df.columns))
with col3:
    st.metric("Churn Rate", f"{df['Attrition_Flag'].value_counts(normalize=True).get('Attrited Customer', 0):.1%}")
with col4:
    st.metric("Avg Credit Limit", f"${df['Credit_Limit'].mean():,.2f}")

# Show data
st.subheader("Sample Data")
st.dataframe(df.head())

# Basic statistics
with st.expander("Basic Statistics"):
    st.write(df.describe())

# Visualizations
st.header("Visualizations")

# Create seven tabs for charts and data
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Overview", "Demographic", "Customer Age", "Education", "Dependents", "Months on Book", "Data"])
with tab1:
    # Basic info
    st.header("Dataset Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", len(df))
    with col2:
        st.metric("Features", len(df.columns))
    with col3:
        churn_rate = df['Attrition_Flag'].value_counts(normalize=True).get('Attrited Customer', 0)
        st.metric("Churn Rate", f"{churn_rate:.1%}")
    with col4:
        st.metric("Avg Credit Limit", f"${df['Credit_Limit'].mean():,.2f}")
    
    # Basic statistics
    st.subheader("Statistics")
    st.write(df.describe())
with tab2:
    st.header("Demographic Distribution")
    # Bar charts comparing categorical variables with the target variable 'Attrition_Flag'
    categorical_vars = ['Gender', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category']
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))

    # adjust spacing (do NOT assign the return value)
    plt.subplots_adjust(hspace=0.4, wspace=0.3)

    fig.suptitle('Categorical Variables by Attrition_Flag', fontsize=16)
    # flatten axes array for easy indexing
    axs = axs.flatten()

    for i, var in enumerate(categorical_vars):    
        sns.countplot(data=df, x=var, hue='Attrition_Flag', ax=axs[i])
        axs[i].set_title(f'Count of {var} by Attrition_Flag')
        axs[i].tick_params(axis='x', rotation=45)
        axs[i].legend(title='Attrition_Flag', loc='upper right')

    # turn off any unused axes (we created 6, but have 5 variables)
    for j in range(i+1, len(axs)):
        axs[j].axis('off')

    # adjust layout to accommodate suptitle
    fig.tight_layout(rect=[0, 0, 1, 0.95])    
    st.pyplot(fig)
    plt.close(fig)
with tab3:
    # set two columns
    col1, col2 = st.columns(2)
    with col1:
        st.header("Customer Age Distribution")
        fig, ax = plt.subplots()
        sns.histplot(data=df, x='Customer_Age', hue='Attrition_Flag', multiple='stack', bins=30, ax=ax)
        ax.set_title('Customer Age Distribution by Attrition_Flag')
        ax.set_xlabel('Customer Age')
        ax.set_ylabel('Count')
        st.pyplot(fig)
        plt.close(fig)
    with col2:
        # Box plot for Customer Age
        st.header("Customer Age Box Plot")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x='Attrition_Flag', y='Customer_Age', ax=ax)
        ax.set_title('Customer Age by Attrition_Flag')
        ax.set_xlabel('Attrition_Flag')
        ax.set_ylabel('Customer Age')
        st.pyplot(fig)
        plt.close(fig)
with tab4:
    st.header("Education Level Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Education_Level', hue='Attrition_Flag', ax=ax)
    ax.set_title('Education Level by Attrition_Flag')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
    plt.close(fig)
with tab5:
    st.header("Dependents Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Dependent_count', hue='Attrition_Flag', ax=ax)
    ax.set_title('Dependents by Attrition_Flag')
    st.pyplot(fig)
    plt.close(fig)
with tab6:
    col1, col2 = st.columns(2)
    with col1:
        st.header("Months on Book Distribution")
        fig, ax = plt.subplots()
        sns.histplot(data=df, x='Months_on_book', hue='Attrition_Flag', multiple='stack', bins=30, ax=ax)
        ax.set_title('Months on Book by Attrition_Flag')
        ax.set_xlabel('Months on Book')
        ax.set_ylabel('Count')
        st.pyplot(fig)
        plt.close(fig)
    with col2:
        # Cohort Analysis: Months on Book vs. Attrition_Flag
        st.header("Months on Book vs. Attrition_Flag")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x='Attrition_Flag', y='Months_on_book', ax=ax)
        ax.set_title('Months on Book by Attrition_Flag')
        ax.set_xlabel('Attrition_Flag')
        ax.set_ylabel('Months on Book')
        st.pyplot(fig)
        plt.close(fig)
           
    col3, col4 = st.columns(2)
    with col3:
  # Cohort Analysis: Churn Rate by Months on Book
        st.header("Churn Rate by Months on Book")
        churn_by_months = df.groupby('Months_on_book')['Attrition_Flag'].value_counts(normalize=True).unstack().reset_index()
        fig, ax = plt.subplots()
        sns.lineplot(data=churn_by_months, x='Months_on_book', y='Attrited Customer', ax=ax)
        ax.set_title('Churn Rate by Months on Book')
        ax.set_xlabel('Months on Book')
        ax.set_ylabel('Churn Rate')
        st.pyplot(fig)
        plt.close(fig)
    with col4:
        # Cohort Analysis: Retention Rate Heatmap by Months on Book
        # Convert Months_on_book to time periods using buckets of 6 months
        st.header("Retention Rate Heatmap by Months on Book")
        retention_rate = df.groupby('Months_on_book')['Attrition_Flag'].value_counts(normalize=True).unstack().fillna(0)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(retention_rate, annot=True, fmt=".2f", cmap='YlGnBu', ax=ax)
        ax.set_title('Retention Rate Heatmap by Months on Book')
        ax.set_xlabel('Attrition_Flag')
        ax.set_ylabel('Months on Book')
        st.pyplot(fig)
        plt.close(fig)
    
    col5, col6 = st.columns(2)
    with col5:
        # Cohort Retention Heatmap using Months_on_book as cohorts/time periods
        st.header("Cohort Retention Heatmap")
        cohort_data = df.copy()
        cohort_data['Cohort'] = (cohort_data['Months_on_book'] // 6) * 6
        cohort_pivot = cohort_data.pivot_table(index='Cohort', columns='Attrition_Flag', values='CLIENTNUM', aggfunc='count').fillna(0)
        cohort_sizes = cohort_pivot.sum(axis=1)
        retention_matrix = cohort_pivot.divide(cohort_sizes, axis=0)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(retention_matrix, annot=True, fmt=".2f", cmap='YlGnBu', ax=ax)
        ax.set_title('Cohort Retention Heatmap')
        ax.set_xlabel('Attrition_Flag')
        ax.set_ylabel('Cohort (Months on Book)')
        st.pyplot(fig)
        plt.close(fig)
    with col6:
        # Cohort retention table and heatmap using `Months_on_book` as cohort/time axis
        st.header("Cohort Retention Analysis")
        
        # prepare a working copy
        df_cohort = df.copy()

        # create 6-month cohort buckets (0-5,6-11,...)
        df_cohort['cohort_group'] = (df_cohort['Months_on_book'] // 6) * 6
        # mark retained customers (adjust string to match your dataset values)
        retained_label = 'Existing Customer'
        df_cohort['is_retained'] = np.where(df_cohort['Attrition_Flag'] == retained_label, 1, 0)

        # compute retention rate per cohort by Months_on_book
        retention = (
            df_cohort
            .groupby(['cohort_group', 'Months_on_book'])['is_retained']
            .mean()
            .reset_index()
        )

        # pivot to table: rows = cohort_group, cols = Months_on_book
        retention_pivot = retention.pivot(index='cohort_group', columns='Months_on_book', values='is_retained')

        # sort columns for display
        retention_pivot = retention_pivot.reindex(sorted(retention_pivot.columns), axis=1)

        # display the retention table (rounded)
        st.dataframe(retention_pivot.round(3))

        # plot heatmap (mask NaNs)
        fig = plt.figure(figsize=(12, 6))
        sns.heatmap(retention_pivot, annot=True, fmt='.2f', cmap='Blues', cbar_kws={'label': 'Retention Rate'})
        plt.title('Cohort Retention Heatmap (by Months_on_book cohorts)')
        plt.xlabel('Months on Book (time)')
        plt.ylabel('Cohort Group (Months on Book start)')
        st.pyplot(fig)
        plt.close(fig)
with tab7:
    st.header("Raw Data")
    st.dataframe(df)
    # Download link for data
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='bank-churners.csv',
        mime='text/csv',
    )

            
