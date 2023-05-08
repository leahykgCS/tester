import streamlit.elements.image
import streamlit as st

st.title(":orange[What are meteorites?]")

# insert image
st.image('meteorimage1.jpg')
st.write("A meteorite is a fragment of spatial matter that falls to the surface of a planet. Most meteorites that fall to Earth come from the Asteroid Belt."
         "Meteorites survive their passage through the atmosphere to reach the surface of a planet or moon. ")

st.write("This website uses comprehensive data set from The Meteoritical Society contains information on all of the known meteorite landings. ")

st.header(":orange[Fun Facts: Did You Know?]")
st.write("*Scientists have estimated that around 48.5 tons/44,000 kg of meteoritic debris fall on our Earth every day.*")
firstFact = st.checkbox('Did you know this fact?')
st.write("*The Meteoritical Society established a method of naming meteorites by using the name of the place that it was found.*")
secondFact = st.checkbox('Did you know this fact before?')
st.write("*There are three types of meteorites: Iron, Stone, Stony-Iron.*")
thirdFact = st.checkbox('Did you know all three types?')
st.write("Image Source:")
st.caption("https://www.bing.com/images/search?view=detailV2&ccid=mQOJCDGG&id=6A4E31E76D7FC78664009D76C9E6527FADCB392C&thid=OIP.mQOJCDGGCCrhHJ1kxMnDRgHaHK&mediaurl=https%3a%2f%2fsites.wustl.edu%2fmeteoritesite%2ffiles%2f2020%2f02%2flm_nwa_02995_heritage_auctions_1334.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.990389083186082ae11c9d64c4c9c346%3frik%3dLDnLrX9S5sl2nQ%26pid%3dImgRaw%26r%3d0&exph=1291&expw=1334&q=meteorite+images&simid=608021718663048489&FORM=IRPRST&ck=8D08C27532C739E15DD91A6F94AEF65C&selectedIndex=8&ajaxhist=0&ajaxserp=0")
