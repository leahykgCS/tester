import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# read data
data = pd.read_csv("..\CS230PROJ\Pages\Meteorite_Landings.csv")
df = pd.DataFrame(data, columns=["name", "year", "mass (g)", "GeoLocation"])

st.title(":orange[The Largest and Smallest Falls, Based on Mass:]")

if st.button("Find the greatest mass in grams"):
    max_mass = data.max()
    st.write("The greatest mass (g) of a meteorite fall in the dataset is:")
    st.write(max_mass)

if st.button('Find the lightest mass in grams'):
    min_mass = data.min()
    st.write('The lightest mass in grams of a meteorite fall in the dataset is:')
    st.write(min_mass)

mass_categories = pd.cut(data['mass (g)'], bins=[0, 100, 1000, 10000, 100000, 1000000, float('inf')], labels=['< 100g', '100g - 1kg', '1kg - 10kg', '10kg - 100kg', '100kg - 1t', '> 1t'])
mass_counts = mass_categories.value_counts()

# pie chart
fig, ax = plt.subplots()
ax.pie(mass_counts, autopct='%1.1f%%')
ax.set_title('Meteorite Landings by Mass')

legend_labels = ['{} ({:,} meteorites)'.format(label, count) for label, count in zip(mass_counts.index, mass_counts)]
ax.legend(legend_labels, bbox_to_anchor=(1.2, 1), loc='upper left')

st.pyplot(fig)
st.write("Displayed is a pie chart showing the percentages of how many meteorites are in each mass group.")