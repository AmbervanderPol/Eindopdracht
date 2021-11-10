## Importeren van packages

import pandas as pd
import matplotlib.pyplot as plt
import os
import requests
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from plotly.subplots import make_subplots
import folium
import json

import warnings
warnings.filterwarnings('ignore')

# Importen van de data

df = pd.read_csv('Opleiding_inkomen.csv')

# Kaart

coördinaten = [[53.217503, 6.566677], [53.200736, 5.795717], [52.878580, 6.646088], [52.441316, 6.398667], [52.435788, 5.453631],[52.056569, 6.028022], [52.091001, 5.117947], [52.377173, 4.902515], [51.916845, 4.482816], [51.495115, 3.842055], [51.592708, 5.129947], [51.187293, 5.999778]]
df['middelste_punt'] = coördinaten

m = folium.Map(location=[52.0893191, 5.1101691], zoom_start = 7, tiles="cartodbpositron")

Mbo = folium.FeatureGroup(name="Mbo", show = False).add_to(m)
Hbo = folium.FeatureGroup(name="Hbo", show = False).add_to(m)
Wo = folium.FeatureGroup(name="Wo", show = False).add_to(m)
Inwoners = folium.FeatureGroup(name="Inwoners", show = True).add_to(m)
Eenpersoonshuishouden = folium.FeatureGroup(name="Eenpersoonshuishouden", show = False).add_to(m)
Particulierehuishoudens = folium.FeatureGroup(name="Particulierehuishoudens", show = False).add_to(m)
Paarkinderen =folium.FeatureGroup(name="Paarkinderen", show = False).add_to(m)

x=0
for row in df.iterrows(): 
    row_values = row[1]
    Inwoners.add_child(folium.vector_layers.Circle(radius = row_values['pop_radius'], location = row_values['middelste_punt'], 
                                           fill = True, color='yellow').add_to(m))
    Mbo.add_child(folium.vector_layers.Circle(radius = row_values['Mbo_radius'], location = row_values['middelste_punt'], 
                                           fill = True, color='red').add_to(m))
    Hbo.add_child(folium.vector_layers.Circle(radius = row_values['Hbo_radius'], location = row_values['middelste_punt'], 
                                          fill = True, color='blue').add_to(m))
    Wo.add_child(folium.vector_layers.Circle(radius = row_values['Wo_radius'], location = row_values['middelste_punt'], 
                                          fill = True, color='purple').add_to(m))
    Eenpersoonshuishouden.add_child(folium.vector_layers.Circle(radius = row_values['eenpersoonshuishouden_radius'], location = row_values['middelste_punt'], 
                                          fill = True, color='dimgrey').add_to(m))
    Particulierehuishoudens.add_child(folium.vector_layers.Circle(radius = row_values['particulierehuishouden_radius'], location = row_values['middelste_punt'], 
                                          fill = True, color='lightcoral').add_to(m))
    Paarkinderen.add_child(folium.vector_layers.Circle(radius = row_values['paarmetkinderen_radius'], location = row_values['middelste_punt'], 
                                          fill = True, color='skyblue').add_to(m))
    
folium.LayerControl().add_to(m)
# folium.TileLayer('cartodbpositron', name='Onderwijs niveau').add_to(LayerControl)
display(m)

