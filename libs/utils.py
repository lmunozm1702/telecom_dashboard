import pandas as pd
from unidecode import unidecode
from definitions import ROOT_DIR

def get_xls_sheets_list(xls_file):
  '''
  Get the list of sheets in an Excel file

  Parameters
  ----------
  xls_file: path to the Excel file from root ex "/data_files/internet.xlsx"

  Returns
  -------
  list: list of sheet names into de file  
  '''
  
  xls = pd.ExcelFile(ROOT_DIR + xls_file)
  return xls.sheet_names
  
def save_xls_sheets_to_parquet(xls_sheet_names, xls_file, save_path):
  '''
  Save each sheet on the list into a parquet file

  Parameters
  ----------
  xls_sheet_names: list of sheet names into the file
  xls_file: path to the Excel file
  save_path: path to save the parquet files from root ex "/data_files"
  '''
  for xls_sheet_name in xls_sheet_names:
    pd.read_excel(ROOT_DIR + xls_file, sheet_name=xls_sheet_name).to_parquet(ROOT_DIR + save_path + '/' + normalize_file_name(xls_sheet_name) + '.parquet')

def normalize_file_name(file_name):
  '''
  Normalize a file name, removing spaces and special characters and converting to lowercase

  Parameters
  ----------
  file_name: file name

  Returns
  -------
  str: normalized file name
  '''
  return unidecode(file_name.replace(' ', '_').replace('-', '_').lower())

def get_xls_sheet_data(xls_file, sheet_name):
  '''
  Get the data from a sheet of an Excel file

  Parameters
  ----------
  xls_file: path to the Excel file
  sheet_name: name of the sheet

  Returns
  -------
  pd.DataFrame: data from the sheet
  '''
  return pd.read_excel(ROOT_DIR + xls_file, sheet_name=sheet_name)