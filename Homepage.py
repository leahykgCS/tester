import streamlit as st

""" Name: Your Name CS230: Section 001 
Data: pd.read_csv("..\CS230PROJ\Pages\Meteorite_Landings.csv")
Link to your web application on Streamlit Cloud (if posted)

Description: This program uses a meteorite fall dataset/dataframe. Using this data, I made several pages on streamlit. I filtered the data, and organized it alphabeticallly. Then I used interative streamlit features. I made several charts and a map."""

st.title(':orange[Kaitlyn Leahy CS230 Final Project: Meteorites Data:]')

st.header(':orange[The following images are of iron meteorites:]')
st.image('IRON1.jpg')
st.image('IRON2.jpg')

st.header(':orange[The following images are of stone meteorites:]')
st.image('STONE1.jpg')
st.image('STONE2.jpg')

st.header(':orange[The following images are of stony-iron meteorites:]')
st.image('STONEIRON1.jpg')
st.image('STONEIRON2.jpg')

