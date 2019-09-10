import pandas as pd
import folium
import folium.plugins as fp
from folium.plugins import HeatMap

# read in csv and import helper functions
import folium_helper_functions as fhf
df = pd.read_csv('data/BFD_fire.csv')

# Instantiate map object
boulder_coords = (40.014984, -105.270546)
boulder_map = fhf.folium_map_object(boulder_coords)

# Create map layers
incidents_2015 = folium.FeatureGroup(name='Incidents in 2015')
fhf.folium_add_layer(df, incidents_2015, boulder_map)