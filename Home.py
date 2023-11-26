import json
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd
import streamlit.components.v1 as components

# Data setup
# noise = gpd.read_file("datasets/noise-algo.geojson")
# transport = gpd.read_file("datasets/transport-berlin.geojson")
# print("Loading districts")
# districts = gpd.read_file("datasets/districts-berlin.geojson")
# print("Loading bikes")
# bikes = gpd.read_file("datasets/bikes-coords.geojson")
# print("Loading education")
# education = gpd.read_file("datasets/education-coords.geojson")
# print("Loading EV charging")
# ev_charging = gpd.read_file("datasets/ev_charging-coords.geojson")
# print("Loading fast food")
# fast_food = gpd.read_file("datasets/fast_food-coords.geojson")
# print("Loading hospitals")
# hospitals = gpd.read_file("datasets/hospitals-coords.geojson")
# print("Loading stations")
# stations = gpd.read_file("datasets/stations-coords.geojson")
# print("Loading waste management")
# waste_management = gpd.read_file("datasets/waste_management-coords.geojson")


# map = KeplerGl(height=800)

# Add noise data, our custom well-being metric (took 2 hours to compute)
# map.add_data(data=noise, name="Noise")
# map.add_data(data=districts, name="Districts")
# map.add_data(data=bikes, name="Bikes")
# map.add_data(data=education, name="Education")
# map.add_data(data=ev_charging, name="EV Charging")
# map.add_data(data=fast_food, name="Fast Food")
# map.add_data(data=hospitals, name="Hospitals")
# map.add_data(data=stations, name="Stations")
# map.add_data(data=waste_management, name="Waste Management")

# Layer styles
# map.config = json.loads(open("config.json").read())

# App setup
st.set_page_config(layout="wide")

# Title and Subheader
st.write("# GreenSight")
st.write("GreenSight is a pioneering GIS company at the intersection of technology and sustainability. Specializing in Geographic Information Systems, we leverage advanced data analytics to showcase quality of life, sustainability, and green development on dynamic maps. Join us on a journey of innovation, where maps become powerful tools for a greener and more sustainable future!")

st.write("## Data Visualization")
st.write("To explore our data, select a page from the sidebar on the left.")

# Toolbar
# st.button("Reset", type="primary")
# if st.button("Save HTML", type="primary"):
#     map.save_to_html(file_name="map.html")
# if st.button("Save Kepler schema", type="primary"):
#     schema = map.get_state(drop_defaults=True)
#     with open("schema.json", "w") as f:
#         f.write(json.dumps(schema))

# Map
# # keplergl_static(map, center_map=True)
# components.html(noise_html, height=800)