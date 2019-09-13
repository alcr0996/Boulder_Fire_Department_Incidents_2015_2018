import pandas as pd
import folium
import folium.plugins as fp
from folium.plugins import HeatMap
from folium.map import Layer

def folium_map(map_object, data, zoom_start=11, popup=False, icon=False, color=False):
    """
    map_object: The variable name of the map object that you have instantiated.
    data: List of lists, or array, of latitude and longitude data
    popup = String information that pops up when clicking on a map marker.
    """
    marker_cluster = fp.MarkerCluster().add_to(map_object)
    folium.Marker(locationlist).add_to(marker_cluster)
    name = str(map_object)
    map_object.save(name + '.html')

    return map_object

def folium_heatmap(map_object, data,
                 zoom_start=12,
                 min_opacity=0.2, radius=7, 
                 max_zoom=1, auto_play=True):
    """
    map_object: The variable name of the map object that you have instantiated.
    data: List of lists of lists of latitude and longitude data
    e.g. [[40.006661, -105.253452],[39.986564, -105.229860],[40.004591, -105.275369],...

    """
    HeatMap(data, min_opacity=min_opacity,
                   max_val=float(60),
                   radius=radius, 
                   max_zoom=max_zoom ).add_to(map_object)
    name = str(map_object)
    map_object.save(name + '.html')

    return map_object

def folium_heat_series(map_object, data,
                 zoom_start=11,
                 min_opacity=0.2, radius=4, blur=2, 
                 max_zoom=1):
    """
    map_object: The variable name of the map object that you have instantiated.
    data: List of lists of lists of latitude and longitude data
    e.g. timeseries_data_list = [[[row['lat'],row['long']] for index, 
             row in inc[inc['month'] == i].iterrows()] 
             for i in range(1,13)]
    """
    fp.HeatMapWithTime(heat_data_list, min_opacity=0.2, 
                        radius=7, auto_play=True,max_opacity=0.8).add_to(map_object)
    
    name = str(map_object)
    map_object.save(name + '.html')

    return map_object