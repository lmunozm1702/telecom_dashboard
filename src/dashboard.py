import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname("../libs")))
import libs.utils as utils
import libs.dash_utils as dash_utils


#@st.cache_data
df_quarters = utils.get_parquet_file_data('/data_files/trimestres_eda_clean.parquet')
df_quarters = df_quarters.drop(['level_0', 'index'], axis=1)

df_provinces = utils.get_parquet_file_data('/data_files/provincias_eda_clean.parquet')
df_provinces = df_provinces.drop(['level_0', 'index'], axis=1)

dash_utils.dashboard_title()

st.subheader('KPIs')
income_kpi = dash_utils.get_income_kpi(df_quarters)
acceses_kpi = dash_utils.get_accesses_kpi(df_quarters)
adsl_kpi = dash_utils.get_adsl_kpi(df_quarters)

cols = st.columns(3, gap='large')
with cols[0]:
  ui.metric_card(title="Ingresos (miles de pesos)", content=income_kpi[0], description=income_kpi[1], key="metric_card_0")
with cols[1]:
  ui.metric_card(title="Acceso trimestral (cada 100 hogares)", content=acceses_kpi[0], description=acceses_kpi[1], key="metric_card_1")
with cols[2]:
  ui.metric_card(title="Eliminar ADSL (% conexiones)", content=adsl_kpi[0], description=adsl_kpi[1], key="metric_card_2")

#st.dataframe(df_quarters, use_container_width=True)
#st.dataframe(df_provinces, use_container_width=True)
st.markdown("---")
cols = st.columns(3, vertical_alignment='bottom')
with cols[0]:
  st.subheader('Análisis trimestral')
  fig = px.line(df_quarters, x="Periodo", y="Ingresos (miles de pesos)", title="Ingresos por trimestre")
  st.plotly_chart(fig, use_container_width=True)
with cols[1]:
  #st.subheader('Accesos por trimestre')
  fig = px.line(df_quarters, x="Periodo", y="Accesos por cada 100 hogares", title="Accesos totales por trimestre")  
  st.plotly_chart(fig, use_container_width=True)
with cols[2]:
  #st.subheader('Accesos por tecnología')
  tech_list = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']
  sel_tech = st.selectbox('Tecnología', tech_list)

  fig = px.line(df_quarters[['Periodo', sel_tech]], x="Periodo", y=sel_tech, title="Accesos por tecnología por trimestre")
  fig.update_layout(yaxis_title='Accesos')
  st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

cols = st.columns(2, vertical_alignment='bottom', gap='large')
with cols[0]:
  st.subheader("Análisis por provincia")
  year_list = df_provinces['Año'].sort_values(ascending=False).unique().tolist()
  selected_year = year_list[0]
  selected_year = st.selectbox('Año', year_list)

  fig = px.bar(df_provinces[df_provinces['Año'] == selected_year], x="Provincia", y="Accesos por cada 100 hogares", title=f"Accesos por provincia {selected_year}")
  fig.update_layout(yaxis_title='Accesos')
  st.plotly_chart(fig, use_container_width=True)

with cols[1]:
 df_provinces = df_provinces.sort_values(by=['Provincia', 'Trimestre'], ascending=[True, False])
 st.dataframe(df_provinces[df_provinces['Año'] == selected_year], use_container_width=True, hide_index=True, column_config={
    'Año': None,
    'Periodo': None,
    'Provincia': 'Provincia',
    'Mbps (Media de bajada)': 'Mbps (Media de bajada)',    
    'Accesos por cada 100 hab': None,
    'Accesos por cada 100 hogares': None,
    'ADSL': 'ADSL',
    'Cablemodem': 'Cablemodem',
    'Fibra óptica': 'Fibra óptica',
    'Wireless': 'Wireless',
    'Otros': 'Otros',
    'Total': None
 }, height=500)

st.markdown("---")