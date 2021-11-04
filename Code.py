import pandas as pd
import requests
import json
import cbsodata
import geopandas as gpd
from shapely.geometry.multipolygon import MultiPolygon
import shapely.wkt
import folium
import numpy as np
import plotly.graph_objects as go
import streamlit as st

inkomen = pd.read_csv('Inkomen_per_regio.csv', delimiter = ';')
aantal_mensen = pd.read_csv('Aantal_mensen_per_regio.csv', delimiter=';')
opleiding = pd.read_csv('Opleiding_per_regio.csv', delimiter =';')
