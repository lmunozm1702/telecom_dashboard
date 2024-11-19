import streamlit as st

def dashboard_title():
  ''' 
  Prints the title of the streamlit dashboard
  '''
  st.set_page_config(layout="wide", page_title='Telecom Dashboard - Internet Channel', page_icon=':chart_with_upwards_trend:')
  #st.subheader(':bar_chart: Panel de Control - Canal Internet')
  #st.markdown('---')
  
def get_income_kpi(df):
  '''
  Returns the value and the description of the KPI
  Increase a 1% plus the IPC of the previous quarter.

  Parameters
  ----------
  df: pd.DataFrame with the data for accesses by quarter

  Returns
  -------
  list: [value, description]
  '''

  df = df.sort_values(['Periodo'])
  df.reset_index(drop=True, inplace=True)

  ipc_previuos_qarter = (25.1+24.7+15.9)
  previous_income = df['Ingresos (miles de pesos)'].iloc[-2]
  actual_income = df['Ingresos (miles de pesos)'].iloc[-1]
  proyected_income = round(previous_income * (1+ipc_previuos_qarter/100) * 1.01,2)
  growth = round((actual_income/proyected_income*100) - 100, 2)

  return [f"{actual_income:,}", f"{growth}% respecto del objetivo ({proyected_income:,})"]  

def get_accesses_kpi(df):
  '''
  Returns the value and the description of the KPI
  Increase a 2% from the previous quarter

  Parameters
  ----------
  df: pd.DataFrame with the data for accesses by quarter

  Returns
  -------
  list: [value, description]
  '''

  df = df.sort_values(['Periodo'])
  df.reset_index(drop=True, inplace=True)

  actual_accesses = df['Accesos por cada 100 hogares'].iloc[-1]
  previous_accesses = df['Accesos por cada 100 hogares'].iloc[-2]
  proyected_accesses = round(previous_accesses * 1.02,2)
  growth = round((actual_accesses/proyected_accesses*100) - 100, 2)

  return [actual_accesses, f"{growth}% respecto del objetivo ({proyected_accesses})"]

def get_adsl_kpi(df):
  '''
  Returns the value and the description of the KPI
  Decrease a 5% from the previous quarter

  Parameters
  ----------
  df: pd.DataFrame with the data for accesses by quarter

  Returns
  -------
  list: [value, description]
  '''

  df = df.sort_values(['Periodo'])
  df.reset_index(drop=True, inplace=True)
  actual_adsl = df['ADSL'].iloc[-1]
  previous_adsl = df['ADSL'].iloc[-2]
  proyected_adsl = round(previous_adsl * 0.95,2)
  growth = round(100 - (actual_adsl/proyected_adsl*100), 2)

  return [f"{actual_adsl:,}", f"{growth}% respecto del objetivo ({proyected_adsl:,})"]

