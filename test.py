import json
import geopandas as gpd
from shapely.geometry import MultiLineString, Polygon
import numpy as np

def sort_polygon_vertices(polygon):
    """
    Sort the vertices of a polygon in counter-clockwise order.
    """
    centroid = polygon.centroid
    return sorted(polygon.exterior.coords[:-1], key=lambda coord: -np.arctan2(coord[0] - centroid.x, coord[1] - centroid.y))

districts = gpd.read_file("datasets/districts-berlin.geojson")

districts.plot().get_figure().savefig("districts.png")

# Create a new GeoDataFrame
gdf = gpd.GeoDataFrame()

# For every feature of the districts GeoDataFrame, look at its first relation
# if a relation with such an id exists in gdf, add the geometry to the existing row
# if not, create a new row
for index, row in districts.iterrows():
    for relation in json.loads(row['@relations']):
        if relation['rel'] in gdf.index:
            gdf.loc[relation['rel'], 'geometry'].append(row['geometry'])
        else:
            gdf.loc[relation['rel'], 'geometry'] = [row['geometry']]
            print(relation['reltags']['name'])

for index, row in gdf.iterrows():
    all_points = [point for line in row['geometry'] for point in line.coords]
    poly = Polygon(all_points)
    gdf.loc[index, 'geometry'] = Polygon(Polygon(sort_polygon_vertices(poly)).exterior.coords)
    # print(index, gdf.loc[index, 'geometry'])
    gdf.loc[index, 'area'] = gdf.loc[index, 'geometry'].area
    print(gdf.loc[index, 'area'] * 1e3, 'km²')

# Mark the geometry column as a geometry
gdf = gpd.GeoDataFrame(gdf, geometry='geometry')
# Dump the GeoDataFrame to a GeoJSON file
gdf.to_file("datasets/districts-berlin-convex.geojson", driver="GeoJSON")
# Render the GeoDataFrame
gdf.plot().get_figure().savefig("districts-convex.png")