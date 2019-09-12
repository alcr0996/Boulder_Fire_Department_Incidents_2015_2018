import pandas as pd
import folium
import folium.plugins as fp
from folium.plugins import HeatMap
from folium.map import Layer

df = pd.read_csv('../data/BFD_fire.csv')

# Map Prep
# Create new df with just lat/long.
incident_latlong = response_data[['lat', 'long']].copy()

# Cast the lat/long to a list
locationlist = incident_latlong.values.tolist()
# locationlist[7] = [39.98363365628458, -105.25191229875358]

# Get Boulder, CO coords, read in response_data.csv, rename
boulder_coords = (40.014984, -105.270546)

# create empty map zoomed in on Boulder, CO

map = folium.Map(location=boulder_coords, zoom_start=12)

# Test with SMALL subset of data
for point in range(0, 50):
    folium.Marker(locationlist[point], popup = response_data['INCIDENTTYPE'][point]).add_to(map)
# map

# Attempt to clean up the map. Instantiate a new map first.
map2 = folium.Map(location=boulder_coords, zoom_start=12)

marker_cluster = fp.MarkerCluster().add_to(map2)

# Remember to try a small subset of data.
for point in range(0, 50):
    folium.Marker(locationlist[point], popup = response_data['INCIDENTTYPE'][point]).add_to(marker_cluster)
# map2

# Attempt 3: Larger subset of data. Testing icons.

map3 = folium.Map(location=boulder_coords, tiles='CartoDB positron', zoom_start=11)

marker_cluster = fp.MarkerCluster().add_to(map3)

# Try a larger subset of data with less zoom:
for point in range(0, 500):
    folium.Marker(locationlist[point], popup = response_data['INCIDENTTYPE'][point], icon = folium.Icon(icon = 'fire')).add_to(marker_cluster)

# map3

# Prepping for map 4: These columns have already been created

# def program_area_icons(df):
#     if df['PROGRAMAREA'] == 'Fire':
#         return 'fire'
#     elif df['PROGRAMAREA'] == 'Rescue':
#         return 'flag'
#     elif df['PROGRAMAREA'] == 'EMS':
#         return 'plus-sign'
#     elif df['PROGRAMAREA'] == 'Hazmat':
#         return 'warning-sign'
#     elif df['PROGRAMAREA'] == 'Mutual Aid':
#         return 'user'
#     else:
#         return 'asterisk'
# response_data["response_icon"] = response_data.apply(program_area_icons, axis=1)

# def incident_year(df):
#     if df['RESPONSEYEAR'] == 2015:
#         return 'red'
#     elif df['RESPONSEYEAR'] == 2016:
#         return 'orange'
#     elif df['RESPONSEYEAR'] == 2017:
#         return 'green'
#     elif df['RESPONSEYEAR'] == 2018:
#         return 'darkblue'
#     elif df['RESPONSEYEAR'] == 2019:
#         return 'darkpurple'
#     else:
#         return 'gray'
# response_data["year_color"] = response_data.apply(incident_year, axis=1)

# Split response_data into separate years.

boulder_2015 = response_data[response_data['RESPONSEYEAR'] == 2015]
incident_latlong_15 = boulder_2015[['lat', 'long']].copy()
locationlist_15 = incident_latlong.values.tolist()

boulder_2016 = response_data[response_data['RESPONSEYEAR'] == 2016]
incident_latlong_16 = boulder_2016[['lat', 'long']].copy()
locationlist_16 = incident_latlong.values.tolist()

boulder_2017 = response_data[response_data['RESPONSEYEAR'] == 2017]
incident_latlong_17 = boulder_2017[['lat', 'long']].copy()
locationlist_17 = incident_latlong.values.tolist()

boulder_2018 = response_data[response_data['RESPONSEYEAR'] == 2018]
incident_latlong_18 = boulder_2018[['lat', 'long']].copy()
locationlist_18 = incident_latlong.values.tolist()

boulder_2019 = response_data[response_data['RESPONSEYEAR'] == 2019]
incident_latlong_19 = boulder_2019[['lat', 'long']].copy()
locationlist_19 = incident_latlong.values.tolist()

map4 = folium.Map(location=boulder_coords, tiles='CartoDB positron', zoom_start=11)

marker_cluster = fp.MarkerCluster().add_to(map4)

# Try adding markers specific to year and responseprogram:
for point in range(0, 750):
    folium.Marker(locationlist[point], popup = response_data['INCIDENTTYPE'][point], 
    icon = folium.Icon(icon = response_data['response_icon'][point], 
    color = response_data['year_color'][point])).add_to(marker_cluster)
map4.save('BFD_hmap_response_year_limited.html')
# map4

# Testing out a heat map
map5 = folium.Map(location=boulder_coords, tiles='CartoDB positron', zoom_start=11)

# locationlist_short = locationlist[:]
HeatMap(locationlist, min_opacity=0.2,
                   max_val=float(60),
                   radius=4, blur=2, 
                   max_zoom=1 ).add_to(map5)

map5.save('BFD_heatmap.html')
# map5

# Prepping a heat map with TimeSeries
# List of list of lists
heat_data_list = [[[row['lat'],row['long']] for index, 
                row in inc[inc['month'] == i].iterrows()] 
                for i in range(1,13)]

map6 = folium.Map(location=boulder_coords, tiles='CartoDB positron', zoom_start=13)
hm = fp.HeatMapWithTime(heat_data_list, min_opacity=0.2, 
                        radius=3.75, auto_play=True,max_opacity=0.8)
hm.add_to(map6)

hm.save('hmap_timeseries.html')

def folium_map










def folium_heatmap(map_object, location, data,
                 tiles='CartoDB positron', zoom_start=11,
                 min_opacity=0.2, radius=4, blur=2, 
                 max_zoom=1):
"""
map_object: name of the map you want to instantiate
location: coordinates you want the instantiated object to start on
data: list of lists of latitude and longitude data
"""
    map_object = folium.Map(location=location,
                             tiles=tiles, zoom_start=zoom_start)
    HeatMap(locationlist, min_opacity=min_opacity,
                   max_val=float(60),
                   radius=radius, blur=blur, 
                   max_zoom=max_zoom ).add_to(map_object)
    name = str(map_object)
    map_object.save(name + '.html')