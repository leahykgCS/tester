import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("..\CS230PROJ\Pages\Meteorite_Landings.csv")
df = pd.DataFrame(data, columns=['year'])

st.title(":orange[Frequency of Meteorite Falls by Decade:]")
fig,ax = plt.subplots()

plt.hist(df, bins=[1810,1820,1830,1840, 1850, 1860, 1870, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, ],color="pink", edgecolor = "lightseagreen")
plt.title("Historgram of Roller Coaster Speeds")
plt.xlabel("Decades")
plt.ylabel("Meteorite Falls")
plt.show()
st.pyplot(fig)
st.write("Above is a histogram showing the frequency of meteorite falls per decade")