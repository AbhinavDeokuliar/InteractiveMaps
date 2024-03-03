import plotly.express as px

# Define map center coordinates
latitude = 30.7688
longitude = 76.5754

# Create map object
fig = px.scatter_mapbox(
    lat=[latitude],
    lon=[longitude],
    zoom=10,  # Adjust zoom level as needed
    mapbox_style="mapbox://styles/mapbox/streets-v11"  # Choose a map style
)

# Optional: Add a title and marker description


# Show the map
fig.show()
