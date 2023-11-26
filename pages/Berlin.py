import streamlit as st
import streamlit.components.v1 as components
import zlib

st.title("GreenSight Data Visualization - Berlin")
st.write("This data was obtained through Overpass Turbo queries and layered using KeplerGL")
st.write("It includes various metrics related to the environment (see layers!)")

# Read data as binary
bin = open("embed/data.html.bin", "rb").read()
# Decompress data
data_html = zlib.decompress(bin).decode("utf-8")
components.html(data_html, height=800)

# # Read data
# data_html = open("embed/data.html").read()
# # Comress & dump data
# bin = zlib.compress(data_html.encode("utf-8"))
# open("embed/data.html.bin", "wb").write(bin)
# print("Compressed data")