import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('Book1.xlsx')

# Extract the latitude, longitude, and point of interest columns
latitudes = df['latitude'].tolist()
longitudes = df['longitude'].tolist()
points_of_interest = df['point_of_interest'].tolist()

# Create a dictionary of tuples
coordinates = {point: (lat, lon) for point, lat, lon in zip(points_of_interest, latitudes, longitudes)}

a =list(coordinates.items())



# Print the dictionary of tuples
# print(coordinates)
key, value = a[1]
print(key)
print(value)