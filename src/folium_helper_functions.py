import pandas as pd
import folium
import folium.plugins as fp
from folium.plugins import HeatMap
from folium.map import Layer
import numpy as np

# Instantiates map object with starting coordinates.
def folium_map_object(start_coords, tile_set='CartoDB positron',
                     zoom=11):
    
    return folium.Map(location=start_coords, tiles=tile_set,
                     zoom_start=zoom)


# Adds a folium layer to the specified map object.
def folium_add_layer(df, feature_map, base_map):
    marker_cluster = fp.MarkerCluster().add_to(feature_map)
    for index, row in df.iterrows():
        folium.Marker(location=(row['lat'], row['long']),
                        color=row['year_color'],
                        icon=folium.Icon(icon=row['response_icon']),
                        popup=str('Response Type: ' + row['PROGRAMAREA'] \
                                + '\nDate: ' + row['RESPONSEDATE'])
                        ).add_to(marker_cluster)
    base_map.add_child(feature_map)

def folium_heat_layer():       
    pass


# if __name__ == "__main__":
#     response_data = pd.read_csv('data/BFD_fire.csv')
#     locationlist = response_data[['lat','long']].values.tolist()
#     boulder_coords = (40.014984, -105.270546)
#     boulder_map = folium_map_object(boulder_coords)

#     folium_add_layer(map_object=boulder_map, lat_long_list=locationlist,
#                      name='Test', overlay=False)

#     boulder_map