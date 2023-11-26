import json
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd

gpd.options.io_engine = "pyogrio"

# Data setup
# noise = gpd.read_file("datasets/noise-algo.geojson")
# transport = gpd.read_file("datasets/transport-berlin.geojson")
print("Loading districts")
districts = gpd.read_file("datasets/districts-berlin.geojson")
# print("Loading bikes")
# bikes = gpd.read_file("datasets/bikes-coords.geojson")
print("Loading education")
education = gpd.read_file("datasets/education-coords.geojson")
print("Loading EV charging")
ev_charging = gpd.read_file("datasets/ev_charging-coords.geojson")
print("Loading fast food")
fast_food = gpd.read_file("datasets/fast_food-coords.geojson")
print("Loading hospitals")
hospitals = gpd.read_file("datasets/hospitals-coords.geojson")
print("Loading stations")
stations = gpd.read_file("datasets/stations-coords.geojson")
print("Loading waste management")
waste_management = gpd.read_file("datasets/waste_management-coords.geojson")


map = KeplerGl(height=800)

# Add noise data, our custom well-being metric (took 2 hours to compute)
# map.add_data(data=noise, name="Noise")
map.add_data(data=districts, name="Districts")
# map.add_data(data=bikes, name="Bikes")
# map.add_data(data=education, name="Education")
# map.add_data(data=ev_charging, name="EV Charging")
# map.add_data(data=fast_food, name="Fast Food")
map.add_data(data=hospitals, name="Hospitals")
# map.add_data(data=stations, name="Stations")
# map.add_data(data=waste_management, name="Waste Management")

# Layer styles
# map.config = json.loads(open("config.json").read())

# App setup
st.set_page_config(layout="wide")

# Title and Subheader
st.write("# GreenSight Data Visualization")
st.write("This data was not captured with a drone. It was captured with a satellite.")

# Toolbar
st.button("Reset", type="primary")

# Map
keplergl_static(map, center_map=True)