import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('Book1.xlsx')

# Extract the latitude and longitude columns
latitudes = df['latitude'].tolist()
longitudes = df['longitude'].tolist()

# Create a list of tuples
coordinates = list(zip(latitudes, longitudes))

# Print the list of tuples
print(coordinates)