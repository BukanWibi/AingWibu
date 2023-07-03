import streamlit as s
from PIL import Image
image = Image.open('banner.png')
s.image(image, caption=' ')
s.title("Ini Aku!")
