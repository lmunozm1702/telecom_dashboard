import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

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

cols = st.columns(3)
with cols[0]:
  ui.metric_card(title="Ingresos (miles de pesos)", content=income_kpi[0], description=income_kpi[1], key="metric_card_0")
with cols[1]:
  ui.metric_card(title="Acceso trimestral (cada 100 hogares)", content=acceses_kpi[0], description=acceses_kpi[1], key="metric_card_1")
with cols[2]:
  ui.metric_card(title="Eliminar ADSL (% conexiones)", content=adsl_kpi[0], description=adsl_kpi[1], key="metric_card_2")

#st.dataframe(df_quarters, use_container_width=True)
#st.dataframe(df_provinces, use_container_width=True)

