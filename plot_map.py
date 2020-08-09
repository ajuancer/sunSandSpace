import requests
import matplotlib.pyplot as plt
import numpy as np
import json



data = {'elements': [
    {
        'type': 'node',
        'lon': -5.659651,
        'lat': 43.542694
    },
    {
        'type': 'node',
        'lon': -5.658059,
        'lat': 43.542072
    },
    {
        'type': 'node',
        'lon': -5.657011,
        'lat': 43.541776
    },
    {
        'type': 'node',
        'lon': -5.655278,
        'lat': 43.541364
    }
]}

# Collect coords into list
coords = []
for element in data['elements']:
  if element['type'] == 'node':
    lon = element['lon']
    lat = element['lat']
    coords.append((lon, lat))
  elif 'center' in element:
    lon = element['center']['lon']
    lat = element['center']['lat']
    coords.append((lon, lat))# Convert coordinates into numpy array
X = np.array(coords)
plt.plot(X[:, 0], X[:, 1], 'o')
plt.title('Biergarten in Germany')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')
plt.show()