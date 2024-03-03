# Import necessary packages
import webbrowser
import folium
import branca


def auto_open(path, f_map):
    html_page = f'{path}'
    f_map.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)


# Create a map using Stamen Terrain, centered on Boulder, CO
m = folium.Map(location=[30.7688, 76.5754],
               tile='Stamen Terrain',
               control_scale=True,
               zoom_start=17)

# Picture embedding in iframe using HTML to place it in the marker
hi = """html = '''<h3> This is a big popup</h3><br>
<img src="D:\study-rewards.webp ;base64,{}" width="500" height="600"><br>
<p>foo bar</p>'''"""
hell = branca.element.IFrame(html=hi, width=500, height=300)
popup = folium.Popup(hell, max_width=500)
folium.Marker([30.767058466248415, 76.57470928662508], popup=popup).add_to(m)
# Add marker to block C1
# folium.Marker([30.767058466248415, 76.57470928662508], popup="C1", ).add_to(m)
# m.save("footprint.html")

# Display m
auto_open("footprint.html", m)
