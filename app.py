import streamlit as st
import pandas as pd

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Smart Data Analyst",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# Title
# ------------------------------
st.title("📊 Smart Data Analyst")
st.write("Upload a CSV file to analyze your data.")


uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

# ------------------------------
# If a file is uploaded
# ------------------------------
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    # Preview
    st.header("📋 Dataset Preview")
    st.dataframe(df.head())

    # Shape
    st.header("📊 Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # Columns
    st.header("📌 Column Names")
    st.write(df.columns.tolist())

    # Data Types
    st.header("🧾 Data Types")
    st.dataframe(df.dtypes.astype(str))

    # Missing Values
    st.header("⚠ Missing Values")
    st.dataframe(df.isnull().sum())

<<<<<<< HEAD
    st.subheader("Statistical Summary")

    st.dataframe(df.describe())
=======
    # Statistics
    st.header("📈 Statistical Summary")
    st.dataframe(df.describe(include="all"))
>>>>>>> fb377df (Fix folder structure)
