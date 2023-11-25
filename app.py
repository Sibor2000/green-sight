import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import pandas as pd

# Data setup
df = pd.DataFrame(
    {
        "City": ["San Francisco", "San Jose", "Palo Alto"],
        "Latitude": [37.77, 37.33, 37.44],
        "Longitude": [-122.43, -121.89, -122.14],
    }
)

map = KeplerGl(height=800)
map.add_data(
    data=df, name="GreenSight"
)

# App setup
st.set_page_config(layout="wide")

# Title and Subheader
st.write("# GreenSight Data Visualization")
st.write("This data was not captured with a drone. It was captured with a satellite.")

# Toolbar
st.button("Reset", type="primary")

# Map
keplergl_static(map, center_map=True)