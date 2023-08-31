import streamlit as st
from PIL import Image

files = [
    "./static/1.jpg",
    "./static/2.jpg",
    "./static/3.jpg",
    "./static/4.jpg",
    "./static/5.jpg",
    "./static/6.jpg",
    "./static/7.jpg",
]

for f in files:
    image = Image.open(f)
    st.image(image)
