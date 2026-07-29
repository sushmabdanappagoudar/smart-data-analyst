import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Data Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Data Analyst")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    rows, columns = df.shape

    st.write(f"Rows : {rows}")
    st.write(f"Columns : {columns}")

    st.subheader("Column Names")

    st.write(df.columns.tolist())

    st.subheader("Data Types")

    st.dataframe(df.dtypes)

    st.subheader("Missing Values")

    st.dataframe(df.isnull().sum())

    st.subheader("Statistical Summary")

    st.dataframe(df.describe())
