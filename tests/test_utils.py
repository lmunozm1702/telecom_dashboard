import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname("../libs")))
import libs.utils as utils
from definitions import ROOT_DIR


def test_normalize_file_name():
  '''
  Test the normalize_file_name function
  '''
  assert utils.normalize_file_name("file name") == "file_name"
  assert utils.normalize_file_name("file-name") == "file_name"
  assert utils.normalize_file_name("file náme with spaces") == "file_name_with_spaces"
  assert utils.normalize_file_name("file-name-wíth-dashes") == "file_name_with_dashes"

def test_get_xls_sheets_list():
  '''
  Test the get_xls_sheets_list function
  '''
  assert 'Ingresos ' in utils.get_xls_sheets_list('/data_files/test.xlsx')

def test_save_xls_sheets_to_parquet():
  '''
  Test the save_xls_sheets_to_parquet function
  '''
  sheet_list = utils.get_xls_sheets_list('/data_files/test.xlsx')
  utils.save_xls_sheets_to_parquet( sheet_list, '/data_files/test.xlsx', '/data_files')
  assert os.path.exists(ROOT_DIR + '/data_files/ingresos_.parquet')  
