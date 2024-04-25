import webbrowser

import folium
import pandas as pd
from folium.features import CustomIcon
from folium.plugins import MarkerCluster


def auto_open(path, f_map):
    """This function opens the file in browser automatically"""
    html_page = f'{path}'
    f_map.save(html_page)
    new = 2
    webbrowser.open(html_page, new=new)

df = pd.read_excel('blocks.xlsx')

# Extract the latitude, longitude, and point of interest columns
b_latitudes = df['latitude'].tolist()
b_longitudes = df['longitude'].tolist()
b_points_of_interest = df['point_of_interest'].tolist()

"""Read the Excel file into a pandas DataFrame """
df1 = pd.read_excel('food.xlsx')

# Extract the latitude, longitude, and point of interest columns
f_latitudes = df1['latitude'].tolist()
f_longitudes = df1['longitude'].tolist()
f_points_of_interest = df1['point_of_interest'].tolist()

"""Starting point of the map"""

latitude = 30.7688
longitude = 76.5754

"""Various tile layers used in the map"""

tile_layer1 = folium.TileLayer(tiles="Cartodb dark_matter")
tile_layer2 = folium.TileLayer(tiles="OpenStreetMap.DE",
                               attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
                                    'contributors')
tile_layer3 = folium.TileLayer(tiles="OpenStreetMap.France",
                               attr='&copy; OpenStreetMap France | &copy; <a '
                                    'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors')
tile_layer4 = folium.TileLayer(tiles="OpenStreetMap.BZH",
                               attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
                                    'contributors, Tiles courtesy of <a href="http://www.openstreetmap.bzh/" '
                                    'target="_blank">Breton OpenStreetMap Team</a>')

"""List of point of interests"""

# Create a dictionary of tuples
b_coordinates = {point: (lat, lon) for point, lat, lon in zip(b_points_of_interest, b_latitudes, b_longitudes)}
f_coordinates = {point: (lat, lon) for point, lat, lon in zip(f_points_of_interest, f_latitudes, f_longitudes)}

"""Icon Urls & its implementation """

food_icon_path = "fast-food_737967.png"
book_icon_path = "book_3145765.png"

food_icon = CustomIcon(food_icon_path, icon_size=(25, 25))
book_icon = CustomIcon(book_icon_path, icon_size=(25, 25))

"""Map initialization"""

map_cu = folium.Map(location=[latitude, longitude], zoom_start=17,
                    marker_zoom=17, tiles=tile_layer3)

"""Adding tiles layer in map"""

food_courts = folium.FeatureGroup(name="Food Courts").add_to(map_cu)
blocks = folium.FeatureGroup(name="Blocks").add_to(map_cu)

# Define JavaScript code for button clicks
js_code = """
var base_layers = {};
base_layers["Stamen TonerLite"] = tile_layer1;


L.control.layers(base_layers, null, {collapsed:True}).addTo(map);
"""

folium.JavascriptLink(js_code).add_to(map_cu)

# Create a marker cluster for food and blocks
food_courts_cluster = MarkerCluster(name="Food Courts").add_to(food_courts)
blocks_cluster = MarkerCluster(name="Blocks").add_to(blocks)

# Add markers to the marker clusters
for point, (lat, lon) in b_coordinates.items():
    folium.Marker(location=[lat, lon],  tooltip=point).add_to(blocks_cluster)

for point, (lat, lon) in f_coordinates.items():
    folium.Marker(location=[lat, lon], tooltip=point).add_to(food_courts_cluster)

folium.LayerControl(collapsed=True).add_to(map_cu)

map_cu.save("draft2.html")
auto_open("draft2.html", map_cu)