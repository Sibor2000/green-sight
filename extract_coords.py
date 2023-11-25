import json
import sys

if len(sys.argv) != 2:
    print("Usage: python3 extract_coords.py <filename>")
    exit(1)

filename = sys.argv[1]
# Load from JSON
geo = json.load(open(filename))

for feature in geo['features']:
    coords = feature['geometry']['coordinates']
    feature['lat'] = coords[1]
    feature['lon'] = coords[0]


# Dump the GeoDataFrame to a GeoJSON file
new_filename = filename.split(".")[0] + "-coords.geojson"
json.dump(geo, open(new_filename, "w"))
