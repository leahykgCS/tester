import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title(':orange[Map of Meteorites:]')
data = pd.read_csv("..\CS230PROJ\Pages\Meteorite_Landings.csv")
df = pd.DataFrame(data, columns=["name", "GeoLocation", "year", "reclat", "reclong"])
df = df.rename(columns={"name": "Meteorite Name","year": "Year", "reclat": "lat", "reclong": "long"})
df = df.dropna()

# GPT using list comp
decades = st.multiselect('What decade of meteor landings would you like to see on the map?',
                         [decade for decade in range(1810, 2030, 10)])
#the ranges and the step of 10

# where year in
dropdown_decade = df[df.Year.isin(decades)]
st.write("These are the decades you selected:")
st.write(decades)
st.write("This includes more details, based on the decade you selected:")
st.write(dropdown_decade)
map_points = dropdown_decade.values.tolist()

# returns more than one value and maps all of these values
def PlotPoints(df):
    # markers on map and put year it fell, used icon
    # initalize map
    m = folium.Map(location=[df.lat.mean(), df.long.mean()],
                     zoom_start=3, control_scale=True)
    for index, row in df.iterrows():
        iframe = folium.IFrame('Meteor Name: ' + str(row['Meteorite Name']) + '\n' + 'Year: ' + str(round(row['Year'])), width=200, height=100)
        popup = folium.Popup(iframe, max_width=None)
        marker_icon = folium.Icon(color='red')
        folium.Marker(location=[row['lat'], row['long']], popup=popup, icon=marker_icon, tooltip=row['Year']).add_to(m)
    st_data = st_folium(m, width=600)
PlotPoints(dropdown_decade)



