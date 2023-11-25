import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import pandas as pd
import geopandas as gpd

# Data setup
districts = gpd.read_file("datasets/districts-berlin.geojson")

map = KeplerGl(height=800)
map.add_data(
    data=districts, name="Districts"
)

# Layer styles
map.config = {
    "version": "v1",
    "config": {
        "mapState": {
            "latitude": 52.520008,
            "longitude": 13.404954,
            "zoom": 10,
        },
        "visState": {
            "layers": [
                {
                    "id": "y2q3v8",
                    "type": "geojson",
                    "config": {
                        "dataId": "Districts",
                        "label": "Districts",
                        "color": [18, 147, 154],
                        "columns": {"geojson": "geometry"},
                        "isVisible": True,
                        "visConfig": {
                            "opacity": 0.8,
                            "strokeOpacity": 0.8,
                            "thickness": 0.5,
                            "strokeColor": [10, 10, 10],
                            "colorRange": {
                                "name": "ColorBrewer YlGn-6",
                                "type": "sequential",
                                "category": "ColorBrewer",
                                "colors": [
                                    "#ffffcc",
                                    "#d9f0a3",
                                    "#addd8e",
                                    "#78c679",
                                    "#31a354",
                                    "#006837",
                                ],
                            },
                            "strokeColorRange": {
                                "name": "ColorBrewer YlGn-6",
                                "type": "sequential",
                                "category": "ColorBrewer",
                                "colors": [
                                    "#ffffcc",
                                    "#d9f0a3",
                                    "#addd8e",
                                    "#78c679",
                                    "#31a354",
                                    "#006837",
                                ],
                            },
                            "radius": 10,
                            "sizeRange": [0, 10],
                            "radiusRange": [0, 50],
                            "heightRange": [0, 500],
                            "elevationScale": 5,
                            "stroked": True,
                            "filled": True,
                            "enable3d": False,
                            "wireframe": False,
                        },
                        "hidden": False,
                        "textLabel": [{"field": None, "color": [255, 255, 255]}],
                    },
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "Districts": ["name", "bezirk", "area", "population"]
                    },
                    "enabled": True,
                },
                "brush": {"size": 0.5, "enabled": False},
                "geocoder": {"enabled": False},
                "coordinate": {"enabled": False},
            },
            "layerBlending": "normal",
            "splitMaps": [],
        },
    },
}

# App setup
st.set_page_config(layout="wide")

# Title and Subheader
st.write("# GreenSight Data Visualization")
st.write("This data was not captured with a drone. It was captured with a satellite.")

# Toolbar
st.button("Reset", type="primary")

# Map
keplergl_static(map, center_map=True)