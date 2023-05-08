import streamlit as st
import pandas as pd

data = pd.read_csv("..\CS230PROJ\Pages\Meteorite_Landings.csv")
st.title(":orange[Filtered Data Based on Minimum Mass:]")
st.write("Due to this dataset having very large masses, I set the minimum mass to 1,000 g")

def filter_data(data, min_mass):
    # filter data based on min mass
    filtered_data = data[data["mass (g)"] >= min_mass]
    return filtered_data[["name", "year", "mass (g)"]]

# filter
min_mass = 1000
filtered_data = filter_data(data, min_mass)

total_mass = round(data["mass (g)"].sum(), 2)

st.write("Filtered Data:")
st.write(filtered_data)
st.write("Total Mass of All Meteorites:", total_mass)

