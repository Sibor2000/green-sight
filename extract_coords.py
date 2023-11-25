import json
import sys

if len(sys.argv) != 2:
    print("Usage: python3 extract_coords.py <filename>")
    exit(1)

filename = sys.argv[1]
# Load from JSON
with open(filename, 'r', encoding='utf-8') as file:
    geo = json.load(file)

for feature in geo['features']:
    coords = feature['geometry']['coordinates']
    feature['properties']['lat'] = coords[1]
    feature['properties']['lon'] = coords[0]
    # Remove 'lat' and 'lon' from the top-level of each feature
    if 'lat' in feature:
        del feature['lat']
    if 'lon' in feature:
        del feature['lon']


# Dump the GeoDataFrame to a GeoJSON file
new_filename = filename.split(".")[0] + "-coords.geojson"
with open(new_filename, "w", encoding='utf-8') as file:
    json.dump(geo, file, indent = 2)
