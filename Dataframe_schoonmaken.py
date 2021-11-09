## Importeren van packages

import pandas as pd
import matplotlib.pyplot as plt
import os
import requests
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd

import warnings
warnings.filterwarnings('ignore')

## Importeren van de data

inkomen = pd.read_csv('Inkomen_per_regio.csv', delimiter = ';')
aantal_mensen = pd.read_csv('Aantal_mensen_per_regio.csv', delimiter=';')
opleiding = pd.read_csv('Opleiding_per_regio.csv', delimiter =';')

geo_df=gpd.read_file('provincie_nederland.json')
geo_df['PROV_NAAM']=geo_df['PROV_NAAM'] +str(' (PV)')

# # API
# from urllib.request import urlopen, Request
# response = requests.get("https://data.overheid.nl/community/datarequest/819")
# print(response.status_code)
# print(response.text) # Dit is een stuk tekst
# response.json() # dit is een Python dictionary


## File opschonen

### Inkomen per regio

#MAXIMAAL 1 KEER RUNNEN! Anders worden er kolommen verwijderd die niet verwijderd moeten worden.
# rijen weg halen
inkomen = inkomen.drop(index=0)
inkomen = inkomen.drop(index=14)
inkomen.reset_index(inplace=True)

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
inkomen = inkomen[['Unnamed: 0', 'Inkomen en vermogen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer']]

# namen van kolommen aanpassen
inkomen.rename(columns={'Unnamed: 0': 'provincie',
                        'Inkomen en vermogen|Particuliere huishoudens excl. studenten':'particuliere huishoudens excl. studenten', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten':'particuliere huishoudens excl. studenten, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden': 'eenpersoons- huishouden, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin': 'eenouder- gezin, gem. besteedbaar inkomen',
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind': 'paar zonder kind, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)':'paar met kinderen, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer':'inkomen als werknemer, gem. besteedbaar inkomen' }, inplace = True)

### Aantal mensen per regio
De kleuren zouden overal nog kunnen worden aangepast

# kolommen weg halen
del aantal_mensen["Unnamed: 2"] 
del aantal_mensen["Onderwerp"]
del aantal_mensen['2020']
#rijen weg halen
aantal_mensen = aantal_mensen.drop(index=13)

# kolom namen aanpassen
aantal_mensen.rename(columns={"Regio's": 'provincie',
                             '2019': 'pop_2019'}, inplace=True)

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
opleiding = opleiding[['provincie', 'Totaal voortgezet onderwijs (vo)', 'Vavo', 'Totaal mbo (incl. extranei)',
                      'Hbo-associate degree', 'Hbo-bachelor', 'Hbo-master/vervolgopleiding', 'Wo-bachelor',
                      'Wo-master', 'Wo-doctoraal', 'Wo-vervolgopleiding']]

opleiding['Totaal voortgezet onderwijs (vo)'] = opleiding['Totaal voortgezet onderwijs (vo)'].astype(float)
opleiding['Vavo']=opleiding['Vavo'].astype(float)
opleiding['Totaal mbo (incl. extranei)'] = opleiding['Totaal mbo (incl. extranei)'].astype(float)
opleiding['Hbo-associate degree'] = opleiding['Hbo-associate degree'].astype(float)
opleiding['Hbo-bachelor'] = opleiding['Hbo-bachelor'].astype(float)
opleiding['Hbo-master/vervolgopleiding'] = opleiding['Hbo-master/vervolgopleiding'].astype(float)
opleiding['Wo-bachelor'] = opleiding['Wo-bachelor'].astype(float)
opleiding['Wo-master'] = opleiding['Wo-master'].astype(float)
opleiding['Wo-doctoraal'] = opleiding['Wo-doctoraal'].astype(float)
opleiding['Wo-vervolgopleiding'] = opleiding['Wo-vervolgopleiding'].astype(float)


# Opleidingen samenvoegen
opleiding['Hbo'] = opleiding['Hbo-associate degree']+opleiding['Hbo-bachelor']+opleiding['Hbo-master/vervolgopleiding']
opleiding['Hbo']

### Geo

geo_df = geo_df[['PROV_NAAM', 'geometry']] # kolommen selecteren

# Dataset mergen
De datasets populatie, inkomen en opleiding worden samengevoegd.

populatie_inkomen = aantal_mensen.merge(inkomen)

df_zondergeo = populatie_inkomen.merge(opleiding)

df=pd.merge(df_zondergeo, geo_df, how = 'inner', left_on = 'provincie', right_on = 'PROV_NAAM', validate = 'many_to_one')

df

## Percentages van opleiding

df['pop_2019']
df.columns

df['Totaal voortgezet onderwijs (vo)_p']=df['Totaal voortgezet onderwijs (vo)']/df['pop_2019']*100
df['Totaal mbo (incl. extranei)_p'] = df['Totaal mbo (incl. extranei)']/df['pop_2019']*100
df['Vavo_p'] = df['Vavo']/df['pop_2019']*100
df['Totaal mbo (incl. extranei)_p'] = df['Totaal mbo (incl. extranei)']/df['pop_2019']*100
df['Hbo-associate degree_p'] = df['Hbo-associate degree']/df['pop_2019']*100
df['Hbo-bachelor_p'] = df['Hbo-bachelor']/df['pop_2019']*100
df['Hbo-master/vervolgopleiding_p'] = df['Hbo-master/vervolgopleiding']/df['pop_2019']*100
df['Wo-bachelor_p'] = df['Wo-bachelor']/df['pop_2019']*100
df['Wo-master_p'] = df['Wo-master']/df['pop_2019']*100
df['Wo-doctoraal_p'] = df['Wo-doctoraal']/df['pop_2019']*100
df['Wo-vervolgopleiding_p'] = df['Wo-vervolgopleiding']/df['pop_2019']*100

## Opleidingen samenvoegen
Hbo en Wo

df['Hbo'] = df['Hbo-associate degree']+ df['Hbo-bachelor'] + df['Hbo-master/vervolgopleiding']
df['Wo'] = df['Wo-bachelor']+df['Wo-master']+df['Wo-doctoraal']+df['Wo-vervolgopleiding']
df.head()

## Importeren van packages

import pandas as pd
import matplotlib.pyplot as plt
import os
import requests
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd

import warnings
warnings.filterwarnings('ignore')

## Importeren van de data

inkomen = pd.read_csv('Inkomen_per_regio.csv', delimiter = ';')

aantal_mensen = pd.read_csv('Aantal_mensen_per_regio.csv', delimiter=';')

opleiding = pd.read_csv('Opleiding_per_regio.csv', delimiter =';')

geo_df=gpd.read_file('provincie_nederland.json')
geo_df['PROV_NAAM']=geo_df['PROV_NAAM'] +str(' (PV)')

# # API
# from urllib.request import urlopen, Request
# response = requests.get("https://data.overheid.nl/community/datarequest/819")
# print(response.status_code)
# print(response.text) # Dit is een stuk tekst
# response.json() # dit is een Python dictionary


## File opschonen

### Inkomen per regio

#MAXIMAAL 1 KEER RUNNEN! Anders worden er kolommen verwijderd die niet verwijderd moeten worden.
# rijen weg halen
inkomen = inkomen.drop(index=0)
inkomen = inkomen.drop(index=14)
inkomen.reset_index(inplace=True)

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
inkomen = inkomen[['Unnamed: 0', 'Inkomen en vermogen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)', 'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer']]

# namen van kolommen aanpassen
inkomen.rename(columns={'Unnamed: 0': 'provincie',
                        'Inkomen en vermogen|Particuliere huishoudens excl. studenten':'particuliere huishoudens excl. studenten', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Particuliere huishoudens excl. studenten':'particuliere huishoudens excl. studenten, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenpersoonshuishouden': 'eenpersoons- huishouden, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Eenoudergezin': 'eenouder- gezin, gem. besteedbaar inkomen',
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, zonder kind': 'paar zonder kind, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Type: Paar, met kind(eren)':'paar met kinderen, gem. besteedbaar inkomen', 
                        'Inkomen en vermogen|Inkomen van particuliere huishoudens|Gemiddeld besteedbaar inkomen|Bron: Inkomen als werknemer':'inkomen als werknemer, gem. besteedbaar inkomen' }, inplace = True)

### Aantal mensen per regio
De kleuren zouden overal nog kunnen worden aangepast

# kolommen weg halen
del aantal_mensen["Unnamed: 2"] 
del aantal_mensen["Onderwerp"]
del aantal_mensen['2020']
#rijen weg halen
aantal_mensen = aantal_mensen.drop(index=13)

# kolom namen aanpassen
aantal_mensen.rename(columns={"Regio's": 'provincie',
                             '2019': 'pop_2019'}, inplace=True)

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
opleiding = opleiding[['provincie', 'Totaal voortgezet onderwijs (vo)', 'Vavo', 'Totaal mbo (incl. extranei)',
                      'Hbo-associate degree', 'Hbo-bachelor', 'Hbo-master/vervolgopleiding', 'Wo-bachelor',
                      'Wo-master', 'Wo-doctoraal', 'Wo-vervolgopleiding']]

opleiding['Totaal voortgezet onderwijs (vo)'] = opleiding['Totaal voortgezet onderwijs (vo)'].astype(float)
opleiding['Vavo']=opleiding['Vavo'].astype(float)
opleiding['Totaal mbo (incl. extranei)'] = opleiding['Totaal mbo (incl. extranei)'].astype(float)
opleiding['Hbo-associate degree'] = opleiding['Hbo-associate degree'].astype(float)
opleiding['Hbo-bachelor'] = opleiding['Hbo-bachelor'].astype(float)
opleiding['Hbo-master/vervolgopleiding'] = opleiding['Hbo-master/vervolgopleiding'].astype(float)
opleiding['Wo-bachelor'] = opleiding['Wo-bachelor'].astype(float)
opleiding['Wo-master'] = opleiding['Wo-master'].astype(float)
opleiding['Wo-doctoraal'] = opleiding['Wo-doctoraal'].astype(float)
opleiding['Wo-vervolgopleiding'] = opleiding['Wo-vervolgopleiding'].astype(float)


# Opleidingen samenvoegen
opleiding['Hbo'] = opleiding['Hbo-associate degree']+opleiding['Hbo-bachelor']+opleiding['Hbo-master/vervolgopleiding']
opleiding['Hbo']

### Geo

geo_df = geo_df[['PROV_NAAM', 'geometry']] # kolommen selecteren

# Dataset mergen
De datasets populatie, inkomen en opleiding worden samengevoegd.

populatie_inkomen = aantal_mensen.merge(inkomen)

df_zondergeo = populatie_inkomen.merge(opleiding)

df=pd.merge(df_zondergeo, geo_df, how = 'inner', left_on = 'provincie', right_on = 'PROV_NAAM', validate = 'many_to_one')

df

## Percentages van opleiding

df['pop_2019']
df.columns

df['Totaal voortgezet onderwijs (vo)_p']=df['Totaal voortgezet onderwijs (vo)']/df['pop_2019']*100
df['Totaal mbo (incl. extranei)_p'] = df['Totaal mbo (incl. extranei)']/df['pop_2019']*100
df['Vavo_p'] = df['Vavo']/df['pop_2019']*100
df['Totaal mbo (incl. extranei)_p'] = df['Totaal mbo (incl. extranei)']/df['pop_2019']*100
df['Hbo-associate degree_p'] = df['Hbo-associate degree']/df['pop_2019']*100
df['Hbo-bachelor_p'] = df['Hbo-bachelor']/df['pop_2019']*100
df['Hbo-master/vervolgopleiding_p'] = df['Hbo-master/vervolgopleiding']/df['pop_2019']*100
df['Wo-bachelor_p'] = df['Wo-bachelor']/df['pop_2019']*100
df['Wo-master_p'] = df['Wo-master']/df['pop_2019']*100
df['Wo-doctoraal_p'] = df['Wo-doctoraal']/df['pop_2019']*100
df['Wo-vervolgopleiding_p'] = df['Wo-vervolgopleiding']/df['pop_2019']*100

## Opleidingen samenvoegen
Hbo en Wo

df['Hbo'] = df['Hbo-associate degree']+ df['Hbo-bachelor'] + df['Hbo-master/vervolgopleiding']
df['Wo'] = df['Wo-bachelor']+df['Wo-master']+df['Wo-doctoraal']+df['Wo-vervolgopleiding']
df.head()

# Dataset opslaan in csv

df.to_csv('Opleiding_inkomen.csv', index = False)
