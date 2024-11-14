import sys
import os

sys.path.append(os.path.dirname(os.path.dirname("../libs/libs")))
import libs.utils as utils

sheets_list = utils.get_xls_sheets_list('/data_files/internet.xlsx')

utils.save_xls_sheets_to_parquet(sheets_list, '/data_files/internet.xlsx', '/data_files')  



