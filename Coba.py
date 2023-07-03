import streamlit as s
s.title("Ini Aku!")
from PIL import Image
image = Image.open('banner.png')
st.image(image, caption='Sunrise by the mountains')
