## Importeren van packages
import streamlit as st
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
import seaborn as sns
from streamlit_folium import folium_static
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = 'Dashboard van inkomen en inleiding', layout = 'wide')
st.title("Dashboard van inkomen en inleiding")
# st.info('''Dit interactieve dashboard geeft weer hoe de geïnspecteerde data verdeeld is. Het dashboard geeft bijvoorbeeld inzichten over hoe de brandstoftypes van auto’s verdeeld zijn, hoe laadstations verdeeld zijn over Nederland en hoe laadtijden per sessie verdeeld zijn.''')
# st.header("Databronnen")
# st.markdown('''De data die gebruikt wordt voor dit dashboard komt van drie verschillende bronnen.''')
st.sidebar.write('''Dashboard is gemaakt door Amber van der Pol (500803136) en Oussama Abou (500803060). \n'''
                 '''**Bron:** de datasets komen allemaal van het cbs. ''')

# Importen van de data
df = pd.read_csv('Opleiding_inkomen.csv')


col1, col2 = st.columns(2)

with col1: 
  st.markdown('''**Inkomen en opleiding**  
  Allemaal informatie over de inkomen en opleiding.  
  
  •	Wat gaan we zien?
  •	Wat is opvallend?
  •	Andere leuke informatie''')
with col2: 
  st.markdown('''**Kaart**''')
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
    Inwoners.add_child(folium.vector_layers.Circle(radius = row_values['pop_radius'], location = row_values['middelste_punt'], fill = True, color='yellow').add_to(m))
    Mbo.add_child(folium.vector_layers.Circle(radius = row_values['Mbo_radius'], location = row_values['middelste_punt'], fill = True, color='red').add_to(m))
    Hbo.add_child(folium.vector_layers.Circle(radius = row_values['Hbo_radius'], location = row_values['middelste_punt'], fill = True, color='blue').add_to(m))
    Wo.add_child(folium.vector_layers.Circle(radius = row_values['Wo_radius'], location = row_values['middelste_punt'], fill = True, color='purple').add_to(m))
    Eenpersoonshuishouden.add_child(folium.vector_layers.Circle(radius = row_values['eenpersoonshuishouden_radius'], location = row_values['middelste_punt'], fill = True, color='dimgrey').add_to(m))
    Particulierehuishoudens.add_child(folium.vector_layers.Circle(radius = row_values['particulierehuishouden_radius'], location = row_values['middelste_punt'], fill = True, color='lightcoral').add_to(m))
    Paarkinderen.add_child(folium.vector_layers.Circle(radius = row_values['paarmetkinderen_radius'], location = row_values['middelste_punt'], fill = True, color='skyblue').add_to(m))
  folium.LayerControl().add_to(m)
    # # folium.TileLayer('cartodbpositron', name='Onderwijs niveau').add_to(LayerControl)
    # display(m)
    # st.map(m)
  folium_static(m, width = 500, height = 600)

  ## Boxplot
col1, col2 = st.columns(2)
with col1: 
  ### Inkomen
  fig1 = go.Figure()
  fig1.add_trace(go.Box(y=df['particuliere huishoudens excl. studenten, gem. besteedbaar inkomen'], name = 'Particuliere huishoudens excl. studenten' , marker_color='rgb(127, 60, 141)'))
  fig1.add_trace(go.Box(y=df['eenpersoons- huishouden, gem. besteedbaar inkomen'], name = 'Eenpersoons- huishouden', marker_color='rgb(17, 165, 121)'))
  fig1.add_trace(go.Box(y=df['eenouder- gezin, gem. besteedbaar inkomen'], name = 'Eenouder- gezin', marker_color='rgb(57, 105, 172)'))
  fig1.add_trace(go.Box(y=df['paar zonder kind, gem. besteedbaar inkomen'], name = 'Paar zonder kind', marker_color='rgb(242, 183, 1)'))
  fig1.add_trace(go.Box(y=df['paar met kinderen, gem. besteedbaar inkomen'], name = 'Paar met kinderen', marker_color='rgb(231, 63, 116)'))
  fig1.add_trace(go.Box(y=df['inkomen als werknemer, gem. besteedbaar inkomen'], name = 'Inkomen als werknemer', marker_color='rgb(128, 186, 90)'))
  fig1.update_layout(title_text = 'Gemiddeld besteedbaar inkomen per soort huishouden', legend_title='Verschillende huishoudens:')
  fig1.update_yaxes(title = 'Gemiddeld besteedbaar inkomen')
  fig1.show()
  st.plotly_chart(fig1, layout = 'small')
with col2:
  ### Opleiding
  fig2 = go.Figure()
  fig2.add_trace(go.Box(y=df['Totaal voortgezet onderwijs (vo)'], name = 'Totaal voortgezet onderwijs (vo)', marker_color='rgb(127, 60, 141)' ))
  fig2.add_trace(go.Box(y=df['Vavo'], name = 'Vavo', marker_color='rgb(165, 170, 153)'))
  fig2.add_trace(go.Box(y=df['Totaal mbo (incl. extranei)'], name = 'Totaal mbo (incl. extranei)', marker_color='rgb(17, 165, 121)'))
  fig2.add_trace(go.Box(y=df['Hbo-associate degree'], name = 'Hbo-associate degree', marker_color='rgb(57, 105, 172)'))
  fig2.add_trace(go.Box(y=df['Hbo-bachelor'], name = 'Hbo-bachelor', marker_color='rgb(242, 183, 1)'))
  fig2.add_trace(go.Box(y=df['Hbo-master/vervolgopleiding'], name = 'Hbo-master/vervolgopleiding', marker_color='rgb(231, 63, 116)'))
  fig2.add_trace(go.Box(y=df['Wo-bachelor'], name = 'Wo-bachelor', marker_color='rgb(128, 186, 90)'))
  fig2.add_trace(go.Box(y=df['Wo-master'],  name = 'Wo-master', marker_color='rgb(230, 131, 16)'))
  fig2.add_trace(go.Box(y=df['Wo-doctoraal'],  name = 'Wo-doctoraal', marker_color='rgb(0, 134, 149)'))
  fig2.add_trace(go.Box(y=df['Wo-vervolgopleiding'], name = 'Wo-vervolgopleiding', marker_color='rgb(207, 28, 144)'))
  fig2.update_layout(title_text = 'Aantal afgestudeerde per opleidingssoort', legend_title='Opleiding:')
  fig2.update_traces(width=1)
  fig2.update_yaxes(title = 'Aantal afgestudeerde')
  fig2.show()
  st.plotly_chart(fig2)



# Subscatter plot
fig = make_subplots(rows=3, cols=3, subplot_titles=("Mbo scholieren","Hbo studenten", "Wo studenten"))
fig.add_trace(go.Scatter(x=df['Totaal mbo (incl. extranei)_p'], y=df['particuliere huishoudens excl. studenten, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Hbo_p'], y=df['particuliere huishoudens excl. studenten, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold),row=1, col=2)
fig.add_trace(go.Scatter(x=df['Wo_p'], y=df['particuliere huishoudens excl. studenten, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold),row=1, col=3)
fig.add_trace(go.Scatter(x=df['Totaal mbo (incl. extranei)_p'], y=df['eenpersoons- huishouden, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Hbo_p'], y=df['eenpersoons- huishouden, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold), row=2, col=2)

fig.add_trace(go.Scatter(x=df['Wo_p'], y=df['eenpersoons- huishouden, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold), row=2, col=3)
fig.add_trace(go.Scatter(x=df['Totaal mbo (incl. extranei)_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold), row=3, col=1)
fig.add_trace(go.Scatter(x=df['Hbo_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold), row=3, col=2)
fig.add_trace(go.Scatter(x=df['Wo_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'], mode='markers+text', marker_color=px.colors.qualitative.Bold), row=3, col=3)

fig['layout']['yaxis1']['title']='Paar met<br>kinderen'
fig['layout']['yaxis4']['title']='Eenpersoons-<br>huishouden'
fig['layout']['yaxis7']['title']='Particuliere huishoudens<br>excl. student'

fig.update_yaxes(range=[15, 80])
fig.update_xaxes(range=[0, 1.2])
fig.update_layout(height=800, width=900, title_text="Inkomen en opleiding",showlegend=False)
fig.show()
st.plotly_chart(fig)


# Lineaire regressiesns_ax3 = sns.regplot(x=df['Totaal mbo (incl. extranei)_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'], ci=None)
sns_ax3.set_xlabel('Percentage Mbo studenten')
sns_ax3.set_ylabel('Gemiddeld besteedbaar inkomen,\n paar met kinderen')
sns_ax3.set_title('Percentage Mbo studenten \nper gemiddeld besteedbaar inkomen, paar met kinderen')
sns_ax3.set(ylim=(60,80), xlim=(0.6,1.3))
#go.Scatter(x=df['Totaal mbo (incl. extranei)_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'])
#TEKST: Bij deze grafiek hoort een corelatiecoefficient van -0.75. Dit betekent dat er een redelijk sterke conclusie kan worden getrokken dat bij een paar met kinderen met een hoger besteedbaar inkomen minder Mbo studeren
#go.Scatter(x=df['Totaal mbo (incl. extranei)_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'])
#TEKST: Bij deze grafiek hoort een corelatiecoefficient van -0.75. Dit betekent dat er een redelijk sterke conclusie kan worden getrokken dat bij een paar met kinderen met een hoger besteedbaar inkomen minder Mbo studeren
st.pyplot(plt)
#TEKST: Bij deze grafiek hoort een corelatiecoefficient van -0.75. Dit betekent dat er een redelijk sterke conclusie kan worden getrokken dat bij een paar met kinderen met een hoger besteedbaar inkomen minder Mbo studeren

sns_ax2 = sns.regplot(x=df['Hbo_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'], ci=None)
sns_ax2.set_title('Percentage Hbo studenten per \n gem besteedbaar inkomen, paar met kinderen')
sns_ax2.set_ylabel('Gemiddeld besteedbaar inkomen,\n paar met kinderen')
sns_ax2.set_xlabel('Percentage Hbo studenten')
sns_ax2.set(ylim=(60,80), xlim=(0.28,0.50))
#TEKST: In onderstaand grafiek is te zien hoe het percentage universiteits studenten lineair stijgt als het gemiddelde besteedbare inkomen van een paar met kinderen ook stijgt. bij een lage aantal studenten is te zien dat het inkomen geclusterd is. naarmate het inkomen stijgt is de afstand tot de regressielijn per provincie groter. correlatiecoefficient is 0.71. wat betekent dat er een redelijk verband is tussen de twee variabelen.st.pyplot(plt)
#TEKST: In onderstaand grafiek is te zien hoe het percentage universiteits studenten lineair stijgt als het gemiddelde besteedbare inkomen van een paar met kinderen ook stijgt. bij een lage aantal studenten is te zien dat het inkomen geclusterd is. naarmate het inkomen stijgt is de afstand tot de regressielijn per provincie groter. correlatiecoefficient is 0.71. wat betekent dat er een redelijk verband is tussen de twee variabelen.

df = df.loc[df['Wo_p']<1]
df['Wo_p']
sns_ax1 = sns.regplot(x=df['Wo_p'], y=df['particuliere huishoudens excl. studenten, gem. besteedbaar inkomen'], ci=None)
sns_ax1.set_title('Percentage Wo studenten per \n particuliere huishoudens exc. studententen')
sns_ax1.set_ylabel('Particuliere huishoudens excl. studententen')
sns_ax1.set_xlabel('Percentage Wo studenten')
#go.Scatter(x=df['Totaal mbo (incl. extranei)_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'])
#In de grafiek is een duidelijke outlier te zien. Die er voor zorgt da
st.pyplot(plt)

#go.Scatter(x=df['Totaal mbo (incl. extranei)_p'], y=df['paar met kinderen, gem. besteedbaar inkomen'])
#In de grafiek is een duidelijke outlier te zien. Die er voor zorgt da


  ## Boxplot
col1, col2 = st.columns(2)
with col1: 
  ### Inkomen
  df_labels = df[['particuliere huishoudens excl. studenten, gem. besteedbaar inkomen', 'eenpersoons- huishouden, gem. besteedbaar inkomen', 'eenouder- gezin, gem. besteedbaar inkomen', 'paar zonder kind, gem. besteedbaar inkomen', 'paar met kinderen, gem. besteedbaar inkomen', 'inkomen als werknemer, gem. besteedbaar inkomen']]
  df_labels = list(df_labels.columns.tolist())
  provincie = ["Groningen (PV)", 'Fryslân (PV)','Drenthe (PV)','Overijssel (PV)','Flevoland (PV)','Gelderland (PV)','Utrecht (PV)','Noord-Holland (PV)','Zuid-Holland (PV)','Zeeland (PV)','Noord-Brabant (PV)','Limburg (PV)']
  color_trace = ["rgb(255, 211, 92)", "rgb(68, 175, 105)", "rgb(133, 199, 242)", "rgb(252, 103, 34)","rgb(213, 114, 148)","rgb(255, 0, 110)","rgb(9, 68, 93)","rgb(131, 56, 236)","rgb(255, 133, 214)","rgb(58, 134, 255)","rgb(255, 251, 29)","rgb(119, 228, 80)" ] # maak lijst met kleuren
  fig = go.Figure()
  j = 0
  dropdown_buttons = []
  for i in df_labels:
    fig.add_trace(go.Bar(x = df['provincie'], y = df[i], name = i, text=df[i], marker_color=px.colors.qualitative.Bold))
    dropdown_buttons.append({'label':df_labels[j], 'method': 'update', 'args': [{"visible":[x==i for x in df_labels]}]})
    j += 1

  fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
  fig.update_layout({'updatemenus':[{'active':True, 'buttons': dropdown_buttons, 'x': 1, 'y': 1.2}]},annotations = [{'text':"Inkomen per soort", 'font_size':20, 'x': 0, 'xref':"paper", 'y':1.2, 'yref':"paper",'showarrow':False}], showlegend = False)
  fig.update_yaxes(range=[0, 80], title = 'inkomen in €1000 ')
  fig.show()  
  st.plotly_chart(fig,)
with col2:
  opleiding_labels = df[[ 'Totaal voortgezet onderwijs (vo)_p', 'Totaal mbo (incl. extranei)_p','Vavo_p', 'Hbo-associate degree_p', 'Hbo-bachelor_p', 'Hbo-master/vervolgopleiding_p', 'Wo-bachelor_p', 'Wo-master_p','Wo-doctoraal_p', 'Wo-vervolgopleiding_p']]
  opleiding_labels = list(opleiding_labels.columns.tolist())
  fig = go.Figure()
  j = 0
  dropdown_buttons = []
  for i in opleiding_labels:
    fig.add_trace(go.Bar(x = df['provincie'], y = df[i], name = i, text=df[i], marker_color=px.colors.qualitative.Bold))
    dropdown_buttons.append({'label':opleiding_labels[j], 'method': 'update', 'args': [{"visible":[x==i for x in opleiding_labels]}]})
    j += 1
  fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
  fig.update_layout({'updatemenus':[{'active':True, 'buttons': dropdown_buttons, 'x': 1, 'y': 1.2}]},annotations = [{'text':"Opleiding per niveau", 'font_size':20,'x':0, 'xref':"paper", 'y':1.2, 'yref':"paper",'showarrow':False}],showlegend = False)
  fig.update_layout(yaxis_range=[0,1.5])
  fig.show()
  st.plotly_chart(fig)

