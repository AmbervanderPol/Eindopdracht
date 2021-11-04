## Importeren van packages

import streamlit as st
import pandas as pd
import os
import requests
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.filterwarnings('ignore')

## Importeren van de data

inkomen = pd.read_csv('Inkomen_per_regio.csv', delimiter = ';')

aantal_mensen = pd.read_csv('Aantal_mensen_per_regio.csv', delimiter=';')

opleiding = pd.read_csv('Opleiding_per_regio.csv', delimiter =';')

## File opschonen

### Inkomen per regio

#MAXIMAAL 1 KEER RUNNEN! Anders worden er kolommen verwijderd die niet verwijderd moeten worden.
# rijen weg halen
inkomen = inkomen.drop(index=0)
inkomen = inkomen.drop(index=14)
inkomen.reset_index(inplace=True)
inkomen.head()

# komma's vervangen voor punten
inkomen['Inkomen en vermogen|Particuliere huishoudens excl. studenten'] = inkomen['Inkomen en vermogen|Particuliere huishoudens excl. studenten'].str.replace(',', '.')
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten'].str.replace(',', '.')
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden'].str.replace(',', '.')
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin'].str.replace(',', '.')
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind'].str.replace(',', '.')
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)'].str.replace(',', '.')
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer'].str.replace(',', '.')

# type van de kolommen omzetten naar floats
inkomen['Inkomen en vermogen|Particuliere huishoudens excl. studenten'] = inkomen['Inkomen en vermogen|Particuliere huishoudens excl. studenten'].astype(float)
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten'].astype(float)
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden'].astype(float)
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin'].astype(float)
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind'].astype(float)
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)'].astype(float)
inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer'] = inkomen['Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer'].astype(float)

# 'Inkomen en vermogen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer'

# kolommen selecteren
inkomen = inkomen[['Unnamed: 0', 'Unnamed: 1', 'Inkomen en vermogen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer']]

# namen van kolommen aanpassen
inkomen.rename(columns={'Unnamed: 0': 'provincie',
                        'Unnamed: 1': 'jaar',
                        'Inkomen en vermogen|Particuliere huishoudens excl. studenten':'particuliere huishoudens excl. studenten', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten':'particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden': 'eenpersoons- huishouden, gem. besteedsbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin': 'eenouder- gezin, gem. besteedsbaar inkomen',
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind': 'paar zonder kind, gem. besteedsbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)':'paar met kinderen, gem. besteedsbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer':'inkomen als werknemer, gem. besteedsbaar inkomen' }, inplace = True)

inkomen.head()

### Aantal mensen per regio

# kolommen weg halen
del aantal_mensen["Unnamed: 2"] 
del aantal_mensen["Onderwerp"]
del aantal_mensen['2020']
#rijen weg halen
aantal_mensen = aantal_mensen.drop(index=13)

# kolom namen aanpassen
aantal_mensen.rename(columns={"Regio's": 'provincie',
                             '2019': 'pop_2019'}, inplace=True)

aantal_mensen.head()

### Opleidingen per regio

# rijen verwijderen
opleiding = opleiding.drop(index=14)
opleiding = opleiding.drop(index=15)
opleiding = opleiding.drop(index=16)
opleiding = opleiding.drop(index=17)
opleiding = opleiding.drop(index=18)
opleiding = opleiding.drop(index=19)
opleiding = opleiding.drop(index=20)
opleiding = opleiding.drop(index=21)
opleiding = opleiding.drop(index=22)
opleiding = opleiding.drop(index=23)
opleiding = opleiding.drop(index=24)
opleiding = opleiding.drop(index=25)
opleiding = opleiding.drop(index=26)
opleiding = opleiding.drop(index=27)
opleiding = opleiding.drop(index=28)
opleiding = opleiding.drop(index=29)
opleiding = opleiding.drop(index=30)
opleiding = opleiding.drop(index=31)

opleiding.reset_index(inplace=True)

# aanpassen de namen van rijen
opleiding.rename(columns={'0': 'provincie'}, inplace = True)

# kolommen selecteren
opleiding = opleiding[['provincie', 'Onderwijssoort', 'Totaal voortgezet onderwijs (vo)', 'Vavo', 'Totaal mbo (incl. extranei)',
                      'Hbo-associate degree', 'Hbo-bachelor', 'Hbo-master/vervolgopleiding', 'Wo-bachelor',
                      'Wo-master', 'Wo-doctoraal', 'Wo-vervolgopleiding']]

opleiding.head()

# Dataset mergen

populatie_inkomen = aantal_mensen.merge(inkomen)

populatie_inkomen_opleiding = populatie_inkomen.merge(opleiding)

populatie_inkomen_opleiding.head()

# Grafieken

## Inkomen histogram
col1, col2, col3 = st.columns(3)

with col1:
fig = px.histogram(data_frame=inkomen, x='provincie', y='particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen', 
                   title='Gemiddeld besteedbaar inkomen',
                   category_orders=dict(provincie = ['Groningen (PV)',
                                                     'Fryslân (PV)',
                                                     'Drenthe (PV)',
                                                     'Overijssel (PV)',
                                                     'Flevoland (PV)',
                                                     'Gelderland (PV)',
                                                     'Utrecht (PV)', 
                                                     'Noord-Holland (PV)',
                                                     'Zuid-Holland (PV)',
                                                     'Zeeland (PV)',
                                                     'Noord-Brabant (PV)',
                                                     'Limburg (PV)']),
                   color='provincie',
                   labels={'particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen': "Gemiddeld besteedbaar inkomen",
                     "provincie": "Provincies"})
fig.update_traces(opacity=0.8)
fig.show()
st.plotly_chart(fig)
inkomen.head(1)
with col2:
fig = px.histogram(data_frame=inkomen, x='provincie', y='particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen', 
                   title='Gemiddeld besteedbaar inkomen',
                   category_orders=dict(provincie = ['Groningen (PV)',
                                                     'Fryslân (PV)',
                                                     'Drenthe (PV)',
                                                     'Overijssel (PV)',
                                                     'Flevoland (PV)',
                                                     'Gelderland (PV)',
                                                     'Utrecht (PV)', 
                                                     'Noord-Holland (PV)',
                                                     'Zuid-Holland (PV)',
                                                     'Zeeland (PV)',
                                                     'Noord-Brabant (PV)',
                                                     'Limburg (PV)']),
                   color='provincie',
                   labels={'particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen': "Gemiddeld besteedbaar inkomen",
                     "provincie": "Provincies"})
fig.update_layout(updatemenus=[ dict( buttons=list([
                    dict(args=["provincie", "'Groningen (PV)'"],
                    label="Groningen",
                    method="restyle"),
                dict(args=["provincie", "Fryslân (PV)"],
                    label="Friesland",
                    method="restyle")]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.001, xanchor="left",
            y=1.15, yanchor="top"),])
fig.update_traces(opacity=0.8)
fig.show()
st.plotly_chart(fig)

with col3:
fig = px.histogram(data_frame=inkomen, x='provincie', y='particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen', 
                   title='Gemiddeld besteedbaar inkomen',
                   category_orders=dict(provincie = ['Groningen (PV)',
                                                     'Fryslân (PV)',
                                                     'Drenthe (PV)',
                                                     'Overijssel (PV)',
                                                     'Flevoland (PV)',
                                                     'Gelderland (PV)',
                                                     'Utrecht (PV)', 
                                                     'Noord-Holland (PV)',
                                                     'Zuid-Holland (PV)',
                                                     'Zeeland (PV)',
                                                     'Noord-Brabant (PV)',
                                                     'Limburg (PV)']),
                   color='provincie',
                   labels={'particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen': "Gemiddeld besteedbaar inkomen",
                     "provincie": "Provincies"})
fig.update_layout(updatemenus=[ dict( buttons=list([
                    dict(args=["provincie", "'Groningen (PV)'"],
                    label="Groningen",
                    method="restyle"),
                dict(args=["provincie", "Fryslân (PV)"],
                    label="Friesland",
                    method="restyle")]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.001, xanchor="left",
            y=1.15, yanchor="top"),])
fig.update_traces(opacity=0.8)
fig.show()
st.plotly_chart(fig)
inkomen.columns

## Inkomen scatterplot

### Aantal mensen per regio

aantal_mensen.reset_index()
aantal_mensen = aantal_mensen.drop(index=0)
fig = px.histogram(data_frame=aantal_mensen, x='provincie', y='pop_2019', 
                   title='Populatie per regio',
                   category_orders=dict(provincie = ['Groningen (PV)',
                                                     'Fryslân (PV)',
                                                     'Drenthe (PV)',
                                                     'Overijssel (PV)',
                                                     'Flevoland (PV)',
                                                     'Gelderland (PV)',
                                                     'Utrecht (PV)', 
                                                     'Noord-Holland (PV)',
                                                     'Zuid-Holland (PV)',
                                                     'Zeeland (PV)',
                                                     'Noord-Brabant (PV)',
                                                     'Limburg (PV)']),
                   color='provincie',
                   labels={'sum of pop_2019': "Populatie",
                    "provincie": "Provincies"})
fig.update_traces(opacity=0.8)
fig.show()
st.plotly_chart(fig)
## Scatter plot

populatie_inkomen_opleiding = populatie_inkomen_opleiding.drop(index=0)

populatie_inkomen_opleiding.head(1)

inkomen.columns

fig = px.scatter(data_frame=populatie_inkomen_opleiding, 
                 x='particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen', 
                 y='pop_2019',
                color='provincie',
                labels = {'pop_2019': "Populatie",
                    "particuliere huishoudens excl. studenten, gem. besteedsbaar inkomen": "Het gemiddelde besteedbare inkomen per huishouden"})
fig.show()
st.plotly_chart(fig)
