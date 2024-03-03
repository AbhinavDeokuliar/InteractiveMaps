import folium
from folium.plugins import GroupedLayerControl
from folium.features import CustomIcon
import webbrowser
from jinja2 import Template


def auto_open(path, f_map):
    html_page = f'{path}'
    f_map.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)

popup_template = Template("""

""")


latitude = 30.7688
longitude = 76.5754

tile_layer1 = folium.TileLayer(tiles="Cartodb dark_matter")
tile_layer4 = folium.TileLayer(tiles="OpenStreetMap.BZH",
                               attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
                                    'contributors, Tiles courtesy of <a href="http://www.openstreetmap.bzh/" '
                                    'target="_blank">Breton OpenStreetMap Team</a>')
tile_layer3 = folium.TileLayer(tiles="OpenStreetMap.France",
                               attr='&copy; OpenStreetMap France | &copy; <a '
                                    'href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors')
tile_layer2 = folium.TileLayer(tiles="OpenStreetMap.DE",
                               attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
                                    'contributors')

block = [[30.76714843670572, 76.57472148622176], [30.766843747902985, 76.57621805141478]]  # [ c3, c1]
food = [[30.768744947318915, 76.5776381704867], [30.768756919536795, 76.5777927058071]]  # [creative food, crunchy bite]
food_icon_url = "https://pics.freeicons.io/uploads/icons/png/10274305501591055829-512.png"
book_icon_url = "https://pics.freeicons.io/uploads/icons/png/7141564811595156044-512.png"

food_icon = CustomIcon(food_icon_url, icon_size=(25, 25))
book_icon = CustomIcon(book_icon_url, icon_size=(25, 25))

map_cu = folium.Map(location=[latitude, longitude], zoom_control=True, zoom_start=17, max_zoom=25, min_zoom=16,
                    marker_zoom=17, tiles=tile_layer2)

tile_layer4.add_to(map_cu)
tile_layer3.add_to(map_cu)

food_courts = folium.FeatureGroup(name="Food_courts").add_to(map_cu)
blocks = folium.FeatureGroup(name="Blocks").add_to(map_cu)

# Define JavaScript code for button clicks
js_code = """
var base_layers = {};
base_layers["Stamen TonerLite"] = tile_layer1;


L.control.layers(base_layers, null, {collapsed:True}).addTo(map);
"""

folium.JavascriptLink(js_code).add_to(map_cu)

folium.Marker([30.76714843670572, 76.57472148622176], popup="C1", icon=book_icon).add_to(blocks)
folium.Marker([30.768744947318915, 76.5776381704867], popup="Creative Foods", icon=food_icon).add_to(food_courts)

folium.LayerControl(collapsed=True).add_to(map_cu)
map_cu.save("draft1.html")
auto_open("draft1.html", map_cu)
#just a add on
#another add on