import folium

# Define coordinates
a = 30.7688
b = 76.5754

# Create a base map
m = folium.Map(location=[a, b], zoom_start=13)

# Define custom marker icons
icon1 = folium.Icon(color='red', prefix='fa', icon='star')
icon2 = folium.Icon(color='blue', prefix='fa', icon='home')
icon3 = folium.Icon(color='green', prefix='fa', icon='flag')

# Create marker layers
marker_layer_1 = folium.FeatureGroup(name="Layer 1").add_to(m)
marker_layer_2 = folium.FeatureGroup(name="Layer 2").add_to(m)
marker_layer_3 = folium.FeatureGroup(name="Layer 3").add_to(m)

# Add markers to respective layers
folium.Marker([a + 0.01, b], icon=icon1).add_to(marker_layer_1)
folium.Marker([a - 0.01, b], icon=icon2).add_to(marker_layer_1)
folium.Marker([a, b + 0.01], icon=icon3).add_to(marker_layer_2)

# Layer control for switching visibility
folium.LayerControl(collapsed=False).add_to(m)

# Display the map
m.save("layer.html")
