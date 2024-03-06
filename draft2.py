import webbrowser
import folium
from folium.features import CustomIcon
import pandas as pd


def auto_open(path, f_map):
    """This function opens the file in browser automatically"""
    html_page = f'{path}'
    f_map.save(html_page)
    new = 2
    webbrowser.open(html_page, new=new)


"""Read the Excel file into a pandas DataFrame """
df = pd.read_excel('Book1.xlsx')

# Extract the latitude, longitude, and point of interest columns
latitudes = df['latitude'].tolist()
longitudes = df['longitude'].tolist()
points_of_interest = df['point_of_interest'].tolist()

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
coordinates = {point: (lat, lon) for point, lat, lon in zip(points_of_interest, latitudes, longitudes)}

"""Icon Urls & its implementation """

food_icon_url = "https://pics.freeicons.io/uploads/icons/png/10274305501591055829-512.png"
book_icon_url = "https://pics.freeicons.io/uploads/icons/png/7141564811595156044-512.png"

food_icon = CustomIcon(food_icon_url, icon_size=(25, 25))
book_icon = CustomIcon(book_icon_url, icon_size=(25, 25))

"""Map initialization"""

map_cu = folium.Map(location=[latitude, longitude], zoom_control=False, scroll_wheel_zoom=False, zoom_start=17,
                    marker_zoom=17, tiles=tile_layer4)

"""Adding tiles layer in map"""

food_courts = folium.FeatureGroup(name="Food_courts").add_to(map_cu)
blocks = folium.FeatureGroup(name="Blocks").add_to(map_cu)

# Define JavaScript code for button clicks
js_code = """
var base_layers = {};
base_layers["Stamen TonerLite"] = tile_layer1;


L.control.layers(base_layers, null, {collapsed:True}).addTo(map);
"""

folium.JavascriptLink(js_code).add_to(map_cu)

"""adding marker in thr map"""

for point, (lat, lon) in coordinates.items():
    folium.Marker(location=[lat, lon], popup=point).add_to(map_cu)

folium.LayerControl(collapsed=True).add_to(map_cu)

map_cu.save("draft2.html")
auto_open("draft2.html", map_cu)
