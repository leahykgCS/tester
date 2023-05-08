import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

data = pd.read_csv("..\CS230PROJ\Pages\Meteorite_Landings.csv")
df = pd.DataFrame(data, columns=["year", 'mass (g)'])

st.header(":orange[Scatterplot of Meteorite Masses (in grams):]")
st.write("This is a scatterplot to show the mass relationship to the year landed.")
st.write("The mass (g) is in millions.")
st.write("There is no strong correlation with years and mass. There are some outliers.")

fig, ax = plt.subplots()
plt.scatter(df['year'], df['mass (g)'])
plt.ylabel('Mass (Grams)')
plt.xlabel('Year of Landing')
st.pyplot(fig)
