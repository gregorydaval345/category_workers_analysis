import pandas as pd
import streamlit as st

df = pd.read_csv("demo.csv")

# Replace dashes ("-") with NaN and then fill all NaN values with 0
df["Unpaid Family Worker"] = df["Unpaid Family Worker"].replace("-", pd.NA)
df["Unpaid Family Worker"] = df["Unpaid Family Worker"].fillna(0)

# If required to cast the column back to an integer (after replacing NaNs)
df["Unpaid Family Worker"] = df["Unpaid Family Worker"].astype(int)

print(df)


# st.write(df)

# print(df.dropna(subset=["Year"]))
