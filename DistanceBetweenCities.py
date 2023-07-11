import math

RADIUS = 6371.01
radians = math.radians

arccos = math.acos
sin = math.sin
cos = math.cos

lat1 = 50.45
lon1 = 30.523
lat2 = 51.5072
lon2 = -0.1275

lon1 = radians(lon1)
lon2 = radians(lon2)
lat1 = radians(lat1)
lat2 = radians(lat2)

distance = 6371.01 * arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2)  * cos(lon1 - lon2))

print(distance)