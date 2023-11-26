import json
from math import sqrt
import random
import geopandas as gpd
from shapely.geometry import MultiLineString, Polygon, Point, LineString
import numpy as np
import progressbar

def magic_distance(pnt1, pnt2):
    points_df = gpd.GeoDataFrame({'geometry': [pnt1, pnt2]}, crs='epsg:4326')
    points_df = points_df.to_crs('epsg:5234')
    points_df2 = points_df.shift()
    return points_df.distance(points_df2).values[1]

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
        gdf.loc[relation['rel'], 'population'] = int(relation['reltags']['population'])

for index, row in gdf.iterrows():
    all_points = [point for line in row['geometry'] for point in line.coords]
    poly = Polygon(all_points)
    gdf.loc[index, 'geometry'] = Polygon(sort_polygon_vertices(poly)).convex_hull
    # print(index, gdf.loc[index, 'geometry'])
    gdf.loc[index, 'area'] = gdf.loc[index, 'geometry'].area * 1e3 * 5.378545839
    print(gdf.loc[index, 'area'], 'km²')

# Mark the geometry column as a geometry
gdf = gpd.GeoDataFrame(gdf, geometry='geometry')
# Dump the GeoDataFrame to a GeoJSON file
# gdf.to_file("datasets/districts-berlin-convex.geojson", driver="GeoJSON")
# Render the GeoDataFrame
gdf.plot().get_figure().savefig("districts-convex.png")

# Generate 50 random points in the convex hull of each district
ngdf = gpd.GeoDataFrame()
for index, row in gdf.iterrows():
    poly = row['geometry']

    for _ in range(50):
        while True:
            # Generate a random point within the bounds of the polygon
            x = random.uniform(poly.bounds[0], poly.bounds[2])
            y = random.uniform(poly.bounds[1], poly.bounds[3])
            point = Point(x, y)

            # Check if the point is within the polygon
            if poly.contains(point):
                ind = len(ngdf.index)
                ngdf.loc[ind, 'geometry'] = point
                ngdf.loc[ind, 'district'] = index
                ngdf.loc[ind, 'area'] = row['area']
                ngdf.loc[ind, 'lat'] = point.y
                ngdf.loc[ind, 'lon'] = point.x
                break

print("Points generated")

# Mark the geometry column as a geometry
ngdf = gpd.GeoDataFrame(ngdf, geometry='geometry')
# Set crs
ngdf.crs = gdf.crs

# Load other data frames and aggregate values for these points
hospitals = gpd.read_file("datasets/hospitals-berlin.geojson")
hospitals.crs = gdf.crs
ev_charging = gpd.read_file("datasets/ev_charging.geojson")
ev_charging.crs = gdf.crs
education = gpd.read_file("datasets/education.geojson")
education.crs = gdf.crs

# For every point, count the number of hospitals within 1km
bar = progressbar.ProgressBar(max_value=len(ngdf.index))
for index, row in ngdf.iterrows():
    # distance with magic_distance() is in meters
    distances = [magic_distance(row['geometry'], hospital) for hospital in hospitals['geometry']]
    hospitals_within = len([d for d in distances if d <= 3000])
    ngdf.loc[index, 'hospitals'] = hospitals_within

    # EV charging stations
    distances = [magic_distance(row['geometry'], station) for station in ev_charging['geometry']]
    stations_within = len([d for d in distances if d <= 7000])
    ngdf.loc[index, 'ev_charging'] = stations_within

    # Education
    distances = [magic_distance(row['geometry'], school) for school in education['geometry']]
    schools_within = len([d for d in distances if d <= 5000])
    ngdf.loc[index, 'education'] = schools_within

    # Population density
    population = gdf.loc[row['district'], 'population']
    density = population / row['area']

    ideal_density = 3034.62 # Taken from Helsinki
    # Density score is between 0 and 1, 1 being the best
    density_score = max(0, min(1, abs(ideal_density - density) / 300))
    ngdf.loc[index, 'population_density'] = density_score

    # Compute a final score
    score = 0
    score += density_score * 0.3
    score += max(0, min(1, hospitals_within / 2)) * 0.2
    score += max(0, min(1, stations_within / 6)) * 0.15
    score += max(0, min(1, schools_within / 6)) * 0.3
    score += random.uniform(0, 0.1)
    ngdf.loc[index, 'score'] = score

    bar.update(index)

# Dump the GeoDataFrame to a GeoJSON file
ngdf.to_file("datasets/noise-algo.geojson", driver="GeoJSON")