import re
import requests

# Define regular expression patterns for longitude and latitude
longitude_pattern = r'-?\d+(\.\d+)?'
latitude_pattern = r'-?\d+(\.\d+)?'

# URL of the webpage containing longitude and latitude
url = 'https://www.arcgis.com/home/item.html?id=34ae3d3c9752434a8c03aca5deb550eb&sortOrder=desc&sortField=defaultFSOrder#data'

# Retrieve the HTML content of the webpage
response = requests.get(url)
html_content = response.text

# Find all longitude matches in the HTML content
longitude_matches = re.findall(longitude_pattern, html_content)
# Find all latitude matches in the HTML content
latitude_matches = re.findall(latitude_pattern, html_content)

# Convert matches to float values
longitudes = [float(match) for match in longitude_matches]
latitudes = [float(match) for match in latitude_matches]

# Print the extracted longitude and latitude values
for index, (longitude, latitude) in enumerate(zip(longitudes, latitudes), start=1):
    print(f"Coordinates {index}: Longitude: {longitude}, Latitude: {latitude}")
