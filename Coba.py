import streamlit as s
from PIL import Image
image = Image.open('banner.png')
s.image(image, caption=' ')
s.title("Pengambil Warna")
color = s.color_picker('Pilih Warna Kesukaanmu', '#00f900')
s.write('Kode Warna nya: ', color)
