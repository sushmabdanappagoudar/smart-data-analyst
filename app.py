import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Data Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Data Analyst")
st.write("Upload a CSV file to analyze your data.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    st.header("📋 Dataset Preview")
    st.dataframe(df.head())

    st.header("📊 Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing Values", int(df.isnull().sum().sum()))

    c4, c5 = st.columns(2)

    c4.metric("Duplicate Rows", int(df.duplicated().sum()))

    memory = df.memory_usage(deep=True).sum() / 1024
    c5.metric("Memory (KB)", f"{memory:.2f}")

    st.header("📌 Column Names")
    st.write(df.columns.tolist())

    st.header("🧾 Data Types")
    st.dataframe(df.dtypes.astype(str))

    st.header("⚠ Missing Values")
    st.dataframe(df.isnull().sum().rename("Missing Values"))

    st.header("📈 Statistical Summary")
    st.dataframe(df.describe(include="all"))
    